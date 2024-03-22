import pygame
pygame.init()

# FOR GAME
XO = 'x'
fps=30
running = True
winner = None
draw = None

# SIZE
width =400
height = 600
widthAndHeght= (width,height)
widthAndHeghtHalf= (width/2,height/2)

# COLOR
white = (255, 255, 255)
line_color = (0, 0, 0)
board = [[None]*3, [None]*3, [None]*3]

# start= 60
# h=110
# w=90  
