import random   
import sys  
import pygame as pg 
import os 
from pygame.locals import * 
import const

pg.init()
class FLAPPY_BIRD(object):
    def GameInitiating(self) -> None:
        self.screen = pg.display.set_mode((const.width,const.height),0,32)
        pg.display.set_caption('Flappy Bird')
        
        # INIT IMG
        self.backGroundImg= self.TransformImg(const.width,const.height,'background.jpg',False)
        self.baseImg= self.TransformImg(const.width,100,'base.jfif',False)
        self.birdImg= self.TransformImg(60,60,'bird.png',True)
        self.scoresImg=[]
        for i in range(10):
            self.scoresImg.append(pg.image.load( self.LoadImg(f"{i}.png")).convert_alpha() )
        
        self.screen.blit(self.scoresImg[0],(10,20))
        pg.display.update()
        self.birdX,self.birdY= 150,200   
        
        self.pipeImgs=[]
        self.pipeXCoor=[]
        self.pipeYCoor=[]
        self.scores=[[0,0]]
        self.screen.blit(self.backGroundImg,(0,0))
        self.screen.blit(self.baseImg,(0,400))
        self.screen.blit(self.birdImg,(40,250))   
        self.pipeWidth= 150

 
        pg.display.flip()

    def LoadImg(self,path):
        return os.path.join('img',path)
    def TransformImg(self,width,height,path,alpha):
        if alpha:
            return  pg.transform.scale(pg.image.load(self.LoadImg(path)).convert_alpha(),(width,height))
        else:
            return  pg.transform.scale(pg.image.load(self.LoadImg(path)).convert(), (width,height) )
    def CreatePipe(self):
        pipeHeight= random.randint(100,300)
        self.gapHeight=100

        pipeImg= self.TransformImg(150,pipeHeight,'pipe.png',True)
        pipeReverseImg= pg.transform.flip(self.TransformImg(150,500-pipeHeight-self.gapHeight,'pipe.png',True),True,True)

        self.pipeImgs.append([pipeImg,pipeReverseImg])
        self.pipeXCoor.append([700,700])
        self.pipeYCoor.append([500-pipeHeight,0])
    def GameOver(self):
        if self.birdX>= self.pipeXCoor[0][0] and self.birdX<= self.pipeXCoor[0][0]+150:
            if self.birdY >= self.pipeYCoor[0][0] or self.birdY <= self.pipeYCoor[0][0]-self.gapHeight :
                self.StartGame()
        elif self.birdY>=350:
            self.StartGame()
    def StartFlappyGame(self):
        self.birdVDown=3
        self.birdVUp= -25
        self.birdFlap=False
        self.pipeV=-3
        
        
        self.CreatePipe()
    
        while const.running:

            # CHECK GAME OVER
            self.GameOver()

            # CREATE NEW PIPE
            if self.pipeXCoor[0][0]<350:
                self.CreatePipe()
                
            # REMOVE PIPE
            if self.pipeXCoor[0][0]<30:
                self.pipeImgs.pop(0)
                self.pipeXCoor.pop(0)
                self.pipeYCoor.pop(0)
                
                self.scores[0][1]+=1
                if self.scores[0][1]==10:
                    self.scores[0][1]=0
                    self.scores[0][0]+=1



            # UPDATE SCORES
           
            
            self.screen.blit(self.backGroundImg,(0,0))
            self.screen.blit(self.baseImg,(0,400))
            self.screen.blit(self.scoresImg[self.scores[0][0]],(50,20) )
            self.screen.blit(self.scoresImg[self.scores[0][1]],(80,20) )
        
            # PIPE1
            self.screen.blit(self.pipeImgs[0][0],(self.pipeXCoor[0][0],self.pipeYCoor[0][0]))
            self.screen.blit(self.pipeImgs[0][1],(self.pipeXCoor[0][1],self.pipeYCoor[0][1]))
            self.pipeXCoor[0][0]+=self.pipeV
            self.pipeXCoor[0][1]+=self.pipeV

            # if self.birdX>self.pipeXCoor[0][0]:

            #     self.scores[0][1]=  self.scores[0][1]+1
            
            # PIPE2
            if len(self.pipeImgs)>1:
                self.screen.blit(self.pipeImgs[1][0],(self.pipeXCoor[1][0],self.pipeYCoor[1][0]))
                self.screen.blit(self.pipeImgs[1][1],(self.pipeXCoor[1][1],self.pipeYCoor[1][1]))
                self.pipeXCoor[1][0]+=self.pipeV
                self.pipeXCoor[1][1]+=self.pipeV
            
            
            pg.display.update()

            for event in pg.event.get():
                if event.type== pg.QUIT:
                    const.running= False
                    pg.quit()
                    sys.exit()
                elif event.type== KEYDOWN and (event.key==K_SPACE or event.key== K_UP):
                    self.birdFlap=True
                    self.birdY+=self.birdVUp
                    self.screen.blit(self.birdImg,(self.birdX,self.birdY))
                    pg.display.update()
                    pg.time.Clock().tick(const.fps)
        
            if self.birdFlap==False:
                self.birdY+=self.birdVDown
                self.screen.blit(self.birdImg,(self.birdX,self.birdY))
                pg.display.update() 
                pg.time.Clock().tick(const.fps)

            self.birdFlap= False
        
                 
                    


        
        self.screen.blit(self.birdImg,(self.birdX,self.birdY))
        pg.display.update()


    def StartGame(self):
        self.GameInitiating()
        # self.CreatePipeImg()
        while const.running:
            for event in pg.event.get():
                if event.type== pg.QUIT:
                    const.running= False
                    pg.quit()
                    sys.exit()
                
                elif event.type== KEYDOWN and (event.key==K_SPACE or event.key== K_UP):
                    self.StartFlappyGame()
                else:
                    self.screen.blit(self.backGroundImg,(0,0))
                    self.screen.blit(self.baseImg,(0,400))
                    self.screen.blit(self.birdImg,(self.birdX,self.birdY))
                    pg.display.update()
                    pg.time.Clock().tick(const.fps)

game=FLAPPY_BIRD()


game.StartGame()
