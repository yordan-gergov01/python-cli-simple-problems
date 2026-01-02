import random

random_number = random.randint(1, 1000)

while True:
    guess = input('Guess the number between 1 and 1000: ')
    
    try:
        guess = int(guess)
    
        if isinstance(guess, int):
            if guess < random_number:
                print('Too low!')
            elif guess > random_number:
                print('Too high!')
            else:
                print('Congratulations! You guessed the number.')
                break
    except:    
        print('Please enter a valid number')