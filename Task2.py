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

most_spent_time = None
for call in calls:
    if most_spent_time is None or int(call[3]) > int(most_spent_time[3]):
        most_spent_time = call

print("%s spent the longest time, %s seconds, on the phone during September 2016." %
      (most_spent_time[0], most_spent_time[3]))
