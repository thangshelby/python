import numpy as np
import random


def reverse(mat,type):
    if type =='row':
        for i in range(0,4):
            mat[i]= mat[i][::-1]
    else:
        for i in range(0,4):
            for j in range(0,2):
                temp = mat[j][i]
                mat[j][i]= mat[3-1][i]
                mat[3-j][i]= temp
def move_left(mat):
    for i in range(0,4):
        for j in range(1,4):
            if mat[i][j]==0:
                continue
            else:
                moveJ=j
                while moveJ >0  and mat[i][moveJ-1]==0: 
                    moveJ-=1

                mat[i][moveJ]= mat[i][j]
                if moveJ!=j:
                    mat[i][j]=0
def move_right(mat):
    reverse(mat,type='row')
    move_left(mat)
    reverse(mat,type='row')

def move_up(mat):
    for i in range(0,4):
        for j in range(1,4):
            if mat[j][i]==0:
                continue
            else:
                
                moveJ=j
                while moveJ >0  and mat[moveJ-1][i]==0: 
                    moveJ-=1
                mat[moveJ][i]= mat[j][i]
                if moveJ!=j:
                    mat[j][i]=0
def move_down(mat):
    # reverse(mat,type='col')
    move_up(mat)
    reverse(mat,type='col')

def merge(mat,type):
    if type =='left' or type == 'right':
        for i in range(0,4):
            for j in range(1,4):
                while j>0 and  mat[i][j-1]==0:
                    j-=1
                if mat[i][j]==mat[i][j-1]:
                    mat[i][j-1]= mat[i][j]*2
                    mat[i][j]=0
                    if type=='left':
                        move_left(mat)
                    else:
                        move_right(mat)
    else:
        for i in range(0,4):
            for j in range(1,4):
                while j>0 and  mat[(j-1)][i]==0:
                    j-=1
                if mat[j][i]==mat[j-1][i]:
                    mat[j-1][i]= mat[j][i]*2
                    mat[j][i]=0
                    if type=='up':
                        move_up(mat)
                    else:
                        move_down(mat)

def start_game():
    mat =np.zeros((4,4,))
    # mat=[
    #     [0,0,0,0],
    #     [0,0,0,2],
    #     [0,2,2,0],
    #     [2,0,0,0], 
    #      ]
    # mat[3][2]=mat[3][1]=mat[1][0]= mat[2][0] =2
    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")

    # print(mat)
    # move_down(mat)
    # # merge(mat,'down')
    # print(mat)

    return mat



def add_new_2(mat):
    i,j= random.randint(0,3),random.randint(0,3)
    while mat[i][j] !=0:
        i= random.randint(0,3)
        j= random.randint(0,3)
    mat[i][j]= 2


def get_current_state(mat):
    if 1024 in mat:
        return "YOU WON !"
    else:
        return "TRY AGAIN !"
        
    

