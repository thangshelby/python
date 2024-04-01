class Ai_Tic_Tac_Toe(object):
    def FindBestMove(self,board):
        bestMove= None
        bestScore= -100
        for action in self.Action(board):
            i,j= action[0],action[1]
            score= self.Minimax(self.Result(i,j,board,True),False)
            if score> bestScore:
                bestMove= (i,j)
                bestScore= score
        return bestMove
    
    def Action(self,board):
        actions= []
        for i in range(3):
            for j in range(3):
                if board[i][j]==None:
                    actions.append((i,j))
        return actions
    def Result(self,i,j,board,isMaximizing):
        newBoard= [row[:] for row in board]
        newBoard[i][j]= 'o' if isMaximizing else 'x'
        return newBoard
    def EvaluateValue(self,board):
        draw= None
        winner= None
        for row in range(0, 3):
            if((board[row][0] is not None) and (board[row][0] == board[row][1] == board[row][2])):
                winner = board[row][0]
                break     
        for col in range(0, 3):
            if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
                winner = board[0][col]
                break
     
        if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
            winner = board[0][0]
        if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
            winner = board[0][2]

        if(all([all(row) for row in board]) and winner is None):
            draw = True

        if winner==None and draw== None:
            return winner
        
        elif draw:
            return 0 
        elif winner=='o':
            return 1
        elif winner!='x':
            return -1
        
    def Minimax(self,board,isMaximizing):
        result= self.EvaluateValue(board)
        if result!=None:
            return result
    
        # Ai TURN 
        if isMaximizing:
            bestScore= -100
            for action in self.Action(board):
                i,j= action[0],action[1]
                score= self.Minimax(self.Result(i,j,board,True),False)
                bestScore= max(score,bestScore)
            return bestScore
        
        # HUMAN TURN
        else:
            bestScore= 100
            for action in self.Action(board):
                i,j= action[0],action[1]
                score= self.Minimax(self.Result(i,j,board,False),True)
                bestScore= min(score,bestScore)
            return bestScore