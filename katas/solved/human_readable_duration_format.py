# Solved!

def transfer_time(low_value, high_value, step):
    while low_value >= step:
        high_value += 1
        low_value -= step
    return low_value, high_value

def format_duration(seconds):
    if seconds == 0: return "now"

    years, days, hours, minutes = 0, 0, 0, 0
    seconds, minutes = transfer_time(seconds, minutes, 60)
    minutes, hours = transfer_time(minutes, hours, 60)
    hours, days = transfer_time(hours, days, 24)
    days, years = transfer_time(days, years, 365)

    words = [("year", "years"), ("day", "days"), ("hour", "hours"), ("minute", "minutes"), ("second", "seconds")]
    separators = [", ", " and "]
    time_lst = [years, days, hours, minutes, seconds]
    res_lst = []
    i = 0
    for x in time_lst:
        word_tuple = words[i]
        i += 1

        if x == 1:
            word = word_tuple[0]
        elif x > 1:
            word = word_tuple[1]
        else:
            continue

        res_lst.append(str(x) + " " + word)

    if len(res_lst) == 1:
        final_sep = ""
    else:
        final_sep = " and "
        
    return ", ".join(res_lst[0:len(res_lst)-1]) + final_sep + res_lst[len(res_lst)-1]


if __name__ == "__main__":
    print(format_duration(60))



