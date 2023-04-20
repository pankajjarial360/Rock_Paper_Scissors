import random

def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors):  ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def check_win(player, computer):
    print(f"You chose {player}, Computer chose {computer}")
    if player == computer :
        return "oohhoo match tied!"
    elif player == "rock":
        if computer == "paper":
            return "paper cover the rock! You lose!"
        else:
            return "rock smashes the scissors! You Win!"            
    elif player == "paper":
        if computer == "scissors":
            return "scissors cut the paper! You lose!"
        else:
            return "paper cover the rock! You Win!"
    elif player == "scissors":
        if computer == "rock":
            return "rock smashes the scissors! You lose!"
        else:
            return "scissors cut the paper! You Win!"
        
choices = get_choices()

result = check_win(choices["player"], choices["computer"])

print(result)

