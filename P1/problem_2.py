# -*- coding: utf-8 -*-
# problem_2.py
# Author: Matheus Dal Mago
# 2020

import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    path_list = []

    def find_files_recursive_helper(my_path):
        if not os.path.exists(my_path):
            return None

        if os.path.isfile(my_path):
            if my_path.endswith(suffix):
                path_list.append(my_path)  # O(1)
            return

        # if os.path.isdir(my_path):  # Check not really needed
        for sub_path in os.listdir(my_path):
            find_files_recursive_helper(os.path.join(my_path, sub_path))

    find_files_recursive_helper(path)
    return path_list


if __name__ == "__main__":
    test_case_1 = find_files(".c", "./testdir/subdir3/subsubdir1/b.c")
    print("Test case 1:", test_case_1)
    # Should print only the file: ['./testdir/subdir3/subsubdir1/b.c']

    test_case_2 = find_files(".c", "./testdir/subdir3/subsubdir1/b.h")
    print("Test case 2:", test_case_2)
    # Should print an empty list: []

    test_case_3 = find_files(".c", "./testdir")
    print("Test case 3:", test_case_3)
    # Expected: ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']

    test_case_4 = find_files(".c", "./testdir/subdir2")
    print("Test case 4:", test_case_4)
    # Expected: []

    test_case_5 = find_files("", "")
    print("Test case 5:", test_case_5)
    # Should print an empty list, since there is no dir with an empty path

    test_case_6 = find_files("", "./")
    print("Test case 6:", test_case_6)
    # Should print all files of current path (and subpaths)

    test_case_7 = find_files("", "./testdir")
    print("Test case 7:", test_case_7)
    # Should print all of testdir files
