import sys
import random
start = int(sys.argv[1])
end = int(sys.argv[2])
answer = random.randint(start, end)
while True:
    try:
        user_guess = int(input(f'Guess a number between {start} and {end}: '))
        if user_guess == answer:
            print(f"Bravo! It was indeed {answer}")
            break
        elif user_guess < start or user_guess > end:
            print(f'Your number is not between {start} and {end}! Try again')
        else:
            print("Nope, try to guess again")
    except ValueError:
        print("Please enter a number")
