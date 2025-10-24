import random

def computer_guess(x): # declarates function
    low = 1 # lower number
    high = x # highest number
    feedback = ''
    while feedback != 'c': # loop # c: correct number 
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct(C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low == guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!') # ends the program after guessing the right number

computer_guess(10) # the hidden number is between 1 and 10