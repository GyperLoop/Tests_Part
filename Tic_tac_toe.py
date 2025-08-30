import random

ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, BLANK = 'X', 'O', ' '

def main():
    print('Welcome to Tic-Tac-Toe!')

    # Ask game mode
    mode = ''
    while mode not in ['1', '2']:
        print('Choose game mode:')
        print('1. Player vs Player')
        print('2. Player vs Computer')
        mode = input('> ')

    difficulty = None
    if mode == '2':
        while difficulty not in ['1', '2']:
            print('Choose difficulty:')
            print('1. Easy')
            print('2. Hard')
            difficulty = input('> ')

    gameBoard = getBlankBoard()
    currentPlayer, nextPlayer = X, O

    while True:
        print(getBoardStr(gameBoard))

        if mode == '1' or currentPlayer == X:  # Human move
            move = None
            while not isValidSpace(gameBoard, move):
                print("What is {}'s move? (1-9)".format(currentPlayer))
                move = input('> ')
        else:  # Computer move
            move = getComputerMove(gameBoard, currentPlayer, nextPlayer, difficulty)
            print("Computer chooses:", move)

        updateBoard(gameBoard, move, currentPlayer)

        # Check win/tie
        if isWinner(gameBoard, currentPlayer):
            print(getBoardStr(gameBoard))
            print(currentPlayer + ' has won the game!')
            break
        elif isBoardFull(gameBoard):
            print(getBoardStr(gameBoard))
            print('The game is a tie!')
            break

        currentPlayer, nextPlayer = nextPlayer, currentPlayer

    print('Thanks for playing!')

def getBlankBoard():
    return {space: BLANK for space in ALL_SPACES}

def getBoardStr(board):
    return ''' 
      {}|{}|{}  1 2 3 
      -+-+- 
      {}|{}|{}  4 5 6 
      -+-+- 
      {}|{}|{}  7 8 9'''.format(board['1'], board['2'], board['3'],
                                board['4'], board['5'], board['6'],
                                board['7'], board['8'], board['9'])

def isValidSpace(board, space):
    return space in ALL_SPACES and board[space] == BLANK

def isWinner(board, player):
    b, p = board, player
    return ((b['1'] == b['2'] == b['3'] == p) or
            (b['4'] == b['5'] == b['6'] == p) or
            (b['7'] == b['8'] == b['9'] == p) or
            (b['1'] == b['4'] == b['7'] == p) or
            (b['2'] == b['5'] == b['8'] == p) or
            (b['3'] == b['6'] == b['9'] == p) or
            (b['3'] == b['5'] == b['7'] == p) or
            (b['1'] == b['5'] == b['9'] == p))

def isBoardFull(board):
    return all(board[space] != BLANK for space in ALL_SPACES)

def updateBoard(board, space, mark):
    board[space] = mark

def getComputerMove(board, computer, opponent, difficulty):
    available = [s for s in ALL_SPACES if isValidSpace(board, s)]

    if difficulty == '1':  # Easy → purely random
        return random.choice(available)

    # Hard → mostly smart, sometimes random
    if random.random() < 0.2:  # 20% chance random
        return random.choice(available)

    # Otherwise → best move via minimax
    bestScore = -float('inf')
    bestMove = None
    for space in available:
        board[space] = computer
        score = minimax(board, False, computer, opponent)
        board[space] = BLANK
        if score > bestScore:
            bestScore = score
            bestMove = space
    return bestMove

def minimax(board, isMaximizing, computer, opponent):
    if isWinner(board, computer):
        return 1
    elif isWinner(board, opponent):
        return -1
    elif isBoardFull(board):
        return 0

    if isMaximizing:
        bestScore = -float('inf')
        for space in ALL_SPACES:
            if isValidSpace(board, space):
                board[space] = computer
                score = minimax(board, False, computer, opponent)
                board[space] = BLANK
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = float('inf')
        for space in ALL_SPACES:
            if isValidSpace(board, space):
                board[space] = opponent
                score = minimax(board, True, computer, opponent)
                board[space] = BLANK
                bestScore = min(score, bestScore)
        return bestScore

if __name__ == '__main__':
    main()