# Starting file for LAB 4
# Include your course number, student first and last name, and date in the comment header

# Sammy Browning
# October 21 2026
# Course Number 72473

import random

# print the title of the program
def display_title():
    print("Guess that Number Game")
    print()

def play_game():
    # ask the player which difficulty they want to play
    print(
        """
        E: Easy - Guess from 1 - 10, limit 5 attempts
        M: Medium - Guess from 1 - 100, limit 7 attempts
        H: Hard - Guess from 1 - 1000, limit 10 attempts
        """)
    your_level = input("Which level would you like to play: E, M, or H?   ")
    # set the limit based on their game level choice
    if your_level.upper() == "E":
        limit = 10
        attempts = 5
    elif your_level.upper() == "M":
        limit = 100
        attempts = 7
    elif your_level.upper() == "H":
        limit = 1000
        attempts = 10
    else:
        limit = 10000   # punish them if they don't enter proper input
        attempts = 3
  
    secret_number = random.randint(1, limit)    # sets the random int parameters between the numbers of 1 and 10 which is the LIMIT
    print(f"I am thinking of a number from 1 and {limit}\n")    # ASK WHY WE USE f AT THE BEGINNING AND n AT THE END
    count = 1   # keep track of the number of total attempts
        
    while (guess := int(input("Your guess: "))) != secret_number:     # This := is called a Walrus while != means does not equal
        if count >= attempts:
            print("Sorry, you ran out of attempts!")
            break
        # the guess is incorrect
        if guess < secret_number:
            print("Sorry, your guess is too low.")
        elif guess > secret_number:
            print("Sorry, your guess is too high.")
        count += 1      # increment the guess attempt counter
    else:   # if they guessed correctly
        print(f"Congrats! You guessed it in {count} tries!\n")

    # if the guess is correct
    # print(f"Congrats! You guessed it in {count} tries!\n")

def main():     # The main function drive the entire program
    display_title()

    # ask for the players name
    # because we may recall their name later, this is why it is best left in the main() function
    player_name = input("Hi! What's your name?"   )
    print()

    again = "y"     # set initial game loop variable

    while again.lower() == "y":     # play the game
        play_game()
        again = input(f"Would you like to play another game, {player_name}? y/n:   ")
        print()

    print(f"Thanks for playing, {player_name}! Bye!")

# if this is started as the main module, call the main() function
if __name__ == "__main__":
    main()