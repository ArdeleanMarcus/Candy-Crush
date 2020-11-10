import random
from numpy import *
import datetime

'''
0 - nu există nici o bomboană în acel element
1 - bomboană de culoare roșie
2 - bomboană de culoare galbenă
3 - bomboană de culoare verde
4 - bomboană de culoare albastră
'''
'''
def candy_crush(numar_de_jocuri:int, numar_procese:int):
    scor = 0
    mutari = 0
    
    for i in range(1, numar_de_jocuri):
        joc = random.randint(1, 10000)
        print("Jocul " + str(i) + " din procesul " + str(numar_procese) + "incepe. NR JOC = " + str(joc))
        joc.play()
        scor += joc.scor
        mutari += joc.mutari
        print("Jocul " + str(i) + " din procesul " + str(numar_procese) + " finalizat \n .Scor = " + str(joc.scor) + "\nMutari: " + str(joc.mutari))
    return
'''

def formatiune_T(scor, mutari):
    # Directie formatiune: Jos
    for r in range(len(board)-4):
        for c in range(1, len(board)-4):
            while board[r+1][c] == board[r][c] == board[r-1][c] == board[r-1][c-1] == board[r-1][c+1]:
                board[r + 1][c] = board[r][c] = board[r - 1][c] = board[r - 1][c - 1] = board[r - 1][c + 1] = 0
                scor += 30
                mutari += 1
                print(board, "\n")
                drop()
                print(board, "\n")
                inlocuire()
                print(board, "\n")
                print("T jos")
                print("scor = ", scor)
                print("pasi = ", mutari)
                print("\n")
                zdrobire = False


    # Directie formatiune: Sus
    for r in range(len(board)-4):
        for c in range(1, len(board)-4):
            while board[r+1][c] == board[r][c] == board[r-1][c] == board[r+1][c-1] == board[r+1][c+1]:
                board[r + 1][c] = board[r][c] = board[r - 1][c] = board[r + 1][c - 1] = board[r + 1][c + 1] = 0
                scor += 30
                mutari += 1
                print(board, "\n")
                drop()
                print(board, "\n")
                inlocuire()
                print(board, "\n")
                print("T sus")
                print("scor = ", scor)
                print("pasi = ", mutari)
                print("\n")
                zdrobire = False


    # Directie formatiune: Stanga
    for r in range(len(board)-4):
        for c in range(1, len(board)-4):
            while board[r][c-1] == board[r][c] == board[r][c+1] == board[r-1][c+1] == board[r+1][c+1]:
                board[r][c-1] = board[r][c] = board[r][c+1] = board[r-1][c+1] = board[r+1][c+1] = 0
                scor += 30
                mutari += 1
                print(board, "\n")
                drop()
                print(board, "\n")
                inlocuire()
                print(board, "\n")
                print("T stanga")
                print("scor = ", scor)
                print("pasi = ", mutari)
                print("\n")
                zdrobire = False


    #Directie formatiune: Dreapta
    for r in range(len(board)-4):
        for c in range(1, len(board)-4):
            while board[r][c-1] == board[r][c] == board[r][c+1] == board[r+1][c-1] == board[r-1][c-1]:
                board[r][c-1] = board[r][c] = board[r][c+1] = board[r+1][c-1] = board[r-1][c-1] = 0
                scor += 30
                mutari += 1
                print(board, "\n")
                drop()
                print(board, "\n")
                inlocuire()
                print(board, "\n")
                print("T dreapta")
                print("scor = ", scor)
                print("pasi = ", mutari)
                print("\n")
                zdrobire = False
    return scor, mutari

def formatiune_L(scor, mutari):
    # Directie formatiune: Colt stanga jos
    for r in range(len(board) - 4):
        for c in range(1, len(board) - 4):
            while board[r-1][c-1] == board[r][c-1] == board[r+1][c-1] == board[r+1][c] == board[r+1][c + 1]:
                board[r-1][c-1] = board[r][c-1] = board[r+1][c-1] = board[r+1][c] = board[r+1][c+1] = 0
                scor += 20
                mutari += 1
                print(board, "\n")
                drop()
                print(board, "\n")
                inlocuire()
                print(board, "\n")
                print("L stanga jos")
                print("scor = ", scor)
                print("pasi = ", mutari)
                print("\n")
                zdrobire = False

    # Directie formatiune: Colt dreapta jos
    for r in range(len(board) - 4):
        for c in range(1, len(board) - 4):
            while board[r+1][c-1] == board[r+1][c] == board[r+1][c+1] == board[r][c+1] == board[r-1][c+1]:
                board[r+1][c-1] = board[r+1][c] = board[r+1][c+1] = board[r][c+1] = board[r-1][c+1] = 0
                scor += 20
                mutari += 1
                print(board, "\n")
                drop()
                print(board, "\n")
                inlocuire()
                print(board, "\n")
                print("L dreapta jos")
                print("scor = ", scor)
                print("pasi = ", mutari)
                print("\n")
                zdrobire = False

    # Directie formatiune: Colt stanga sus
    for r in range(len(board) - 4):
        for c in range(1, len(board) - 4):
            while board[r-1][c-1] == board[r][c-1] == board[r+1][c-1] == board[r-1][c] == board[r-1][c+1]:
                board[r - 1][c - 1] = board[r][c - 1] = board[r + 1][c - 1] = board[r - 1][c] = board[r - 1][c + 1] = 0
                scor += 20
                mutari += 1
                print(board, "\n")
                drop()
                print(board, "\n")
                inlocuire()
                print(board, "\n")
                print("L stanga sus")
                print("scor = ", scor)
                print("pasi = ", mutari)
                print("\n")
                zdrobire = False

    # Directie formatiune: Colt dreapta sus
    for r in range(len(board) - 4):
        for c in range(1, len(board) - 4):
            while board[r+1][c - 1] == board[r+1][c] == board[r+1][c+1] == board[r][c+1] == board[r-1][c+1]:
                board[r + 1][c - 1] = board[r + 1][c] = board[r + 1][c + 1] = board[r][c + 1] = board[r - 1][c + 1] = 0
                scor += 20
                mutari += 1
                print(board, "\n")
                drop()
                print(board, "\n")
                inlocuire()
                print(board, "\n")
                print("L dreapta sus")
                print("scor = ", scor)
                print("pasi = ", mutari)
                print("\n")
                zdrobire = False
    return scor, mutari

