import numpy as np
from numpy import random

'''
0 - nu există nici o bomboană în acel element
1 - bomboană de culoare roșie
2 - bomboană de culoare galbenă
3 - bomboană de culoare verde
4 - bomboană de culoare albastră
'''

# initializare matrice 11 X 11 cu bomboane de diverse culori
#board = np.random.randint(choice, size=(11, 11))
board =  random.choice([1, 2, 3, 4], size=(11, 11))
print(board)
print("\n")
zdrobire = True

def drop(board):
    for c in range(len(board)):
        for r in range(len(board)):
            if board[r][c] == 0 and r !=0:
                for k in range(r, 0, -1):
                    board[k][c], board[k-1][c] = board[k-1][c], board[k][c]

def inlocuire(board):
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 0:
                board[r][c] = random.choice([1, 2, 3, 4])




'''
def inlocuire_linie_3(board):
    for r in range(len(board)):
        for c in range(len(board) - 2):
            if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                board[r][c] = board[r][c+1] = board[r][c+2] = 0
                scor = scor + 5
                pasi = pasi + 1
                print(board)
                drop(board)
                print(board)
                inlocuire(board)
                print(board)
                print("linie")
                print("scor = ", scor)
                print("pasi = ", pasi)
                print("\n")
                zdrobire = False

    # sortare coloane
    for r in range(len(board) - 2):
        for c in range(len(board)):
            if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                board[r][c] = board[r+1][c] = board[r+2][c] = 0
                scor = scor + 5
                pasi = pasi + 1
                print(board)
                drop(board)
                print(board)
                inlocuire(board)
                print(board)
                print("coloana")
                print("\n")
                print("scor = ", scor)
                print("pasi = ", pasi)
                zdrobire = False

'''

def candy_crush():
    scor = 0
    pasi = 0
    '''
    # LINIE DE 5
    # sortare linii
    for r in range(len(board)):
        for c in range(len(board) - 4):
            while abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) == abs(board[r][c+3]) == abs(board[r][c+4]) != 0:
                board[r][c] = board[r][c+1] = board[r][c+2] = board[r][c+3] = board[r][c+4] = 0
                scor = scor + 50
                pasi = pasi + 1
                print(board)
                drop(board)
                print(board)
                inlocuire(board)
                print(board)
                print("linie")
                print("scor = ", scor)
                print("pasi = ", pasi)
                print("\n")
                zdrobire = False

    # sortare coloane
    for r in range(len(board) - 4):
        for c in range(len(board)):
            while abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) == abs(board[r+3][c]) == abs(board[r+4][c]) != 0:
                board[r][c] = board[r+1][c] = board[r+2][c] = board[r+3][c] = board[r+4][c] = 0
                scor = scor + 50
                pasi = pasi + 1
                print(board)
                drop(board)
                print(board)
                inlocuire(board)
                print(board)
                print("coloana")
                print("\n")
                print("scor = ", scor)
                print("pasi = ", pasi)
                zdrobire = False

    # LINIE DE 4
    # sortare linii
    for r in range(len(board)):
        for c in range(len(board) - 3):
            while abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) == abs(board[r][c+3]) != 0:
                board[r][c] = board[r][c+1] = board[r][c+2] = board[r][c+3] = 0
                scor = scor + 10
                pasi = pasi + 1
                print(board)
                drop(board)
                print(board)
                inlocuire(board)
                print(board)
                print("linie")
                print("scor = ", scor)
                print("pasi = ", pasi)
                print("\n")
                zdrobire = False

    # sortare coloane
    for r in range(len(board) - 3):
        for c in range(len(board)):
            while abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]) == abs(board[r + 3][c]) != 0:
                board[r][c] = board[r+1][c] = board[r+2][c] = board[r+3][c] = 0
                scor = scor + 10
                pasi = pasi + 1
                print(board)
                drop(board)
                print(board)
                inlocuire(board)
                print(board)
                print("coloana")
                print("\n")
                print("scor = ", scor)
                print("pasi = ", pasi)
                zdrobire = False

'''
    # LINIE DE 3
    # sortare linii
    r_linie = range(len(board))
    c_linie = range(len(board) - 2)
    r_coloana = range(len(board) - 2)
    c_coloana = range(len(board))
    for r in range(len(board) - 2):
        for c in range(len(board) - 2):
            while abs(board[r_linie][c_linie]) == abs(board[r_linie][c_linie+1]) == abs(board[r_linie][c_linie+2]) != 0 or abs(board[r_coloana][c_coloana]) == abs(board[r_coloana+1][c_coloana]) == abs(board[r_coloana+2][c_coloana]) != 0:
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    for r in range(len(board)):
                        for c in range(len(board) - 2):
                            if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                                board[r][c] = board[r][c+1] = board[r][c+2] = 0
                                scor = scor + 5
                                pasi = pasi + 1
                                print(board)
                                drop(board)
                                print(board)
                                inlocuire(board)
                                print(board)
                                print("linie")
                                print("scor = ", scor)
                                print("pasi = ", pasi)
                                print("\n")
                                zdrobire = False
                elif abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    for r in range(len(board) - 2):
                        for c in range(len(board)):
                            if abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]) != 0:
                                board[r][c] = board[r + 1][c] = board[r + 2][c] = 0
                                scor = scor + 5
                                pasi = pasi + 1
                                print(board)
                                drop(board)
                                print(board)
                                inlocuire(board)
                                print(board)
                                print("coloana")
                                print("\n")
                                print("scor = ", scor)
                                print("pasi = ", pasi)
                                zdrobire = False
    return candy_crush() and scor if zdrobire else 0
'''
    # sortare coloane
    for r in range(len(board)):
        for c in range(len(board) - 2):
            while abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                for r in range(len(board) - 2):
                    for c in range(len(board)):
                        if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                            board[r][c] = board[r+1][c] = board[r+2][c] = 0
                            scor = scor + 5
                            pasi = pasi + 1
                            print(board)
                            drop(board)
                            print(board)
                            inlocuire(board)
                            print(board)
                            print("coloana")
                            print("\n")
                            print("scor = ", scor)
                            print("pasi = ", pasi)
                            zdrobire = False
'''






candy_crush()
