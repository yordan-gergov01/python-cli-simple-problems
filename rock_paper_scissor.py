import random

game_elements = ('r', 'p', 's')
wins = {'r': 's', 'p': 'r', 's': 'p'}
emojis = {
    'r': '🪨',
    'p': '📄',
    's': '✂️'
}

while True:
    user_choice = input("Rock, paper, or scissors? (r/p/s): ").strip().casefold()
    
    if user_choice not in game_elements:
        print('Invalid choice!')
        continue
    
    computer_choice = random.choice(game_elements)
    
    print(f"You chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif wins[user_choice] == computer_choice:
        print("You win! 🎉")
    else:
        print("Computer wins! 🤖")
    
    print()
    
    if input("Play again? (y/n): ").lower() != 'y':
        print("Goodbye! 👋")
        break