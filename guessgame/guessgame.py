import random

randint = random.randint(1, 100)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
print("\n\nPlease select the difficulty level:\n1.Easy (10 chances)\n2.Medium (5 chances)\n3.Hard (3 chances)\n")
choice = int(input("Enter your choice:"))
if choice == 1:
    chances = 10
    mode = 'Easy'
elif choice == 2:
    chances = 5
    mode = 'Medium'
elif choice == 3:
    chances = 3
    mode = 'Hard'

print(f"\n\nGreat! You have selected the {mode} level.\nLet's start the game!")

times = 1
while(chances != 0):
    guess = int(input("Enter your guess:"))

    if(guess == randint):
        print(f"Congratulations! You guessed the correct number in {times} attempts.")
        break
    elif(guess < randint):
        print(f"Incorrect! The number is greater than {guess}.")
    else:
        print(f"Incorrect! The number is less than {guess}.")
    
    if chances == 0:
        print("Sorry! you lose this time. try more after")

    chances -= 1
    times += 1


