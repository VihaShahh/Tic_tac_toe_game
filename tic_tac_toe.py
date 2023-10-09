
import random

board = [' ' for x in range(10)]


def print_board():
    print("-" * 15)
    print(f" {board[1]} | {board[2]} | {board[3]}")
    print("+" * 12)
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print("+" * 12)
    print(f" {board[7]} | {board[8]} | {board[9]}")
    print("-" * 15)


def set_move(pos, symbol):
    board[pos] = symbol


def is_free(pos):
    return board[pos] == ' '


def is_full():
    if board.count(' ') <= 1:
        return True
    else:
        return False


def calc_move():
    avail_moves = [x for x, char in enumerate(board) if char == ' ' and x != 0]
    move = 0
    print(avail_moves)
    for player in ['0', 'X']:
        for i in avail_moves:
            tmp_board = board[:]
            tmp_board[i] = player
            if is_won(tmp_board, player):
                move = i
                return move

    corners = []
    for i in avail_moves:
        if i in [1, 3, 7, 9]:
            corners.append(i)

    if len(corners) > 1:
        move = get_random_move(corners)
        return move

    if 5 in avail_moves:
        move = 5
        return move

    edges = []
    for i in avail_moves:
        if i in [2, 4, 6, 8]:
            move = edges.append(i)
            return move

    if len(edges) > 1:
        move = get_random_move(edges)
        print(move)
        return move

    return move


def get_random_move(list):
    mv = random.choice(list)
    print(mv)
    return mv


def is_won(bo, symbol):
    return (bo[1] == symbol and bo[2] == symbol and bo[3] == symbol) or \
           (bo[4] == symbol and bo[5] == symbol and bo[6] == symbol) or \
           (bo[7] == symbol and bo[8] == symbol and bo[9] == symbol) or \
           (bo[1] == symbol and bo[4] == symbol and bo[7] == symbol) or \
           (bo[2] == symbol and bo[5] == symbol and bo[8] == symbol) or \
           (bo[3] == symbol and bo[6] == symbol and bo[9] == symbol) or \
           (bo[1] == symbol and bo[5] == symbol and bo[9] == symbol) or \
           (bo[3] == symbol and bo[5] == symbol and bo[7] == symbol)


def player_move():
    valid = False
    while not valid:
        pos = int(input("Enter Your move from (1-9):"))
        if is_free(pos):
            if 1 <= pos <= 9:
                set_move(pos, 'X')
                print(f"User[X] choose {pos}.")
                return
            else:
                print("Enter choice between 1-9.")
                valid = False
        else:
            print("Space already occupied!")
            valid = False
    else:
        print("The block is already Occupied !")


def main():
    while not is_full():
        print_board()
        if is_won(board, '0'):
            print("Computer won the GAME !")
        else:
            player_move()
            print_board()

        if is_won(board, 'X'):
            print("User won the GAME !")
            break
        else:
            pos = calc_move()
            if pos == 0:
                print("Tie Game!")
                break
            else:
                set_move(pos, '0')
                print(f"Computer[0] choose {pos}.")
                print_board()

        if is_won(board, '0'):
            print("Computer won the GAME!")
            break
        elif is_won(board, 'X'):
            print("User won the GAME")

    if is_full() and not is_won(board, 'X') and not is_won(board, '0'):
        print("Tie Game!")


main()