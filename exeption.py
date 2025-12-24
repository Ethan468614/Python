try:
    number = int(input("Enter an number: "))
    print("you entered:", number)

except ValueError as ex:
    print("exeption:", ex)
