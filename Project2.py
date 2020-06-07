# Project2 - Bulls and Cows

# Define basic variables
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
Hello_user = '''
Hi there !
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
Enter a number'''
import random

# Define main function
def main():
    print(Hello_user)
    rand_number = list(map(int, random.sample(nums, 4)))
    guess_counter = 0
    user_review = ""
    while True:
        user_guess = user_input(rand_number)
        bulls, cows = bulls_and_cows(user_guess, rand_number)
        print(f" {bulls} Bulls, {cows} Cows")
        guess_counter = guess_counter + 1
        if bulls == 4:
            if guess_counter < 2:
                user_review = "Amazing"
            elif guess_counter < 10:
                user_review = "Average"
            else: user_revies = "Not so good"
            print(f"Correct, you've guessed the right number in {guess_counter} guesses! \nThats {user_review}")
            break

# Function which takes user input and check the formatting, if it is ok, then it return the user input
def user_input(rand_number):
    guess_list = []
    while True:
        guess_num = input(" -> ")
        try:
            if len(str(guess_num)) == 4:
                for i in str(guess_num):
                    guess_list.append(int(i))
                return guess_list
            else:
                print("zadejte prosim 4 cislice")
        except ValueError:
            print("Spatny format cisla")

# function which takes, random number and user input and return the number of 'bulls' and 'cows' for the round
def bulls_and_cows(guess_num, rand_num):
    bulls = 0
    cows = 0
    for i, x in enumerate((rand_num)):
        for j, y in enumerate((guess_num)):
            if i == j and x == y:
                bulls = bulls + 1
            elif y == x and not j == i:
                cows = cows + 1
    return bulls, cows

main()
