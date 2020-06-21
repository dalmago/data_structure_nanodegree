"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Keep record of all numbers and its spent time
spent_time = {}

for call in calls:  # O(n)
    calling_number = call[0]
    receiving_number = call[1]

    # If the number is not in the dictionary yet, read the spent time as zero
    calling_sum = spent_time.get(calling_number, 0)  # O(n)
    receiving_sum = spent_time.get(receiving_number, 0)

    calling_sum += int(call[3])
    receiving_sum += int(call[3])

    spent_time[calling_number] = calling_sum  # O(n)
    spent_time[receiving_number] = receiving_sum

most_spent_time = None
for number, time in spent_time.items():  # O(n)
    if most_spent_time is None or time > most_spent_time[1]:
        most_spent_time = (number, time)

print("%s spent the longest time, %s seconds, on the phone during September 2016." %
      (most_spent_time[0], most_spent_time[1]))
