import pygame as pg
import time
from pygame.locals import *
from ai import main
from main import *
import const

pg.init()
class TIC_TAC_TOE(object):
    def game_initiating_window(self):
        self.AI = main.Ai_Tic_Tac_Toe()

        self.screen= pg.display.set_mode((const.widthAndHeght),0,const.fps)
        pg.display.set_caption('Tic Tac Toe')

        boardImg=pg.image.load(const.imgLoader('board.jpg')).convert()
        backGround= pg.transform.scale(boardImg,(400,400))
        self.XImg=pg.transform.scale(pg.image.load(const.imgLoader('X.png')).convert_alpha(),(80,80))
        self.OImg=pg.transform.scale(pg.image.load(const.imgLoader('O.png')).convert_alpha(),(80,80))
        
        self.screen.blit(backGround,(0,0))
        pg.display.flip()
        self.drawStatus()

    def drawStatus(self):
        if const.winner is None:
            message = const.XO.upper() + "'s Turn"
        else:
            message = const.winner.upper() + " won !"
        if const.draw:
            message = "Game Draw !"
        font = pg.font.Font(None, 30)
 
        text = font.render(message, 1, (255, 255, 255))
    
    
        self.screen.fill((0, 0, 0), (0, 400, 500, 100))
        text_rect = text.get_rect(center=(const.width / 2, 500-50))
        self.screen.blit(text, text_rect)
        pg.display.update()
 
    def drawXO(self,row,col):
        add=5
        if col==1:
            add=12
        elif col==2:
            add=25
        const.board[row][col]=const.XO
        posx,posy=  60+add+ col*90 ,50+ row*110
        if const.XO=='x':
            self.screen.blit(self.XImg,(posx,posy))
            const.XO='o'
        else:
            self.screen.blit(self.OImg,(posx,posy))
            const.XO='x'
        self.checkStatus()
        pg.display.update()
    
    def checkStatus(self):
        print(const.board)
        for row in range(0, 3):
            if((const.board[row][0] == const.board[row][1] == const.board[row][2]) and (const.board[row][0] is not None)):
                const.winner = const.board[row][0]
                break
 
        # checking for winning columns
        for col in range(0, 3):
            if((const.board[0][col] == const.board[1][col] == const.board[2][col]) and (const.board[0][col] is not None)):
                const.winner = const.board[0][col]
                break
        # check for diagonal winners
        if (const.board[0][0] == const.board[1][1] == const.board[2][2]) and (const.board[0][0] is not None):
            # game won diagonally left to right
            const.winner = const.board[0][0]
        if (const.board[0][2] == const.board[1][1] == const.board[2][0]) and (const.board[0][2] is not None):
            # game won diagonally right to left
            const.winner = const.board[0][2]
    
        if(all([all(row) for row in const.board]) and const.winner is None):
            const.draw = True

        self.drawStatus()

    def userClick(self):
        x,y= pg.mouse.get_pos()
        if x<60 or x >340 or y <30 or y>370:
            return
        col= (x-60)//90
        row = (y-30)//110
        if row >2 or row < 0 or col >2 or col < 0:
            return
        
        self.drawXO(row,col)
    def resetGame(self):
        time.sleep(3)

        const.XO='x'
        const.winner = None
        const.draw = None
        const.board = [[None]*3, [None]*3, [None]*3]
        self.startGame()
        
  
    def startGame(self):
        clock= pg.time.Clock()
        self.game_initiating_window()
        while const.running:
            if const.XO=='o':
                print(const.board)
                AiMove=self.AI.FindBestMove(const.board)
                time.sleep(0.5)
                self.drawXO(AiMove[0],AiMove[1])
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    const.running= False
                elif event.type== pg.MOUSEBUTTONDOWN :
                    self.userClick()
                    if( const.winner or const.draw):
                        self.resetGame()
            pg.display.update()
            clock.tick(const.fps)
        # pg.quit()

game = TIC_TAC_TOE()
game.startGame()
