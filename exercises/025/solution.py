import datetime
ymd = datetime.datetime.now().date()
hms = datetime.datetime.now().strftime("%H:%M:%S")
print("Today is ", ymd, " and it is ", hms)