def linie_de_5(scor, mutari):
    # LINIE DE 5
    # sortare linii
    for r in range(len(board)):
        for c in range(len(board) - 4):
            while abs(board[r][c]) == abs(board[r][c + 1]) == abs(board[r][c + 2]) == abs(board[r][c + 3]) == abs(
                    board[r][c + 4]) != 0:
                board[r][c] = board[r][c + 1] = board[r][c + 2] = board[r][c + 3] = board[r][c + 4] = 0
                scor = scor + 50
                mutari += 1
                print(board, "\n")
                drop()
                print(board, "\n")
                inlocuire()
                print(board, "\n")
                print("linie de 5")
                print("scor = ", scor)
                print("pasi = ", mutari)
                print("\n")
                zdrobire = False

    # sortare coloane
    for r in range(len(board) - 4):
        for c in range(len(board)):
            while abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]) == abs(board[r + 3][c]) == abs(
                    board[r + 4][c]) != 0:
                board[r][c] = board[r + 1][c] = board[r + 2][c] = board[r + 3][c] = board[r + 4][c] = 0
                scor = scor + 50
                mutari += 1
                print(board, "\n")
                drop()
                print(board, "\n")
                inlocuire()
                print(board, "\n")
                print("coloana de 5")
                print("\n")
                print("scor = ", scor)
                print("pasi = ", mutari)
                zdrobire = False
    return scor, mutari

def linie_de_4(scor, mutari):
    # LINIE DE 4
    # sortare linii
    for r in range(len(board)):
        for c in range(len(board) - 3):
            while abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) == abs(board[r][c+3]) != 0:
                board[r][c] = board[r][c+1] = board[r][c+2] = board[r][c+3] = 0
                scor += 10
                mutari += 1
                print(board, "\n")
                drop()
                print(board, "\n")
                inlocuire()
                print(board, "\n")
                print("linie de 4")
                print("scor = ", scor)
                print("pasi = ", mutari)
                print("\n")
                zdrobire = False

    # sortare coloane
    for r in range(len(board) - 3):
        for c in range(len(board)):
            while abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]) == abs(board[r + 3][c]) != 0:
                board[r][c] = board[r+1][c] = board[r+2][c] = board[r+3][c] = 0
                scor += 10
                mutari += 1
                print(board, "\n")
                drop()
                print(board, "\n")
                inlocuire()
                print(board, "\n")
                print("coloana de 4")
                print("\n")
                print("scor = ", scor)
                print("pasi = ", mutari)
                zdrobire = False
    return scor, mutari

def linie_de_3(scor, mutari):
    for r in range(len(board)):
        for c in range(len(board) - 2):
            while abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2])  != 0:
                board[r][c] = board[r][c+1] = board[r][c+2] = 0
                scor += 10
                mutari += 1
                print(board, "\n")
                drop()
                print(board, "\n")
                inlocuire()
                print(board, "\n")
                print("linie de 3")
                print("scor = ", scor)
                print("pasi = ", mutari)
                print("\n")
                zdrobire = False

    # sortare coloane
    for r in range(len(board) - 2):
        for c in range(len(board)):
            while abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]) != 0:
                board[r][c] = board[r+1][c] = board[r+2][c] = 0
                scor += 10
                mutari += 1
                print(board, "\n")
                drop()
                print(board, "\n")
                inlocuire()
                print(board, "\n")
                print("coloana de 3")
                print("\n")
                print("scor = ", scor)
                print("pasi = ", mutari)
                zdrobire = False
    return scor, mutari

#dupa ce o formatiune de bomboane a fost schimbata cu 0, acestea sunt mutate in partea de sus a matricei
def drop():
    for c in range(len(board)):
        for r in range(len(board)):
            if board[r][c] == 0 and r !=0:
                for k in range(r, 0, -1):
                    board[k][c], board[k-1][c] = board[k-1][c], board[k][c]

# dupa ce o formatiune de bomboane a fost zdrobita, elementele acesteia se schimba cu 0
def inlocuire():
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 0:
                board[r][c] = random.choice([1, 2, 3, 4])





if __name__ == '__main__':
    # numar_procese = 10
    # numar_de_jocuri = 10000
    scor = 0
    mutari = 0
    time_start = datetime.datetime.now()
    # initializare matrice 11 X 11 cu bomboane de diverse culori
    board = random.choice([1, 2, 3, 4], size=(11, 11))
    print(board)
    print("\n")

    linie_de_5(scor, mutari)
    formatiune_T(scor, mutari)
    formatiune_L(scor, mutari)
    linie_de_4(scor, mutari)
    linie_de_3(scor, mutari)




    ##
    #calculam intervalul de timp pentru
    time_end =datetime.datetime.now()
    final_time = time_end - time_start
    print("Durata: ", final_time)











