import random

def guess(x):
    random_number = random.randint(1, x) # random.randint(a,b): Return an int random number N such that a <= N <=b.
   # Once the Computer has a random number, we need to guess in Terminal and input what our guess is
   # The computer will tell us whether it's too high, too low, or if we guessed the number correctly\
   # we need to keep *looping* until we get the right answer
    
    guess = 0
    while guess != random_number: 
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    
    print(f"Yay! Congrats! Right number! {random_number}")

guess(10)