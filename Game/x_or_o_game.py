from IPython.display import clear_output
def display_board(list_board, symbol, row, col):
    list_board[row][col] = symbol
    if check_win(list_board, symbol):
        print("You won!")
        return True
    print_board(list_board)
    return list_board


def default_board():
    col = 3
    row = 3
    default_list = [["_"] * col for i in range(row)]
    return default_list


def print_board(list_board):
    for i in range(len(list_board)):
        for j in range(len(list_board[i])):
            print(list_board[i][j], end=' ')
        print()


def check_win(list_board, symbol):
    if (check_col(list_board, symbol) or check_row(list_board, symbol) or
            check_diagonal(list_board, symbol) or check_diagonal(list_board, symbol, 2, True)):
        return True
    return False


def check_row(list_board, symbol):
    for i in range(len(list_board)):
        result = []
        for j in range(len(list_board[i])):
            if list_board[i][j] == symbol:
                result.append(True)
            else:
                result.append(False)
        print(result)
        if False not in result:
            return True
    return False


def check_col(list_board, symbol):
    for i in range(0, 3):
        result = []
        for j in range(0, 3):
            if list_board[j][i] == symbol:
                result.append(True)
            else:
                result.append(False)
        if False not in result:
            return True
    return False


def check_diagonal(list_board, symbol, start=0, second_diagonal=False):
    result = []
    j = start
    for i in range(len(list_board)):
        if list_board[i][j] == symbol:
            result.append(True)
        else:
            result.append(False)
        if second_diagonal:
            j -= 1
        else:
            j += 1
    if False not in result:
        return True
    return False

def x_or_o_game():
    list_board = default_board()
    while True:
        symbol = input("Введите свой символ")
        if symbol == " " or (symbol != "x" and symbol != "o"):
            symbol = input("Введите свой символ")
        row = int(input("Введите строку"))
        col = int(input("Введите столбец"))
        list_board = display_board(list_board, symbol, row-1, col-1)
        clear_output()
        if list_board == True:
            break

x_or_o_game()