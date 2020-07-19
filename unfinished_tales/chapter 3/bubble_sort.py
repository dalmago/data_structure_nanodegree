
wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]


def bubble_sort_1(l):
    for bubble_up in range(len(l) - 1, 1, -1):  # count down from len - 1 to 2
        for idx in range(bubble_up):  # count up len - 1 - bubble_up elements
            if l[idx] > l[idx + 1]:
                l[idx + 1], l[idx] = l[idx], l[idx + 1]


bubble_sort_1(wakeup_times)
print ("Pass" if (wakeup_times[0] == 3) else "Fail")


# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]

def bubble_sort_2(l):
    def time_is_earlier(time1, time2):
        if time1[0] < time2[0]:
            return True

        elif time1[0] == time2[0]:
            if time1[1] < time2[1]:
                return True

        return False

    for bubble_up in range(len(l) - 1, 1, -1):  # count down from len - 1 to 2
        for idx in range(bubble_up):  # count up len - 1 - bubble_up elements

            if time_is_earlier(l[idx], l[idx + 1]):
                l[idx + 1], l[idx] = l[idx], l[idx + 1]

bubble_sort_2(sleep_times)
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")
