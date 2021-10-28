from random import randint
from datetime import datetime
import time

def display_board():
    for i in range(0,3):
        for j in range(0,3):
            print(game[i][j],end='')
        print()
    print()

def check_valid(r, c):
    if 0<=r<=2 and 0<=c<=2:
        return True
    else:
        return False

def is_empty(r, c):
    if game[r][c]=='-':
        return True
    else:
        return False
    
def selection(xo):
    while True:
        print('Player ',xo,' Turn')
        r=int(input("Row : "))
        c=int(input("Col : "))
        if check_valid(r,c):
            if is_empty(r,c):
                game[r][c] = xo
                return
            else:
                print('This cell in not empty, try again')
        else:
            print('row and col must bi between 0 and 2, try again')    
    
    
def check_winner():
    for i in range(0,3):
        cx,co=0,0 
        for j in range(0,3):
            if game[i][j]=='X':
                cx+=1
            elif game[i][j]=='O':
                co+=1
        if cx==3:
            print('---- Player X Won! ----')
            return True
        elif co==3:
            print('---- Player O Won! ----')
            return True
        
        
    for i in range(0,3):
        cx,co=0,0
        for j in range(0,3):
            if game[j][i]=='X':
                cx+=1
            elif game[j][i]=='O':
                co+=1
        if cx==3:
            print('---- Player X Won! ----')
            return True
        elif co==3:
            print('---- Player O Won! ----')
            return True
        
        
    if (game[0][0]==game[1][1]==game[2][2]=='X') or (game[0][2]==game[1][1]==game[2][0]=='X') :
        print('---- Player X Won! ----')
        return True
    elif (game[0][0]==game[1][1]==game[2][2]=='O') or (game[0][2]==game[1][1]==game[2][0]=='O'):
        print('---- Player O Won! ----')
        return True
    return False
    
def game_draw():
    for i in range(0,3):
        for j in range(0,3):
            if game[i][j]=='-':
                return False
    print('---- Draw! ----')
    return True

def plvpl():
    while True:
        display_board()
        xo='X'
        selection(xo)
        if check_winner() or game_draw():
            display_board()
            return
        display_board()   
        xo='O'
        selection(xo)
        if check_winner() or game_draw():
            display_board()
            return

def pc_play():
    print('Player O Turn')
    while True:
        
        r=randint(0,2)
        c=randint(0,2)
        if check_valid(r,c):
            if is_empty(r,c):
                game[r][c]='O'
                print('Row : ',r)
                print('Col : ',c)
                return

def plvpc():
    while True:
        display_board()
        xo='X'
        selection(xo)
        if check_winner() or game_draw():
            display_board()
            return
        pc_play()
        if check_winner() or game_draw():
            display_board()
            return
            
#######################################################################

while True:
    game=[[ '-' , '-' , '-'],
          [ '-' , '-' , '-'],
          [ '-' , '-' , '-']]
    
    sel=int(input('1.Player VS Pc\n2.Player VS Player\n3.exit\nSelection : '))

    if sel==1:
        x=time.time()
        plvpc()
        y=time.time()
        print('Game Time : ',y-x)
        
        
       
    elif sel==2:
        x=time.time()
        plvpl()
        y=time.time()
        print('Game Time : ',y-x)
        
    elif sel==3:
        break 
        



