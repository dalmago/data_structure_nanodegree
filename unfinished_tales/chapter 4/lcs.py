# Longest Common Subsequence

import numpy as np

def lcs(string_a, string_b):
    len1 = len(string_a)
    len2 = len(string_b)

    lcs_matrix = np.zeros((len1 + 1, len2 + 1))

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if string_a[i - 1] == string_b[j - 1]:
                lcs_matrix[i, j] = lcs_matrix[i-1, j-1] + 1
            else:
                lcs_matrix[i, j] = max(lcs_matrix[i-1, j], lcs_matrix[i, j-1])

    return lcs_matrix[-1, -1]


test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"

lcs_val1 = lcs(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"

lcs_val2 = lcs(test_A2, test_B2)

print('LCS val 1 = ', lcs_val1)
assert lcs_val1 == 5, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)
assert lcs_val2 == 7, "Incorrect LCS value."
print('Tests passed!')
