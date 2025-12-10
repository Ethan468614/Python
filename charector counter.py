s = (input("Please enter your word "))

char = (input("Please enter your charector "))

i = 0

c = 0 

while (i < len(s)):
    if (s [i] == char ):
        c= c +1
    i = i + 1

print("the total number of times" + char + " has occured = ", c)        