import pygame as pg
import os
import sys
from pygame.locals import *
import pieces
import engine
import time

pg.init()

class Chess(object):
    def GameInitiating(self):
        # GAME INIT
        self.width, self.height = 640, 640
        self.pWidth, self.pHeight = 70, 70
        self.fps = 32
        self.running = True
        self.hover = False
        self.x, self.y, self.row, self.col = None, None, None, None
        self.promoStatus= False
        self.turn  ='White'
        self.whiteTime= 900
        self.blackTime =900
        self.preMove=[]
        self.AiChess= engine.Ai_chess()
        self.moves=[]
        self.mode=None
        self.splash_screen=True
        # BOARD INIT

        self.screen = pg.display.set_mode(
            (self.width, self.height), 0, 120)
        pg.display.set_caption("Chess")

        self.splashImg= self.TransformImg(
            self.width, self.height,'splash2.jpg', False)
        self.mode1PlayerImg=  self.TransformImg(
            200,100,'2player.png', True)
        self.mode2PlayerImg=  self.TransformImg(
            200,100,'1player.png', True)

        self.boardImg = self.TransformImg(
            self.width, self.height, 'board2.web.webp', False)
        self.board:pieces.Pieces| None  = [[None] * 8 for _ in range(8)]

        # PIECE INIT
        self.pieceWhiteImages = {}
        self.pieceBlackImages = {}
        self.pieces = ['P', 'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        for piece in self.pieces:
            if piece not in self.pieceWhiteImages:
                self.pieceWhiteImages[piece] = self.TransformImg(
                    self.pWidth, self.pHeight, f"w{piece}.png", True)
                self.pieceBlackImages[piece] = self.TransformImg(
                    self.pWidth, self.pHeight, f"b{piece}.png", True)

        self.numberImgs={}    
        for i in range(10):
            self.numberImgs[i]=self.TransformImg(25,30,f"{i}.png",True)
        for i in range(1, 9):
            self.board[0][i-1] = pieces.Classify('Black',self.pieces[i],0,i-1)
            self.board[1][i-1] =  pieces.Classify('Black',self.pieces[0],1,i-1)
            self.board[7][i-1] =  pieces.Classify('White',self.pieces[i],7,i-1)
            self.board[6][i-1] =  pieces.Classify('White',self.pieces[0],6,i-1)

        self.DrawSplashScreen()

    def DrawSplashScreen(self):
        self.screen.blit(self.splashImg,(0,0))
        pg.display.flip()

    def DrawChess(self):
               
        if self.splash_screen:
            self.DrawSplashScreen()
     
        else:
            self.screen.blit(self.boardImg,(0,0))
            for i in range(8):
                for j in range(8):  
                    if self.board[i][j]:
                        if self.board[i][j].GetTeam()  == 'Black':
                            self.screen.blit(
                                self.pieceBlackImages[self.board[i][j].GetType()[0]], (50+j*68 , i*68+50))
                        else:
                            self.screen.blit(
                                self.pieceWhiteImages[self.board[i][j].GetType()[0]], (50+j*68 , i*68+50))

            self.DrawClock()
        pg.display.update()
    
    def DrawClock(self):
        whiteClock = pg.Surface((125,50),pg.SRCALPHA)


        whiteClock.fill('White')

        # Create default time fot both
        whiteMinute,blackMinute= round(self.whiteTime//60),round(self.blackTime//60)
        whiteSecond,blackSecond = round(self.whiteTime- whiteMinute*60),round(self.blackTime- blackMinute*60)
        

        # White clock
        whiteClock.blit(self.numberImgs[int(str(whiteMinute).rjust(2,'0')[0])],(5,10))
        whiteClock.blit(self.numberImgs[int(str(whiteMinute).rjust(2,'0')[1])],(35,10))
       
  
        whiteClock.blit(self.numberImgs[int(str(whiteSecond).rjust(2,'0')[0])],(65,10))
        whiteClock.blit(self.numberImgs[int(str(whiteSecond).rjust(2,'0')[1])],(95,10))
        
        self.screen.blit(whiteClock,(50+68*5,55+68*8))


        # Black clock
        if self.mode==2:
            blackClock = pg.Surface((125,50),pg.SRCALPHA)
            blackClock.fill('White')

            blackClock.blit(self.numberImgs[int(str(blackMinute).rjust(2,'0')[0])],(5,10))
            blackClock.blit(self.numberImgs[int(str(blackMinute).rjust(2,'0')[1])],(35,10))
            
    
            blackClock.blit(self.numberImgs[int(str(blackSecond).rjust(2,'0')[0])],(65,10))
            blackClock.blit(self.numberImgs[int(str(blackSecond).rjust(2,'0')[1])],(95,10))


            self.screen.blit(blackClock,(50+68*5,0))  

        pg.display.update()

    def LoadImg(self, path):
        return os.path.join('img', path)

    def TransformImg(self, width, height, path, alpha):
        if alpha:
            return pg.transform.scale(pg.image.load(self.LoadImg(path)).convert_alpha(), (width, height))
        else:
            return pg.transform.scale(pg.image.load(self.LoadImg(path)).convert(), (width, height))
    
    def UserClick(self):
        x, y = pg.mouse.get_pos()

        col,row = (x-50)//68, (y-50)//68

        if self.splash_screen:
            if x>=80 and x<=360 and y>=350 and y<=400:
                self.mode=1
                self.splash_screen= False
            elif x>=80 and x<= 360 and y>=410 and y<=460:
                self.mode=2
                self.splash_screen= False
                
            self.DrawChess()
            return
        
        else:
            if row <0 or row > 7 or col <0 or col >7 or (self.board[row][col]!= None and self.board[row][col].GetTeam()!= self.turn and self.hover==False):
                return 
            
            if self.promoStatus==True:
                self.Promote(row,col)
                return

            if  (self.hover == False or self.board[row][col] and self.board[row][col].GetTeam()==self.turn ):
                self.UnActivePiece()
                if self.board[row][col]:
                    self.hover = True
                    self.ActivePiece(row, col)
            else:
                self.hover= False

                if self.row == row and self.col == col:
                    self.UnActivePiece()
                elif (row,col) in self.board[self.row][self.col].GetAllValidMoves(self.board):
                    self.MovePiece(row,col)
        
    def ActivePiece(self, row, col):
        self.row,self.col= row,col
       

        for validMove in self.board[row][col].GetAllValidMoves(self.board):
            i,j = validMove[0],validMove[1]
            COLOR = (255, 255, 255)
            ALPHA = 128
            transparent_color = COLOR + (ALPHA,)
            dotMove =  pg.Surface((65, 65),pg.SRCALPHA)
            dotMove.fill(transparent_color)

            pg.draw.circle(dotMove,(123,127,120),(32,32),6)
            self.screen.blit(dotMove, (j*68+50, i*68+50))


        # for i in range (8):
        #     for j in range(8):
        #         if self.board[row][col].IsValidMove(i,j,self.board):
        #             COLOR = (255, 255, 255)
        #             ALPHA = 128
        #             transparent_color = COLOR + (ALPHA,)
        #             dotMove =  pg.Surface((65, 65),pg.SRCALPHA)
        #             dotMove.fill(transparent_color)

        #             pg.draw.circle(dotMove,(123,127,120),(32,32),6)
        #             self.screen.blit(dotMove, (j*68+50, i*68+50))
        
        
        COLOR = (20, 123, 104)
        ALPHA = 128
        transparent_color = COLOR + (ALPHA,)
        transparent_rect = pg.Surface((65, 65), pg.SRCALPHA)
        transparent_rect.fill(transparent_color)
        self.screen.blit(transparent_rect, (col*68+50, row*68+50))
        
        pg.display.update()

    def UnActivePiece(self):
        self.DrawChess()
        pass

    def Promote(self,row,col):
        self.promoStatus=False
        type=''
        if row==3 and col==3:type='R'
        elif row==3 and col ==4:type='N'
        elif row==4 and col ==3:type='B'
        else:type='Q'
        self.board[self.row][self.col].Promote(type,self.board)
        self.row,self.col= None,None
        self.DrawChess()
        pg.display.update()

    def MovePiece(self, row, col):
        currentPiece=self.board[self.row][self.col]
        colDict= {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h'}
        if currentPiece.GetTeam()=='White':
            self.turn='Black'
        else:
            self.turn='White'

        validMove=(row,col) in currentPiece.GetAllValidMoves(self.board)

        if validMove==False:
            self.UnActivePiece()
        else:
            piece='' if currentPiece.GetType()=='Pawn'else currentPiece.GetType()[0]
            take= 'x' if self.board[row][col]!=None else ''
            if take=='x'and piece=='':
                piece=colDict[currentPiece.col]   
            sign=str(piece+take+ str(colDict[col])+str(8-row) )
            if sign=='Kg1' or sign=='Kg7':
                self.moves.append('O-O')  
            elif sign=='Kc1' or sign== 'Kc7':
                self.moves.append('O-O-O')  
            else:
                self.moves.append(str(piece+take+ str(colDict[col])+str(8-row) ))

            currentPiece.Move(row,col,self.board)
        print(self.moves)
        self.DrawChess()
        if currentPiece.GetType()== "Pawn" and currentPiece.CheckPromotion():
            self.promoStatus= True
            self.row,self.col= row,  col
            
            team = currentPiece.GetTeam()[0].lower()
            promotionImgs=[]
            for i in range (1,5):
                promotionImgs.append(self.TransformImg(60,60,f"{team}{self.pieces[i]}promo.svg",True))
            
            COLOR = (123,111,122)
            self.promotionLayout= pg.Surface((140, 140),pg.SRCALPHA)
            self.promotionLayout.fill(COLOR +(128,))
            self.promotionLayout.blit(promotionImgs[0],(10,10))
            self.promotionLayout.blit(promotionImgs[1],(75,10))
            self.promotionLayout.blit(promotionImgs[2],(10,75))
            self.promotionLayout.blit(promotionImgs[3],(75,75))

            self.screen.blit(self.promotionLayout, (3*65+50,3*65+50))
            pg.display.update()

    def CheckWin(self):
        cnt =0
        for i in range(8):
            for j in range(8):
                if self.board[i][j]!=None and self.board[i][j].GetType()=='King':
                    cnt+=1
        if cnt <=1:
            return True
        return False
    
    def StartGame(self):
        CLOCK = pg.time.Clock()
        self.GameInitiating()

        while self.running:
    
            if self.turn=='White':
                self.whiteTime-=0.03125
            else:
                if self.mode==2:
                    self.blackTime-=0.03125
                else:
                    self.pieceInBoard = {}
                    for i in range(8):
                        for j in range(8):
                            currentPiece = self.board[i][j]
                            if currentPiece != None and currentPiece.GetTeam() == 'Black':
                                if currentPiece.GetType()[0] not in self.pieceInBoard:
                                    self.pieceInBoard[currentPiece.GetType()[0]] = [
                                        currentPiece]
                                else:
                                    self.pieceInBoard[currentPiece.GetType()[0]].append(
                                        currentPiece)

                    res  = self.AiChess.FindBestMove(self.board,' '.join(self.moves),self.pieceInBoard)
                
                    bestPiece= res[0]
                    bestMove=res[1]

                    self.row = bestPiece.row
                    self.col = bestPiece.col
                    time.sleep(1)
                    self.MovePiece(bestMove[0],bestMove[1])

            if self.splash_screen==False:
                self.DrawClock()
            for event in pg.event.get():
                if event.type == pg.QUIT or self.CheckWin():
                    self.running = False
                    pg.quit()
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    self.UserClick()

            CLOCK.tick(self.fps)

game = Chess()
game.StartGame()
