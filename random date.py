import random
import time

def randomdate(startDate, endDate):
    print("printing random date between", startDate, "and", endDate)

    randomgen = random.random()
    dateformat = "%m/%d/%Y"

    startTime = time.mktime(time.strptime(startDate, dateformat))
    endTime = time.mktime(time.strptime(endDate, dateformat))

    randomtime = startTime + randomgen * (endTime - startTime)

    randomdate = time.strftime(dateformat, time.localtime(randomtime))

    time.localtime(randomtime)
    return randomdate

print("random date is:", randomdate("1/1/2020", "12/31/2023"))