# Project2 - Bulls and Cows
# Popis: 2. projekt 'Bulls and cows' v Engeto Online Python Akademii
# Autor: Jiri Gloza

# Define basic variables
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
Welcome_message = '''
Hi there !
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
Enter a number'''
import random


# Define main function and generating random number.
# While cycle checks for user inputs and compare with random number using function user input
# Function Bulls_and_cows checks the position of numbers and return number of bulls and cows for each guess
def main():
    print(Welcome_message)
    rand_number = list(map(int, random.sample(nums, 4)))
    guess_counter = 0
    user_word_score = ""
    while True:
        user_guess = user_input(rand_number)
        bulls, cows = bulls_and_cows(user_guess, rand_number)
        print(f" {bulls} Bulls, {cows} Cows")
        guess_counter = guess_counter + 1
        if bulls == 4:
            if guess_counter < 2:
                user_word_score = "Amazing"
            elif guess_counter < 10:
                user_word_score = "Average"
            else:
                user_word_score = "Not so good"
            print(f"Correct, you've guessed the right number in {guess_counter} guesses! \nThats {user_word_score}")
            break


# Function which takes user input and check the formatting, if it is ok, then it return the user input back to main()
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
                print("Please enter 4 digits only")
        except ValueError:
            print("Bad formatting -> only digits are allowed")


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
