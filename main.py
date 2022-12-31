import random

# create board dictionary
board = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}

# set player who goes first random
xo = ['X', 'O']
player = random.choice(xo)

# set game to on/True
game_on = True


def make_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def game(player):

    print(f"It's your turn player {player}.")
    move = input("Where will you move? ")

#check move
    if board[move] == ' ':
        # update dictionary
        board.update({move: player})
    else:
        print("Not a valid space, try again. ")
        move = input("Where will you move? ")
        board.update({move: player})

    #print board after moving
    make_board(board)
    # check for a winner or tie
    check_winner(player)
    is_board_full(board)


def check_winner(player):
    if board['1'] == board['2'] == board['3'] and board['3'] != ' ':  # across the top
        make_board(board)
        print("\nGame Over.\n")
        print(" **** " + player + " won! ****")
        play_again()
    elif board['4'] == board['5'] == board['6'] and board['4'] != ' ':  # across the middle
        make_board(board)
        print("\nGame Over.\n")
        print(" **** " + player + " won! ****")
        play_again()
    elif board['7'] == board['8'] == board['9'] != ' ':  # across the bottom
        make_board(board)
        print("\nGame Over.\n")
        print(" **** " + player + " won. ****")
        play_again()
    elif board['1'] == board['4'] == board['7'] != ' ':  # down the left side
        make_board(board)
        print("\nGame Over.\n")
        print(" **** " + player + " won! ****")
        play_again()
    elif board['2'] == board['5'] == board['8'] != ' ':  # down the middle
        make_board(board)
        print("\nGame Over.\n")
        print(" **** " + player + " won. ****")
        play_again()
    elif board['3'] == board['6'] == board['9'] != ' ':  # down the right side
        make_board(board)
        print("\nGame Over.\n")
        print(" **** " + player + " won. ****")
        play_again()
    elif board['7'] == board['5'] == board['3'] != ' ':  # diagonal
        make_board(board)
        print("\nGame Over.\n")
        print(" **** " + player + " won. ****")
        play_again()
    elif board['1'] == board['5'] == board['9'] != ' ':  # diagonal
        make_board(board)
        print("\nGame Over.\n")
        print(" **** " + player + " won. ****")
        play_again()
    else:
        return True


# loop thru X,Os to count if it's a tie
def is_board_full(board):
    count = 0
    for a in board:
        if board[a] == "X" or board[a] == "O":
            count += 1
    if count == 9:
        print("The game ends in a Tie!")
        play_again()
    return True


def play_again():
    answer = input("Want to play again? Type Y or N. ").upper()
    global board
    if answer == 'Y':
        # reset dict back
        board = {key: ' ' for key in board}
    else:
        # turn game off
        global game_on
        game_on = False


# intro
print("Let's play Tic-Tac-Toe! Each space is numbered 1-9 across.")
make_board(board)

while game_on:
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    game(player)
