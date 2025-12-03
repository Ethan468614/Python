medical_cause = input("Do you have a medical cause y/n: ")

attendence = int(input("Enter your attendence of the student: "))

if medical_cause == 'y':
    print("Student is allowed to sit in exam")
else:
    if attendence >=75:
        print('you are allowed')
    else:
        print("you are not allowed")           