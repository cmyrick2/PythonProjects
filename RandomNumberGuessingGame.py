import random

playAgain = True
while playAgain:
    flag = True
    while flag:
        num = input('Type a number for an upper bound: \n')

        if num.isdigit():
            print("Let's play!")
            num = int(num)
            flag = False
        else:
            print("Invalid Input! Try Again!")

    secret = random.randint(1, num)

    guess = None
    count = 1

    while guess != secret:
        guess = input("Please type a number between 1 and " + str(num) + ": \n")
        if guess.isdigit():
            guess = int(guess)
        
        if guess == secret:
            print("You got it!")
        else:
            print("Please try again!")
            count += 1

    print("It took you", count, "guesses!")
    playAgainInput = input("Do you want to play again? Input Y for yes and N for no: \n")
    if playAgainInput != "Y":
        playAgain = False