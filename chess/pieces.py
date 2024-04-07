
class Pieces(object):
    team,type,row,col=None,None,None,None
    def __init__(self,team,row,col  ) -> None:
        self.team,self.row,self.col=team, row,col
        
    def GetType(self):
        return self.type
    def GetTeam(self):
        return self.team
    def Move(self,row,col,board):
        board[self.row][self.col]= None
        self.row,self.col= row,col
        board[row][col]= self
    def CheckInBoard(self,row,col):
        if row <0 or row >7 or col<0 or col >7:
            return False
    def GetAllValidMoves(self,board):
        pass

class Pawn(Pieces):
    type= 'Pawn'
    firstMove=False
    canEnPassant=False
    def __init__(self,team,row,col):
        self.team,self.row,self.col=team, row,col
   
    def SetFalse(self):
        self.canEnPassant=False

    def GetAllValidMoves(self,board ):
        res=[]
        if self.team=='White':
            if board[self.row-1][self.col]==None:
                res.append((self.row-1,self.col))
                if self.firstMove==False and board[self.row-2][self.col]==None:
                    res.append((self.row-2,self.col))
            if self.col!=0 and board[self.row-1][self.col-1]!=None and board[self.row-1][self.col-1].GetTeam()!=self.team:
                res.append((self.row-1,self.col-1))
            if self.col != 7 and  board[self.row-1][self.col+1]!=None and board[self.row-1][self.col+1].GetTeam()!=self.team :
                res.append((self.row-1,self.col+1))
        else:
            if board[self.row+1][self.col]==None:
                res.append((self.row+1,self.col))
                if self.firstMove==False and board[self.row+2][self.col]==None:
                    res.append((self.row+2,self.col))
            if self.col !=0 and board[self.row+1][self.col-1]!=None and board[self.row+1][self.col-1].GetTeam()!=self.team :
                res.append((self.row+1,self.col-1))
            if self.col != 7 and  board[self.row+1][self.col+1]!=None and board[self.row+1][self.col+1].GetTeam()!=self.team:
                res.append((self.row+1,self.col+1))

        return res
   
    def CheckPromotion(self):
        if self.team=='White' and self.row==0:
            return True
        elif self.team=='Black' and self.row== 7:
            return True
        return False
   
    def Promote(self,type,board):
    
        board[self.row][self.col]=  Classify(self.team,type,self.row,self.col)
            
    def Move(self,row,col,board):
        if self.firstMove==False:
            self.firstMove= True
            # if abs(row - self.row)==2:
            #     if board[row][col-1]!=None and board[row][col-1].GetTeam()!= self.team and board[row][col-1].GetType()=='Pawn':
            #         board[row][col-1].canEnPassant=True
            #     if board[row][col+1]!=None and board[row][col+1].GetTeam()!= self.team and board[row][col+1].GetType()=='Pawn':
            #         board[row][col+1].canEnPassant=True
        # if self.canEnPassant:
        #     if self.team=='White':
        #         if self.col-col==1 and  board[self.row][self.col-1]!=None and  board[self.row][self.col-1].GetTeam()!=self.team and board[self.row][self.col-1].GetType()=='Pawn' and self.row-row==1:
        #             board[self.row][self.col-1]=None
        #         elif col-self.col==1 and board[self.row][self.col+1]!=None and  board[self.row][self.col+1].GetTeam()!=self.team and board[self.row][self.col+1].GetType()=='Pawn' and self.row-row==1:
        #             board[self.row][self.col-1]=None
                    
        #     else:
        #         if self.col-col==1 and  board[self.row][self.col-1]!=None and  board[self.row][self.col-1].GetTeam()!=self.team and board[self.row][self.col-1].GetType()=='Pawn' and self.row-row==-1:
        #             board[self.row][self.col-1]=None
                    
        #         elif col-self.col==1 and board[self.row][self.col+1]!=None and  board[self.row][self.col+1].GetTeam()!=self.team and board[self.row][self.col+1].GetType()=='Pawn' and self.row-row==-1:
        #             board[self.row][self.col+1]=None
                    

        
        board[self.row][self.col]= None
        self.row,self.col= row,col
        board[row][col]= self
    
    def EnPassant(self):
        pass

class Rook(Pieces):
    type='Rook'
    def __init__(self,team,row,col):
        self.team,self.row,self.col=team, row,col
    def GetAllValidMoves(self, board):
        res=[]
        for row in range(self.row-1,-1,-1):
            if board[row][self.col]!= None :
                if board[row][self.col].GetTeam()!= self.team:
                    res.append((row,self.col))
                break
            res.append((row,self.col))
        
        for row in range(self.row+1,8):
            if board[row][self.col]!= None :
                if  board[row][self.col].GetTeam()!= self.team:
                    res.append((row,self.col))
                break
            res.append((row,self.col))

        for col in range(self.col-1,-1,-1):
            if board[self.row][col]!= None:
                if board[self.row][col].GetTeam()!= self.team:
                    res.append((self.row,col))
                break
            res.append((self.row,col))

        for col in range(self.col+1,8):
            if board[self.row][col]!= None :
                if board[self.row][col].GetTeam()!= self.team:
                    res.append((self.row,col))
                break
            res.append((self.row,col))
        return res      
    
