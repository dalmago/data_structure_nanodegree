def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    """
    if len(string) == 0:
        return ['']

    last_char = string[-1]
    str_perm = permutations(string[:-1])

    new_list = []
    for i in range(len(str_perm)):
        substr = str_perm[i]

        for j in range(len(substr) + 1):
            new_list.append( substr[:j] + last_char + substr[j:] )

    return new_list

def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")

string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)

string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)
