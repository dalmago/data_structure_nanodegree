def longest_consecutive_subsequence(input_list):
    visited = {}

    smallest = None
    for elem in input_list:
        if smallest is None:
            smallest = elem

        visited[elem] = {"smallest": elem, "count": 1}

        if elem - 1 in visited:
            # increment counts
            visited[elem - 1]['count'] += 1
            visited[elem]['count'] = visited[elem - 1]['count']

            visited[elem]['smallest'] = visited[elem - 1]['smallest']
            visited[visited[elem]['smallest']]['count'] = visited[elem]['count']

        if elem + 1 in visited:
            # increment counts
            visited[elem + 1]['count'] += visited[elem]['count']
            visited[elem]['count'] = visited[elem + 1]['count']

            visited[elem + 1]['smallest'] = visited[elem]['smallest']
            visited[visited[elem]['smallest']]['count'] = visited[elem]['count']

        if visited[elem]['count'] > visited[smallest]['count']:
            smallest = elem

        elif visited[elem]['count'] == visited[smallest]['count']:
            if visited[elem]['smallest'] < smallest:
                smallest = visited[elem]['smallest']

    return list(range(smallest, smallest + visited[smallest]['count']))


def test_function(test_case):
    output = longest_consecutive_subsequence(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")

test_case_1 = [[5, 4, 55, 1, 10, 3, 2], [1, 2, 3, 4, 5]]
test_function(test_case_1)

test_case_2 = [[2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6 ], [8, 9, 10, 11, 12]]
test_function(test_case_2)

test_case_3 = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
test_function(test_case_3)
