a = input("Enter the value of a: ")

if a.replace('.', '', 1).isdigit():
    num = float(a)
    if num < 0:
        print("Cannot compute square root of a negative number.")
    else:
        print("Square root:", num ** 0.5)
else:
    print("Please enter a valid number.")

    
