import random


def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"Player chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors!!, You win!"
        else:
            return "paper covers rocks!!, You Lose"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rocks!!, You win!"
        else:
            return "Scissors cut paper!!, You Lose"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut paper!!, You win!"
        else:
            return "Paper covers rocks!!, You Lose"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
