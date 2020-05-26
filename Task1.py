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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def number_in_list(number, numbers_list):
    for n in numbers_list:
        if n == number:
            return True

    return False


# Starting as zero since the files could be empty
counter = 0
unique_numbers = []

for text in texts:
    sending_number = text[0]
    receiving_number = text[1]

    if not number_in_list(sending_number, unique_numbers):
        unique_numbers.append(sending_number)  # append is O(1)
        counter += 1

    if not number_in_list(receiving_number, unique_numbers):
        unique_numbers.append(receiving_number)
        counter += 1

for call in calls:
    calling_number = call[0]
    receiving_number = call[1]

    if not number_in_list(calling_number, unique_numbers):
        unique_numbers.append(calling_number)
        counter += 1

    if not number_in_list(receiving_number, unique_numbers):
        unique_numbers.append(receiving_number)
        counter += 1

print("There are %s different telephone numbers in the records." % counter)
