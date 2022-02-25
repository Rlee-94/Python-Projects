#generate a random number from 1-10
from random import randint
answer = randint(1,10)


#Check that input is a number from 1-10
while True:
    try:
        user_guess = int(input("Guess a number from 1-10 and I'll tell you if you're right: "))
        if 0 < user_guess < 11:
            if user_guess == answer:
                print("You're a genius!")
                break
        else:
            print("Hey, I said a number from 1-10!") #If numbers outside of range, prompt again
    except ValueError: #If string is entered, prompt for number again.
        print('Please enter a number from 1-10')
        continue
