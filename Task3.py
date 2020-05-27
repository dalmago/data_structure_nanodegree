"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def is_bangalore_prefix(prefix):
    return prefix == "080"


def get_prefix(number):
    if number[0] == '(':  # fixed lines
        idx = 1
        while number[idx] != ')':
            idx += 1
        return number[1:idx]

    if number[0] == '7' or number[0] == '8' or number[0] == '9':  # mobile
        return number[:4]

    # telemarketers
    return number[:3]


def number_in_list(number, numbers_list):
    for n in numbers_list:
        if n == number:
            return True
    return False


called_prefixes = []
count_from_bangalore = 0
count_to_bangalore = 0

for call in calls:
    calling_number = call[0]
    receiving_number = call[1]

    calling_prefix = get_prefix(calling_number)
    if is_bangalore_prefix(calling_prefix):  # O(1)
        count_from_bangalore += 1
        receiving_prefix = get_prefix(receiving_number)  # O(1)

        if is_bangalore_prefix(receiving_prefix):
            count_to_bangalore += 1

        if not number_in_list(receiving_prefix, called_prefixes):
            called_prefixes.append(receiving_prefix)  # append is O(1)

called_prefixes.sort()  # O(n log(n))
print("The numbers called by people in Bangalore have codes:")
for code in called_prefixes:  # O(n)
    print(code)

print("%.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore." %
      (count_to_bangalore * 100.0 / count_from_bangalore,))
