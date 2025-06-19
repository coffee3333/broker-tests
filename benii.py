import random

def rock_paper_scissors():
    options = ['rock', 'paper', 'scissors']
    print("🎮 Rock, Paper, Scissors Game!")
    
    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'q' to quit): ").lower()
        if user_choice == 'q':
            print("👋 Thanks for playing!")
            break
        if user_choice not in options:
            print("❌ Invalid choice.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose {computer_choice}.")

        if user_choice == computer_choice:
            print("🤝 It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("✅ You win!")
        else:
            print("💻 Computer wins!")

if __name__ == "__main__":
    rock_paper_scissors()
