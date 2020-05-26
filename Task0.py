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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def is_before(timestamp1, timestamp2):
    year1 = int(timestamp1[6:10])
    year2 = int(timestamp2[6:10])

    if year1 < year2:
        return True

    if year2 == year1:
        month1 = int(timestamp1[3:5])
        month2 = int(timestamp2[3:5])

        if month1 < month2:
            return True

        if month1 == month2:
            day1 = int(timestamp1[0:2])
            day2 = int(timestamp2[0:2])

            if day1 < day2:
                return True

            if day1 == day2:
                hour1 = int(timestamp1[11:13])
                hour2 = int(timestamp2[11:13])

                if hour1 < hour2:
                    return True

                if hour1 == hour2:
                    minute1 = int(timestamp1[14:16])
                    minute2 = int(timestamp2[14:16])

                    if minute1 < minute2:
                        return True

                    if minute1 == minute2:
                        second1 = int(timestamp1[17:19])
                        second2 = int(timestamp2[17:19])

                        if second1 < second2:
                            return True
    return False


first_text = None
last_call = None

for text in texts:
    if first_text is None or is_before(text[2], first_text[2]):
        first_text = text

for call in calls:
    if last_call is None or is_before(last_call[2], call[2]):
        last_call = call

print("First record of texts, %s texts %s at time %s" % (first_text[0], first_text[1], first_text[2]))
print("Last record of calls, %s calls %s at time %s, lasting %s seconds" % (last_call[0], last_call[1], last_call[2],
                                                                            last_call[3]))
