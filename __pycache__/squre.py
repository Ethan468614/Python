user_input = int(input("Enter a number")) 

squared_value = user_input*user_input
print(f"the square value of {user_input} is {squared_value}")

if squared_value % 2 == 0:
    print(f"{squared_value} is even")
else:
    print(f"{squared_value} is odd")

    