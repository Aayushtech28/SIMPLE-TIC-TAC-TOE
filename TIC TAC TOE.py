board = [' ' for x in range(1 , 11)]

def insertLetter(letter,pos):
    board[pos] = letter

def freeSpace(pos):
    return board[pos] == ' '

def printBoard(board):
    print("   |   |   ")
    print(' ' + board[1] + ' | '  +  board[2] + ' | ' + board[3])
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(' ' + board[4] +  ' | ' +  board[5] + ' | ' +  board[6])
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(' ' + board[7] +  ' | ' + board[8] +  ' | ' + board[9])
    print("   |   |   ")

def IsBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def winner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
            (b[4] == l and b[5] == l and b[6] == l) or
            (b[7] == l and b[8] == l and b[9] == l) or
            (b[1] == l and b[4] == l and b[7] == l) or
            (b[2] == l and b[5] == l and b[8] == l) or
            (b[3] == l and b[6] == l and b[9] == l) or
            (b[1] == l and b[5] == l and b[9] == l) or
            (b[3] == l and b[5] == l and b[7] == l))

def playerMove():
    run = True
    while(run == True):
        move  = int(input("please select a position to enter the X between 1 to 9"))
        if move > 0 and move < 10:
            if freeSpace(move):
                run = False
                insertLetter('X' , move)
            else:
                print("space is occupied")
        else:
            print("Enter a number between 1 and 9")

def computerMove():
    import random
    possiblemoves = [x for x , letter in enumerate(board)  if letter == ' ' and x != 0]
    move = 0

    for let in ['0' , 'X']:
        for i in possiblemoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if winner(boardcopy , let):
                move = i
                return move

    cornersAvail = []
    for i in possiblemoves:
        if i in [1,3,7,9]:
            cornersAvail.append(i)


    if len(cornersAvail) > 0:
        move = random.choice(cornersAvail)
        return move



    if 5 in possiblemoves:
        move = 5
        return move



    edgesAvail = []
    for i in possiblemoves:
        if i in [2,4,6,8]:
            edgesAvail.append(i)

    if len(edgesAvail) > 0:
        move = random.choice(edgesAvail)
        return move

def main():
    printBoard(board)
    while not (IsBoardFull(board)):
        if not (winner(board , 'O')):
            playerMove()

        else:
            print("sorry you loose")
            break
        if not (winner(board , 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertLetter('O' , move)
                printBoard(board)
        else:
            print("you win")
            break

    if IsBoardFull(board):
        print("Tie game")


while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
