import random

def number_guessing_game():
    print('WELCOME to the Number Guessing Game (Enter 0 to stop the game)')
    target_number = random.randint(1, 100) 
    attempts = 0

    try:
        while True:
            user_quess = int(input('Guess the number (1-100):'))
            attempts += 1

            if user_quess == 0:
                print('Goodbye. :(')
                break
            elif user_quess == target_number:
                print(f'Congratulation! You guessed the correct number, its {target_number} in {attempts} attempts :)')
                break
            elif user_quess < 1:
                print('Error 1: Please enter a valid number (1-100).')
            elif user_quess >100:
                print('Error 2: Please enter a valid number (1-100).')
            elif user_quess < target_number:
                print('To low, try again.')
            else:
                print('To high, try again.')
                
    except ValueError:
        print('Error 3: Please enter a valid number (1-100).')


number_guessing_game()