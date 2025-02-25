import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It is a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = input("Enter rock, paper, scissors (or 'quit' to stop): ").lower()
        if user_choice == 'quit':
            print("Final Scores - You:", user_score, "Computer:", computer_score)
            break
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, try again!")
            continue

        computer_choice = get_computer_choice()
        print("Computer chose:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

if __name__ == "__main__":
    play_game()
