import random

# Game info
print("This is a number guessing game with three(3) difficulty levels")
print("--------------------------------")
print("Easy level: Guess between 1-10 and you have only six(6) guesses")
print("Medium level: Guess between 1-20 and you have only four(4) guesses")
print("Hard level: Guess between 1-50 and you have only three(3) guesses")
print("--------------------------------")
print("For Easy, please enter 'e'")
print("For Medium, please enter 'm'")
print("For Hard, please enter 'h'")
print("--------------------------------")

# Select preferred game level and convert to lowercase
level = input("Please enter your difficulty level: ").lower()


# Define game function to be used for each difficulty level
def game(guesses_left, answer):
    while guesses_left > 0:
        print("You have", guesses_left, "guesses left.")
        
        # check if input is an integer
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input, please enter a valid integer")
            continue
        guesses_left -= 1
        
        # check if guess is correct
        if guess == answer:
            print("Congratulations! You won the game!")
            break
        elif guess < answer:
            print("Your guess is too low,")
            pass
        elif guess > answer:
            print("Your guess is too high")
            pass
        pass
    print("Game Over!")
    return guesses_left, answer


# Easy level, available guesses = 6 and answer is between 1 to 10
if level == "e":
    print("Please guess between 1 and 10")
    game(6, random.randint(1,10))


# Medium level, available guesses = 4 and answer is between 1 to 20
if level == "m":
    print("Please guess between 1 and 20")
    game(4, random.randint(1,20))


# Hard level, available guesses = 3 and answer is between 1 to 50
if level == "h":
    print("Please guess between 1 and 50")
    game(3, random.randint(1,50))
