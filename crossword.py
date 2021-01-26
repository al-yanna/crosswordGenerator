# Created by: Alyanna Santos


# printboard(board) function prints out the 20x20 matrix with borders and coordinates.
def printboard(board):
    print(' 01234567890123456789')
    print(blank + '_' * 20)
    for row in range(20):
        for col in range(23):
            if col == 0 or col == 21:
                print('|', end='')
            elif col == 22:
                print(row, end='')
            else:
                print(board[row][col - 1], end='')
        print()
    print(blank + '_' * 20)
    print(' 01234567890123456789')
blank = ' '
board = [[blank] * 20 for i in range(20)]

# addFirstWord function adds the first word in the middle of the 20x20 matrix.
def addFirstWord(board, word):
    middle = (len(word)) // 2
    index = 0
    start = 10 - middle
    end = 10 + middle
    if len(word) > 20:
        return False
    else:
        if len(word) % 2 == 1:
            for i in range(start, end + 1):
                board[10][i] = word[index]
                index += 1
        else:
            for i in range(start, end):
                board[10][i] = word[index]
                index += 1
        return True


# adjacentVertical and adjacentHorizontal functions are used to make sure the placement of a
# word is not adjacent to any letter which is not in the word in which the word intersects.
def adjacentVertical(row, col):
    if board[row][col + 1] != blank:
        return True
    if board[row][col - 1] != blank:
        return True
    else:
        return False

def adjacentHorizontal(row, col):
    if board[row + 1][col] != blank:
        return True
    if board[row - 1][col] != blank:
        return True
    else:
        return False

# checkVertical and checkHorizontal functions are used to check if the word can be placed
# vertically or horizontally along the matrix containing words in list.
legalError = ''
def checkVertical(board, word, row, col):
    global legalError
    if len(word) > 20 - row:
        return False
    else:
        for letter in range(len(word)):
            if word[letter] == board[row + letter][col]:
                return True
            if board[row + letter][col] == blank:
                if adjacentVertical(row + letter, col):
                    legalError = 'illegal adjacencies'
                    return False
                else:
                    continue
            elif word[letter] != board[row + letter][col]:
                legalError = 'no matching letter'
                return False

def checkHorizontal(board, word, row, col):
    global legalError
    if len(word) > 20 - col:
        return False
    else:
        for letter in range(len(word)):
            if word[letter] == board[row][col + letter]:
                return True
            if board[row][col + letter] == blank:
                if adjacentHorizontal(row, col + letter):
                    legalError = 'illegal adjacencies'
                    return False
                else:
                    continue
            elif word[letter] != board[row][col + letter]:
                legalError = 'no matching letter'
                return False

# addVertical and addHorizontal functions are used to place all the words that can be placed
# legally onto the crossword into the 20x20 matrix.
def addVertical(board, word):
    for row in range(len(board) - 1):
        for col in range(len(board) - 1):
            if checkVertical(board, word, row, col):
                for letter in range(len(word)):
                    if adjacentVertical(row, col):
                        return False
                    else:
                        board[row + letter][col] = word[letter]
                return True
    return False

def addHorizontal(board, word):
    for row in range(len(board) - 1):
        for col in range(len(board) - 1):
            if checkHorizontal(board, word, row, col):
                for letter in range(len(word)):
                    if adjacentHorizontal(row, col):
                        return False
                    else:
                        board[row][col + letter] = word[letter]
                return True
    return False

# crossword(L) function
def crossword(L):
    global legalError
    for word in range(len(L)):
        if L[0] == L[word]:
            if len(L[word]) > 20:
                print(L[word], 'reaches outside grid')
            else:
                addFirstWord(board, L[word])
    for index in range(1, len(L)):
        if index % 2 == 1:
            if len(L[index]) > 20:
                print(L[index], 'reaches outside grid')
            else:
                addVertical(board, L[index])
        else:
            if len(L[index]) > 20:
                print(L[index], 'reaches outside grid')
            else:
                if legalError == 'illegal adjacencies':
                    print(L[index], 'has illegal adjacencies')
                addHorizontal(board, L[index])

# -----------------------------------------------------------------------------------------

# Testng:

# For L, 'burr' does not have matching letters, therefore not added into the crossword.
L = ['clowning', 'incline', 'plan', 'apple', 'temp', 'burr']
crossword(L)
printboard(board)
print()
blank = ' '
board = [[blank] * 20 for i in range(20)]

# For L2, 'appleeeeeeeeeeeeeeeeeeeeeeeeee' reaches out of the grid and 'burr' does not have matching letters,
# therefore not added into the crossword.
L2 = ['clowning', 'incline', 'plan', 'appleeeeeeeeeeeeeeeeeeeeeeeeee', 'burr', 'temp']
crossword(L2)
printboard(board)
print()
blank = ' '
board = [[blank] * 20 for i in range(20)]

# For L3, 'prove' has illegal agencies and 'burr' does not have matching letters,
# therefore not added into the crossword.
L3 = ['clowning', 'incline', 'plan', 'apple', 'temp', 'burr', 'prove']
crossword(L3)
printboard(board)
print()
blank = ' '
board = [[blank] * 20 for i in range(20)]
