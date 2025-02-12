import random

def play():
    user = input("What is your choose.\n'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r','p','s'])

    # if the computer and user both are same
    if user == computer:
        return 'Tie'

    if is_win(user, computer):
        return 'You Won!'

    return 'You Lost!'

def is_win(player, opponent):
    # it will return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())