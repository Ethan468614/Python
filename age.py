#check the user input
#use type(()) to check the type of input
#and check if the user entered integer or not
#if user enters an integer value 
#Then check if the age is odd or even
#Also use while loop to keep asking until user enters valid input


user_input = input("Please enter your age: ")

if type(user_input) is not int or not user_input.float():
    raise ValueError("Invalid input: Please enter a valid integer for age.")

else:
    if user_input % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")   


