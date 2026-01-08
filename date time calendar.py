from datetime import date, time, datetime

taday = date.today()
now = datetime.now()

print("Today's dateis :", taday)
print("current date and time is :", now)

print("Date components:", taday.year, taday.month, taday.day )