import random
print('Let\'s play the game!!')
choices = ["rock", "paper", "scissors"]

def user():
    for item in choices:
        print(f"{item}")
    user_input = input("Select between them: ").lower()
    while user_input not in choices:
        user_input = input("Invalid choice. Select between rock, paper, or scissors: ").lower()
    return user_input

def computer():
    computer_input = random.choice(choices)
    return computer_input
def play_game():
    user_input = user()
    computer_input = computer()
    #print(f"You chose: {user_input}")
    #print(f"Computer chose: {computer_input}")
    if user_input == computer_input:
        print("It's a tie!")
    elif (user_input == 'rock' and computer_input == 'scissors') or \
            (user_input == 'scissors' and computer_input == 'paper') or \
            (user_input == 'paper' and computer_input == 'rock'):
        print("You win!")
    else:
        print("Computer wins!")
while True:
 play_game()