class Knight(Pieces):
    type='Night'
    def __init__(self,team,row,col):
        self.team,self.row,self.col=team, row,col
        self.movesX=[-1,-2,-2,-1,1,2,2,1]
        self.movesY=[-2,-1,1,2,-2,-1,1,2]
    def GetAllValidMoves(self, board):
        res=[]
        for i in range(8):
            newRow= self.row+ self.movesX[i]
            newCol= self.col+ self.movesY[i]
            if self.CheckInBoard(newRow,newCol)==False or board[newRow][newCol]!= None and board[newRow][newCol].GetTeam()==self.team:
                continue
            res.append((newRow,newCol))
        return res
            
class Bishop(Pieces):
    type='Bishop'
    def __init__(self,team,row,col):
        self.team,self.row,self.col=team, row,col
    def GetAllValidMoves(self, board):
        res=[]
        for row in range(self.row-1,-1,-1):
            newCol = self.row - row + self.col
            if self.CheckInBoard(row,newCol)==False:
                break
            if board[row][newCol]!= None :
                if board[row][newCol].GetTeam()!= self.team:
                    res.append((row,newCol))
                break
            res.append((row,newCol))

        for row in range(self.row+1,8):
            newCol = self.row - row + self.col
            if self.CheckInBoard(row,newCol)==False:
                break
            if board[row][newCol]!= None :
                if board[row][newCol].GetTeam()!= self.team:
                    res.append((row,newCol))
                break
            res.append((row,newCol))

        for row in range(self.row-1,-1,-1):
            newCol =-( self.row - row) + self.col
            if self.CheckInBoard(row,newCol)==False:
                break
            if board[row][newCol]!= None :
                if board[row][newCol].GetTeam()!= self.team:
                    res.append((row,newCol))
                break
            res.append((row,newCol))
        
        for row in range(self.row+1,8):
            newCol = row-self.row + self.col
            if self.CheckInBoard(row,newCol)==False:
                break
            if board[row][newCol]!= None :
                if board[row][newCol].GetTeam()!= self.team:
                    res.append((row,newCol))
                break
            res.append((row,newCol))
        return res

class King(Pieces):
    firstMove=False
    type='King'
    isCastling= False
    def __init__(self,team,row,col):
        self.team,self.row,self.col= team,row,col
        self.movesX=[-1,-1,-1,0,0,1,1,1]
        self.movesY=[-1,0,1,-1,1,-1,0,1]
    def GetAllValidMoves(self,board):
        res=[]
        for i in range(8):
            newRow= self.row+ self.movesX[i]
            newCol= self.col+ self.movesY[i]
            if self.CheckInBoard(newRow,newCol)==False or board[newRow][newCol]!= None and board[newRow][newCol].GetTeam()==self.team:
                continue
            res.append((newRow,newCol))
        if self.firstMove==False and self.row==7 and self.col == 4 or self.row== 0 and self.col==4:
            if self.team=='White':
                if board[7][5]==None and board[7][6]==None:
                    res.append((7,6))
                if board[7][1]==None and board[7][2]==None and board[7][3]==None:
                    res.append((7,2))
            else:
                if board[0][5]==None and board[0][6]==None:
                    res.append((0,6))
                if board[0][1]==None and board[0][2]==None and board[0][3]==None:
                    res.append((0,2))

        return res
    def Move(self, row, col, board):
        self.firstMove= True
        self.Castling(row,col,board)

    def Castling(self,row,col,board):
        if abs(col-self.col)==2 and row == self.row:
            if col > self.col:  
                board[row][col-1]=  Rook(self.team,self.row,col-1)
                board[row][7]= None
            else:
                board[row][col+1]= Rook(self.team,self.row,col+1)
                board[row][0]=None
        board[self.row][self.col]= None
        self.row,self.col= row,col
        board[row][col]= self

class Queen(Rook,Bishop):
    type='Queen'
    def __init__(self,team,row,col):
        self.team,self.row,self.col=team,row,col
    def GetAllValidMoves(self,board):
        res=[]
        res+=Rook(self.team,self.row,self.col).GetAllValidMoves(board)
        res+= Bishop(self.team,self.row,self.col).GetAllValidMoves(board)
        return res

def Classify(team,type,row,col):
        if type=='P':
            return Pawn(team,row,col)
        elif type=='R':
            return Rook(team,row,col)
        elif type=='N':
            return Knight(team,row,col)
        elif type=='B':
            return Bishop(team,row,col)
        elif type=='Q':
            return Queen(team,row,col)
        elif type=='K':
            return King(team,row,col)