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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def number_in_list_element(number, numbers_list, element):
    for n in numbers_list:
        if n[element] == number:
            return True
    return False


def number_in_list(number, numbers_list):
    for n in numbers_list:
        if n == number:
            return True
    return False


mkt_numbers = []

for call in calls:
    calling_number = call[0]

    if not number_in_list(calling_number, mkt_numbers):
        if not number_in_list_element(calling_number, calls, 1):  # check for call receiving numbers
            if not number_in_list_element(calling_number, texts, 0):  # check for text sending numbers
                if not number_in_list_element(calling_number, texts, 1):  # check for text receiving numbers
                    mkt_numbers.append(calling_number)

mkt_numbers.sort()
print("These numbers could be telemarketers:")
for number in mkt_numbers:
    print(number)
