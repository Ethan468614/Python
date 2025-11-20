Amount = int(input("Please enter the amount for withdrawel: "))
note1 = Amount//100
note2 = (Amount%100)//50
note3 = ((Amount%100)%50)//10

print("notes of 100 rs: ", note1)
print("notes of 50 rs: ", note2)
print("ntes of 10 rs: ", note3)