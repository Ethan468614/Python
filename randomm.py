import random 

playing = True

number = str(random.randint(10,20))

print("I will generate a random number between 10 to 20 and you have to guess "
"the number one digit at a time.")

print("The game ends when you get one hero")

while playing:
    guess = input("Enter your guess \n")
    if number == guess:
        print("you win")
        print(f"The number was {number}")
        break
    else:
        print("wrong guess, try again. \n")
        