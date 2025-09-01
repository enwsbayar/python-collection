# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

# It is much easier to understand with an example:

# * For seconds = 62, your function should return 
#     "1 minute and 2 seconds"
# * For seconds = 3662, your function should return
#     "1 hour, 1 minute and 2 seconds"
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.

# Note that spaces are important.

# Detailed rules
# The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

# The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

# A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

# Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

# A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

# A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

#https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

def formatDuration(seconds):

  result = ""
  total = 0

#calculate seconds, minutes, hours, days, years.-----------<
  minutes = hours = days = years = 0 

  if seconds % 60 >= 0:                   
    minutes = seconds // 60
    seconds %= 60
  
  if minutes % 60 >= 0:
    hours = minutes // 60   
    minutes %= 60
                                                      
  if hours % 24 >= 0:
    days = hours // 24
    hours %= 24

  if days % 365 >= 0:
    years = days // 365
    days %= 365
#now-----------------------------------------------------<
  if years == 0 and days == 0 and hours == 0 and minutes == 0 and seconds == 0:
    return "now"
#--------------------------------------------------------<

#Find the elements that are bigger than 0.---------------<
  checkSeconds = checkMinutes = checkHours = checkDays = checkYears = False 

  if seconds > 0:
    checkSeconds = True
    total += 1
  if minutes > 0:
    checkMinutes = True
    total += 1
  if hours > 0:
    checkHours = True
    total += 1
  if days > 0:
    checkDays = True
    total += 1
  if years > 0:
    checkYears = True
    total += 1

#--------------------------------------------------------<

#If there is only one element:---------------------------<
  if checkSeconds == True and checkMinutes == False and checkHours == False and checkDays == False and checkYears == False:
    if seconds > 1:
      return "{} seconds".format(seconds)
    elif seconds == 1:
      return "{} second".format(seconds)
  
  if checkSeconds == False and checkMinutes == True and checkHours == False and checkDays == False and checkYears == False:
    if minutes > 1:
      return "{} minutes".format(minutes)
    elif minutes == 1:
      return "{} minute".format(minutes)
    
  if checkSeconds == False and checkMinutes == False and checkHours == True and checkDays == False and checkYears == False:
    if hours > 1:
      return "{} hours".format(hours)
    elif hours == 1:
      return "{} hour".format(hours)
    
  if checkSeconds == False and checkMinutes == False and checkHours == False and checkDays == True and checkYears == False:
    if days > 1:
      return "{} days".format(days)
    elif days == 1:
      return "{} day".format(days)
  
  if checkSeconds == False and checkMinutes == False and checkHours == False and checkDays == False and checkYears == True:
    if years > 1:
      return "{} years".format(years)
    elif years == 1:
      return "{} year".format(years)
#--------------------------------------------------------<

#Find the first and last element.------------------------<
  secondsFirstCheck = minutesFirstCheck = hoursFirstCheck = daysFirstCheck = yearsFirstCheck = False

  if years > 0:
    yearsFirstCheck = True
  elif days > 0:
    daysFirstCheck = True
  elif hours > 0:
    hoursFirstCheck = True
  elif minutes > 0:
    minutesFirstCheck = True
  elif seconds > 0:
    secondsFirstCheck = True

  secondsLastCheck = minutesLastCheck = hoursLastCheck = daysLastCheck = yearsLastCheck = False

  if seconds > 0:
    secondsLastCheck = True
  elif minutes > 0:
    minutesLastCheck = True
  elif hours > 0:
    hoursLastCheck = True
  elif days > 0:
    daysLastCheck = True
  elif years > 0:
    yearsLastCheck = True

#--------------------------------------------------------<

#return part---------------------------------------------<

#first part----------------------------------------------<
  if yearsFirstCheck == True:
    if years > 1:
      if total > 2:
        result += "{} years, ".format(years)
        total -= 1
      else:
        result += "{} years ".format(years)
    elif years == 1:
      if total > 2:
        result += "{} year, ".format(years)
        total -= 1
      else:
        result += "{} year ".format(years)
    
  elif daysFirstCheck == True:
    if days > 1:
      if total > 2:
        result += "{} days, ".format(days)
        total -= 1
      else:
        result += "{} days ".format(days)
    elif days == 1:
      if total > 2:
        result += "{} day, ".format(days)
        total -= 1
      else:
        result += "{} day ".format(days)

  elif hoursFirstCheck == True:
    if hours > 1:
      if total > 2:
        result += "{} hours, ".format(hours)
        total -= 1
      else:
        result += "{} hours ".format(hours)
    elif hours == 1:
      if total > 2:
        result += "{} hour, ".format(hours)
        total -= 1
      else:
        result += "{} hour ".format(hours)
  
  elif minutesFirstCheck == True:
    if minutes > 1:
      result += "{} minutes ".format(minutes)
    elif minutes == 1:
      result += "{} minute ".format(minutes)
  
  elif secondsFirstCheck == True: #it's impossible but it doesn't hurt to try.
    if seconds > 1:
      result += "{} seconds ".format(seconds)
    elif seconds == 1:
      result += "{} second ".format(seconds)
#second part---------------------------------------------<
  if yearsFirstCheck == False and yearsLastCheck == False:
    if years > 1:
      result += "{} years, ".format(years)
    elif years == 1:
      result += "{} year, ".format(years)

  if daysFirstCheck == False and daysLastCheck == False:
    if days > 1:
      if total > 2:
        result += "{} days, ".format(days)
        total -= 1
      else:
        result += "{} days ".format(days)
    elif days == 1:
      if total > 2:
        result += "{} day, ".format(days)
      else:
        result += "{} day ".format(days)

  if hoursFirstCheck == False and hoursLastCheck == False:
    if hours > 1:
      if total > 2:
        result += "{} hours, ".format(hours)
        total -= 1
      else:
        result += "{} hours ".format(hours)
    elif hours == 1:
      if total > 2:
        result += "{} hour, ".format(hours)
      else:
        result += "{} hour ".format(hours)

  if minutesFirstCheck == False and minutesLastCheck == False:
    if minutes > 1:
      result += "{} minutes ".format(minutes)
    elif minutes == 1:
      result += "{} minute ".format(minutes)
  
  if secondsFirstCheck == False and secondsLastCheck == False:
    if seconds > 1:
      result += "{} seconds ".format(seconds)
    elif seconds == 1:
      result += "{} second ".format(seconds)
#third part----------------------------------------------<
  if yearsLastCheck == True:
    if years > 1:
      result += "and {} years".format(years)
    elif years == 1:
      result += "and {} year".format(years)
    
  elif daysLastCheck == True:
    if days > 1:
      result += "and {} days".format(days)
    elif days == 1:
      result += "and {} day".format(days)

  elif hoursLastCheck == True:
    if hours > 1:
      result += "and {} hours".format(hours)
    elif days == 1:
      result += "and {} hour".format(hours)
  
  elif minutesLastCheck == True:
    if minutes > 1:
      result += "and {} minutes".format(minutes)
    elif minutes == 1:
      result %= "and {} minute".format(minutes)
  
  elif secondsLastCheck == True: #it's impossible but it doesn't hurt to try.
    if seconds > 1:
      result += "and {} seconds".format(seconds)
    elif seconds == 1:
      result += "and {} second".format(seconds)

  return result

print(formatDuration(3662))


    