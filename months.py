import calendar

user = int(input("Enter month number (1-12): "))

if 1 <= user <= 12:
    print(f"The name of the month for month number {user} is {calendar.month_name[user]}")
else:
    print("Invalid month number")