import random

#set variables to track score and choice list.
user_score = 0
comp_score = 0
ties = 0
choices = ['r','p','s']

#Program will run until user or comp reach 5 wins.

    user = input("Enter (r), (p), or (s):  ") 
    comp = random.choice(choices) 

    #Outcome of choices
    if user == 'r' and comp == 'r':
        print("You both chose rock, its a tie!")
        ties += 1
    if user == 'r' and comp == 's':
        print("You chose rock and the computer chose scissors, you win!")
        user_score += 1
    if user == 'r' and comp == 'p':
        print("You chose rock and the computer chose paper, the computer wins!")
        comp_score += 1
    if user == 'p' and comp == 'p':
        print("You both chose paper, its a tie!")
        ties += 1
    if user == 'p' and comp == 'r':
        print("You chose paper and the computer chose rock, you win!")
        user_score += 1
    if user == 'p' and comp == 's':
        print("You chose paper and the computer chose scissors, the computer win!")
        comp_score += 1
    if user == 's' and comp == 's':
        print("You both chose scissors, its a tie!")
        ties += 1 
    if user == 's' and comp == 'p':
        print("You chose scissors and the computer chose rock, you win!")
        user_score += 1
    if user == 's' and comp == 'r':
        print("You chose scissors and the computer chose paper, the computer wins!")
        comp_score += 1
    
    #Display current number of wins/ties between user and comp
    print(f"User score: {user_score}")
    print(f"Computer score: {comp_score}")
    print(f"Ties: {ties}")
    
