import random
import pandas


class Ai_chess(object):    
    
    def __init__(self) -> None:
        self.scorePerPiece = {'Pawn': 1, 'Night': 3, 'Bishop': 3,
                     'Rook': 5, 'Queen': 9, 'King': 1000}

        self.chessDataBase= pandas.read_csv('openning/data.csv')
    
    def OpenningBook(self, curMoves):
        result = None
        for move in self.chessDataBase.iloc[:,0]:
            if curMoves == move[:len(curMoves)]:
                result = move
                print(result)
                return result
            
    def FindBestMove(self, board, moves,pieceInBoard):
        colDict = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                   'e': 4, 'f': 5, 'g': 6, 'h': 7}
        bestMoves = None
        bestPiece = None

        openning = self.OpenningBook(moves)
        if openning != None:
            blackMove = openning.split(' ')[len(moves.split(' '))]
            
            if blackMove=='O-O':
                bestPiece= board[0][4]
                bestMoves= (0,6)
                print(bestPiece.GetType(),bestMoves)

                return (bestPiece, bestMoves)

            elif blackMove=='O-O-O':
                bestPiece=board[0][4]
                bestMoves= (0,2)
                print(bestPiece.GetType(),bestMoves)
                return (bestPiece, bestMoves)
            bestMoves = (8-int(blackMove[-1]), colDict[blackMove[-2]])

            

            if blackMove[0].isupper():
                for piece in pieceInBoard[blackMove[0]]:
                    if bestMoves in piece.GetAllValidMoves(board) :
                        bestPiece = piece
                        break
            else:
                for piece in pieceInBoard['P']:

                    if bestMoves in piece.GetAllValidMoves(board):
                        bestPiece = piece
                        break

        else:
            possible_Moves_Of_Piece, piecesDict, pieces = self.FindAllPossibleMoves(
                board, True)
            bestSore = -pow(2, 30)

            for piece in range(pieces):
                for possibleMove in possible_Moves_Of_Piece[piecesDict[piece]]:

                    row, col = possibleMove[0], possibleMove[1]
                    score = self.Minimax(self.Result(
                        row, col, board, piecesDict[piece]), False, 1, -pow(2, 30), pow(2, 30))
                    if score > bestSore:
                        bestSore = score
                        bestPiece = piecesDict[piece]
                        bestMoves = (row, col)
        return (bestPiece, bestMoves)

    def Evaluate(self, board):
        whiteScores = 0
        blackScores = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] != None:
                    if board[i][j].GetTeam() == 'White':
                        whiteScores += self.scorePerPiece[board[i]
                                                          [j].GetType()]
                    else:
                        blackScores += self.scorePerPiece[board[i]
                                                          [j].GetType()]
        return blackScores-whiteScores

    def FindAllPossibleMoves(self, board, isMaximizing):
        possible_Moves_Of_Piece = {}
        piecesDict = {}
        pieces = 0
        for i in range(8):
            for j in range(8):
                currentPiece = board[i][j]
                if currentPiece != None and currentPiece.GetTeam() == 'Black' if isMaximizing else 'White':
                    if currentPiece == None:
                        continue
                    validMove = currentPiece.GetAllValidMoves(board)
                    if len(validMove) > 0:
                        piecesDict[pieces] = currentPiece
                        possible_Moves_Of_Piece[currentPiece] = validMove
                        pieces += 1
        return (possible_Moves_Of_Piece, piecesDict, pieces)

    def Result(self, row, col, board, piece):
        newBoard = [row[:] for row in board]
        newBoard[row][col] = newBoard[piece.row][piece.col]
        newBoard[piece.row][piece.col] = None

        return newBoard

    def Minimax(self, board, isMaximizing, depth, alpha, beta):
        if depth == 3:
            return self.Evaluate(board)

        possible_Moves_Of_Piece, piecesDict, pieces = self.FindAllPossibleMoves(
            board, isMaximizing)
        bestSore = None

        # Ai Turn
        if isMaximizing:
            bestSore = -pow(2, 30)
            for piece in range(pieces):
                for possibleMove in possible_Moves_Of_Piece[piecesDict[piece]]:
                    row, col = possibleMove[0], possibleMove[1]
                    score = self.Minimax(self.Result(
                        row, col, board, piecesDict[piece]), False, depth+1, alpha, beta)
                    bestSore = max(bestSore, score)
                    alpha = max(alpha, bestSore)
                    if beta <= alpha:
                        break

        # Human Turn
        else:
            bestSore = pow(2, 30)
            for piece in range(pieces):
                for possibleMove in possible_Moves_Of_Piece[piecesDict[piece]]:
                    row, col = possibleMove[0], possibleMove[1]
                    score = self.Minimax(self.Result(
                        row, col, board, piecesDict[piece]), True, depth+1, alpha, beta)
                    bestSore = min(bestSore, score)
                    beta = min(bestSore, beta)
                    if beta <= alpha:
                        break
        return bestSore

    
