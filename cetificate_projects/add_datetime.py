def add_time(start, duration):
  new_time = str()
  mm = int(start.split(" ")[0].split(":")[1])
  hh = int(start.split(" ")[0].split(":")[0])
  period = start.split(" ")[1]
  addmm = int(duration.split(":")[1])
  addhh = int(duration.split(":")[0])

  #convert to 24h clock
  if period == "PM":
    hh = hh + 12

  #add the minutes
  if addmm + mm > 60:
    addhh = addhh + (addmm + mm)/60
    endmm = (addmm + mm)%60
  else: 
    endmm = addmm + mm

  #add the hours
  if addhh + hh >= 24:
    addday = (addhh + hh)/24
    endhh = (addhh + hh)%24
  else:
    endhh = addhh + hh

  #convert to 12h clock
  if endhh >= 12:
    endhh = endhh - 12
    period = "PM"
  else:
    period = "AM"

  #adjust string new time
  if len(str(endmm)<2:
    finalmm = str("0" + str(endmm))
  else:
    finalmm = str(endmm)

  new_time = str(endhh) + ":" + finalmm + " " + period

  return new_time

print(add_time("12:55 AM", "3:12"))