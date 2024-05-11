import random
import time

def intro():
    print("May I ask you for your name?")
    name = input()  # asks for the name
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(0.5)
    print("Go ahead. Guess!")

def pick():
    number = random.randint(1, 200)  # pick the number between 1 and 200
    guesses_taken = 0
    while guesses_taken < 6:  # if the number of guesses is less than 6
        time.sleep(0.25)
        enter = input("Guess: ")  # inserts the place to enter guess
        try:  # check if a number was entered
            guess = int(enter)  # stores the guess as an integer instead of a string

            if 1 <= guess <= 200:  # if they are in range
                guesses_taken += 1  # adds one guess each time the player is wrong
                if guesses_taken < 6:
                    if guess < number:
                        print("The guess of the number that you have entered is too low")
                    elif guess > number:
                        print("The guess of the number that you have entered is too high")
                    else:
                        print("Good job, " + name + "! You guessed my number in " + str(guesses_taken) + " guesses!")
                        return
                    print("Try Again!")
                else:
                    break  # if the guess is right, then we are going to jump out of the while block
            else:  # if they aren't in the range
                print("Silly Goose! That number isn't in the range!")
                time.sleep(0.25)
                print("Please enter a number between 1 and 200")

        except ValueError:  # if a number wasn't entered
            print("I don't think that " + enter + " is a number. Sorry")

    print('Nope. The number I was thinking of was ' + str(number))

def play_game():
    play_again = "yes"
    while play_again.lower() in ["yes", "y"]:
        intro()
        pick()
        print("Do you want to play again? (yes/no)")
        play_again = input()

play_game()
