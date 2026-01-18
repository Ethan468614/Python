
var = {'Codingal': 3, 'is': 2,'best': 2,'Coding': 1}

print(var)

user_input = input()

if user_input == "Codingal":
    print(var["Codingal"])
elif user_input == "is":
    print(var["is"])
elif user_input == "best":
    print(var["best"])
elif user_input == "Coding":
    print(var["Coding"])
else:
    print("Invalid input")
