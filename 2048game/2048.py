from logic import *


class GAME_2048(object):
    mat= start_game()
    while(1):

        print(mat)
        currentState= get_current_state(mat)
        if "WON" in currentState:
            print(currentState)
            break
        

        move= input('Press key to move:')
        if move== 'a'or move=='A':
            move_left(mat)
            merge(mat,'left')
            add_new_2(mat)
        elif move=='d' or move=='D':
            move_right(mat)
            merge(mat,'right')
            add_new_2(mat)
        elif move=='w' or move=='W':
            move_up(mat)
            merge(mat,'up')
            add_new_2(mat)
        elif move=='s' or move=='S':
            move_down(mat)
            merge(mat,'down')
            add_new_2(mat)
        else:
            print("Not valid synxtax.Please try again !")
      
        
if __name__=='2048.py':
    GAME_2048.start_game()