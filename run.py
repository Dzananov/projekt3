import random
user=input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer = random.choice(possible_actions)
print(f"You chose {user}, computer chose {computer}.")
if user == computer:
    print(f"Both selected {user}. It's a tie!")
elif user == "paper":
    if computer == "rock":
        print("paper covers rock! You win!")
    else:
        print("scissors cut paper! You lose.")
elif user == "scissors":
    if computer == "paper":
        print("scissor cut paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
elif user == "rock":
    if computer == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("paper covers rock! You lose.")