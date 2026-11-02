import random

# tells game if they have won
def check_guess(guess, secret):
    if guess > secret:
        print("Too high!")
        return False
    elif guess < secret:
        print("Too low!")
        return False
    else:
        print("Correct! You got it.")
        return True

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Lets see if you can guess it!")
    
    # variables
    secret_number = random.randint(1, 100)
    attempts = 0
    game_over = False
    
    # The main game loop
    while not game_over:
        user_input = input("Enter your guess: ")
        
        # checking if its an actual number
        if not user_input.isdigit():
            print("Please enter a valid number!")
            continue
            
        guess = int(user_input)
        attempts = attempts + 1
        
        #  will print high/low/correct 
        game_over = check_guess(guess, secret_number)
        
    print(f"Congrats! It took you {attempts} attempts.")

#start the game
play_game()