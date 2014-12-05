def drawboard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def getboardcopy(board):
    copyBoard = []
    for i in board:
        copyBoard.append(i)
    return copyBoard


def iswinner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter)
            or
            (board[4] == letter and board[5] == letter and board[6] == letter)
            or
            (board[1] == letter and board[2] == letter and board[3] == letter)
            or
            (board[7] == letter and board[4] == letter and board[1] == letter)
            or
            (board[8] == letter and board[5] == letter and board[2] == letter)
            or
            (board[9] == letter and board[6] == letter and board[3] == letter)
            or
            (board[7] == letter and board[5] == letter and board[3] == letter)
            or
            (board[9] == letter and board[5] == letter and board[1] == letter))


def is_space_empty(board, space):
    return board[space] == ' '


def getplayermove(board):
    move = 0
    while move not in "1 2 3 4 5 6 7 8 9".split() and is_space_empty(board,
                                                                     move):
        move = input("where do you play?(1-9 and free)")
    return int(move)


def getcomputermove(board):
    for i in range(1, 10):
        copyBoard = getboardcopy(board)
        if is_space_empty(copyBoard, i):
            copyBoard[i] = "X"
            if iswinner(copyBoard, "X"):
                return i
    for i in range(1, 10):
        copyBoard = getboardcopy(board)
        if is_space_empty(copyBoard, i):
            copyBoard[i] = "O"
            if iswinner(copyBoard, "O"):
                return i
    if is_space_empty(board, 5):
        return 5

    for i in [1, 3, 7, 9]:
        if is_space_empty(board, i):
            return i

    for i in [2, 4, 6, 8]:
        if is_space_empty(board, i):
            return i


def makeplayermove(board):
    move = getplayermove(board)
    board[move] = "O"


def makecomputermove(board):
    move = getcomputermove(board)
    if move not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return "fail"
    board[move] = "X"


def isboardfull(board):
    for i in range(1, 10):
        if is_space_empty(board, i):
            return False
    return True


def main():
    Thebigbadboard = [" "] * 10
    gameplay = True
    while(gameplay):
        drawboard(Thebigbadboard)
        makeplayermove(Thebigbadboard)
        if iswinner(Thebigbadboard, "O"):
            drawboard(Thebigbadboard)
            print("You Win!")
            gameplay = False
        if isboardfull(Thebigbadboard):
            drawboard(Thebigbadboard)
            print("Tie")
            gameplay = False
        makecomputermove(Thebigbadboard)
        if iswinner(Thebigbadboard, "X"):
            drawboard(Thebigbadboard)
            print("You Lose!")
            gameplay = False


if __name__ == '__main__':
    main()
