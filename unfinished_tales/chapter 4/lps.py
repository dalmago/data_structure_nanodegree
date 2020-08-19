import numpy as np

# Longest Palindrome Subsequence

def lps(input_string):
    # The function should return one value: the LPS length for the given input string

    strlen = len(input_string)

    lps_matrix = np.zeros((strlen, strlen))
    np.fill_diagonal(lps_matrix, 1)  # main diagonal

    for row in range(strlen - 2, -1, -1):
        for column in range(row + 1, strlen):
            if input_string[row] == input_string[column]:
                lps_matrix[row, column] = lps_matrix[row + 1, column - 1] + 2
            else:
                lps_matrix[row, column] = max(lps_matrix[row + 1, column], lps_matrix[row, column - 1])

    return lps_matrix[0, -1]


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


string = 'BxAoNxAoNxA'
solution = 5  # ANANA
test_case = [string, solution]
test_function(test_case)

string = 'BANANO'
solution = 3  # NAN
test_case = [string, solution]
test_function(test_case)

string = "TACOCAT"
solution = 7  # TACOCAT
test_case = [string, solution]
test_function(test_case)

string = "COOL"
solution = 2  # OO
test_case = [string, solution]
test_function(test_case)
