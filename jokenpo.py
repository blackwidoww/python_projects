import random

def play(): 
    # declares a function
    user = input("What's your choice? 'r' for rock, 'p; for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's']) # random.choice: choose randomly an item from a list
    
    if user == computer:
        return 'It\'s a tie!'
    # r > s, s > p, p > r
    if is_win (user, computer):
        return 'You won!'
    return 'You lost!'

def is_win(player, opponent):
    # return true if the player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())