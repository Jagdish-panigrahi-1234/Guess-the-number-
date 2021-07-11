import random
randNumber = random.randint(1, 100)
userGuess = None
gusses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    gusses += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

print(f"You guessed the number in {gusses} guesses")
