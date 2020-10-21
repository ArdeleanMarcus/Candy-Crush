class Solutie:
    def candycrush(self, board):
        #verificare eroare
        if not board:
            board

        done = True
        #1 verificare randuri
        for randuri in range(len(board)):
            for coloane in range(len(board[randuri]-2)):
                numar1 = abs(board[r][c])
                numar2 = abs(board[r][c+1])
                numar3 = abs(board[r][c+2])
                if numar1 == numar2 and numar2 == numar3 and numar1 != 0:
                    board[r][c] = -numar1
                    board[r][c+1] = -numar2
                    board[r][c+2] = -numar3
                    done = False

        #2verificare coloane



        #3gravitate



        return board if done else candyCrush(board)


