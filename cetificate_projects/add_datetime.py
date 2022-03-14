def add_time(start, duration, args=None):
    #function: add time
    #add_time("3:00 PM", "3:10")
    start = "11:40 AM"
    duration  = "0:25"
    args = None

    # initialize variables
    curhh = int(start.split(" ")[0].split(":")[0])
    curmm = int(start.split(" ")[0].split(":")[1])
    addhh = int(duration.split(":")[0])
    addmm = int(duration.split(":")[1])
    period = start.split(" ")[1]
    weekdaysname = {'monday': 0, 'tuesday': 1, 'friday': 4, 'wednesday': 2, 'thursday': 3, 'sunday': 6, 'saturday': 5}
    weekdayindex = {0: 'monday', 1: 'tuesday', 2: 'wednesday', 3: 'thursday', 4: 'friday', 5: 'saturday', 6: 'sunday'}

    # convert into minutes all
    if period == "PM":
        curhh = curhh + 12
    totalmin = (curhh * 60) + (addhh * 60) + addmm + curmm

    # calculate days to add
    totaldays = int(totalmin / 1440)
    if totaldays > 0:
        if totaldays == 1:
            endday = "(next day)"
        else:
            endday = "(" + str(totaldays) + " days later)"
    else:
        endday = str()

    #convert back to hours
    totalmin = totalmin - totaldays * 1440
    endhh = int((totalmin) / 60)
    endmm = int(totalmin % 60)
    if endhh >= 12:
        period = "PM"
        endhh = endhh - 12
    else:
        period = "AM"

    # adjust zero h
    if endhh == 0: endhh = 12 

    # adjust minutes
    if len(str(endmm)) < 2:
        strmin = "0" + str(endmm)
    else:
        strmin = str(endmm)

    # Adjust in case of week day namme
    if (args is not None):
        weekday = str(args).lower()
        totaldays = totaldays + weekdaysname[weekday]
        totaldays = totaldays % 7
        weekdayadd = weekdayindex[totaldays]
        weekdayadd = weekdayadd.capitalize()
        end_time = str(endhh) + ":" + strmin + " " + str(period) + ", " + weekdayadd + " " + endday
    else:
        end_time = str(endhh) + ":" + strmin + " " + str(period) + " " + endday
    end_time = end_time.rstrip()
    end_time = end_time.lstrip()
    return end_time

print(add_time("3:00 PM", "3:10","Sunday"))