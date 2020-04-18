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

# Easy level
if level == "e":
    answer = random.randint(1,10)
    life = 6
    while life > 0:
        print("You have", life, "guesses left. Please guess between 1 and 10")
        
        # check if input is an integer
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input, please enter a valid integer")
            continue
        life -= 1
        
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

# Medium level
if level == "m":
    answer = random.randint(1,20)
    life = 4
    while life > 0:
        print("You have", life, "guesses left. Please guess between 1 and 20")
        
        # check if input is an integer
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input, please enter a valid integer")
            continue
        life -= 1
        
        # check if guess is correct
        if guess == answer:
            print("Congratulations! You won the game!")
            break
        elif guess < answer:
            print("Your guess is too low")
            pass
        elif guess > answer:
            print("Your guess is too high")
            pass
        pass
    print("Game Over!")

# Hard level
if level == "h":
    answer = random.randint(1,50)
    life = 3
    while life > 0:
        print("You have", life, "guesses left. Please guess between 1 and 50")
        
        # check if input is an integer
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input, please enter a valid integer")
            continue
        life -= 1
        
        # check if guess is correct
        if guess == answer:
            print("Congratulations! You won the game!")
            break
        elif guess < answer:
            print("Your guess is too low")
            pass
        elif guess > answer:
            print("Your guess is too high")
            pass
        pass
    print("Game Over!")
