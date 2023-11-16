import random

options = ("rock","paper","scissors")
player_options = ("r","p","s","rock","paper","scissors")
runing = True


while runing:
    player = None
    computer = random.choice(options)
    while player not in player_options:
        player = input("Enter a choice (rock(r), paper(p), scissors(s)): ")

    if(player == "r"):
        player = "rock"
    elif(player == "p"):
        player = "paper"
    elif(player == "s"):
        player = "scissors"
    
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    
    if(player == computer):
        print("Tie!")
    elif(player == "rock" and computer == "paper"):
        print("Lose!")
    elif(player == "paper" and computer == "scissors"):
        print("Lose!")
    elif(player == "scissors" and computer == "rock"):
        print("Lose!")
    else:
        runing = False
        print("Win!")
