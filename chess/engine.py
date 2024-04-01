import random

class Ai_chess(object):
    scorePerPiece={'Pawn':1,'Night':3,'Bishop':3,
                   'Rook':5,'Queen':9,'King':1000}
    
    def FindBestMove(self,board):
        possible_Moves_Of_Piece,piecesDict,pieces=self.FindAllPossibleMoves(board,True)
        bestMoves=None
        bestPiece=None
        bestSores=-pow(2,30)

        for piece in range(pieces):
            for possibleMove in possible_Moves_Of_Piece[piecesDict[piece]]:
                row,col= possibleMove[0],possibleMove[1]
                score=  self.Minimax(self.Result(row,col,board,piecesDict[piece]),False,1)
                if score>bestSores:
                    bestSores=score
                    bestPiece= piecesDict[piece]
                    bestMoves= (row,col)
        return (bestPiece,bestMoves)
    
    # def Evaluate(self,board,isMaximizing):
    def Evaluate(self,board):
        whiteScores=0
        blackScores=0
        for i in range(8):
            for j in range(8):
                if board[i][j]!=None:
                    if board[i][j].GetTeam()=='White':
                        whiteScores+= self.scorePerPiece[board[i][j].GetType()]
                    else:
                        blackScores+= self.scorePerPiece[board[i][j].GetType()]
        # return whiteScores-blackScores if isMaximizing else blackScores-whiteScores
        return blackScores-whiteScores
                        


    def FindAllPossibleMoves(self,board,isMaximizing):
        possible_Moves_Of_Piece= {}
        piecesDict={}
        pieces=0
        for i in range(8):
            for j in range(8):
                currentPiece= board[i][j]
                if currentPiece!= None and currentPiece.GetTeam()=='Black' if isMaximizing else 'White':
                    if currentPiece==None:
                        continue
                    validMove= currentPiece.GetAllValidMoves(board)
                    if len(validMove)>0:
                        piecesDict[pieces]= currentPiece
                        possible_Moves_Of_Piece[currentPiece]= validMove
                        pieces+=1
        return (possible_Moves_Of_Piece,piecesDict,pieces)

    def Result(self,row,col,board,piece):
        newBoard= [row[:] for row in board]
        newBoard[row][col]=newBoard[piece.row][piece.col]
        newBoard[piece.row][piece.col]=None

        return newBoard
        
    def Minimax(self,board,isMaximizing,depth):
        if depth== 1:
            # return self.Evaluate(board,isMaximizing)
            return self.Evaluate(board)
        
        
        possible_Moves_Of_Piece,piecesDict,pieces=self.FindAllPossibleMoves(board,isMaximizing)
        bestSores=None

        # Ai Turn 
        if isMaximizing:
            bestSores=-pow(2,30)
            for piece in range(pieces):
                for possibleMove in possible_Moves_Of_Piece[piecesDict[piece]]:
                    row,col= possibleMove[0],possibleMove[1]
                    score=  self.Minimax(self.Result(row,col,board,piecesDict[piece]),False,depth+1)
                    bestSores= max(bestSores,score)
            
        # Human Turn
        else:
            bestSores=pow(2,30)
            for piece in range(pieces):
                for possibleMove in possible_Moves_Of_Piece[piecesDict[piece]]:
                    row,col= possibleMove[0],possibleMove[1]
                    score=  self.Minimax(self.Result(row,col,board,piecesDict[piece]),True,depth+1)
                    bestSores= min(bestSores,score)
        return bestSores
      
                    





