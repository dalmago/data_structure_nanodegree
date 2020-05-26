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


def get_year(timestamp):
    return int(timestamp[6:10])


def get_month(timestamp):
    return int(timestamp[3:5])


def get_day(timestamp):
    return int(timestamp[0:2])


def get_hour(timestamp):
    return int(timestamp[11:13])


def get_minute(timestamp):
    return int(timestamp[14:16])


def get_second(timestamp):
    return int(timestamp[17:19])


def is_before(timestamp1, timestamp2):
    # Check if timestamp1 comes before timestamp2
    year1 = get_year(timestamp1)
    year2 = get_year(timestamp2)

    if year1 < year2:
        return True

    if year1 == year2:
        month1 = get_month(timestamp1)
        month2 = get_month(timestamp2)

        if month1 < month2:
            return True

        if month1 == month2:
            day1 = get_day(timestamp1)
            day2 = get_day(timestamp2)

            if day1 < day2:
                return True

            if day1 == day2:
                hour1 = get_hour(timestamp1)
                hour2 = get_hour(timestamp2)

                if hour1 < hour2:
                    return True

                if hour1 == hour2:
                    minute1 = get_minute(timestamp1)
                    minute2 = get_minute(timestamp2)

                    if minute1 < minute2:
                        return True

                    if minute1 == minute2:
                        if get_second(timestamp1) < get_second(timestamp2):
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
