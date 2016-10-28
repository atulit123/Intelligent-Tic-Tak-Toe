import pygame,sys
from pygame.locals import *
import random
pygame.init()
WINDOWWIDTH=440
GRIDWIDTH=80
GRIDORIGIN=(WINDOWWIDTH-3*GRIDWIDTH)/2
BGCOLOR=((230,241,222))
GDCOLOR=((72,203,51))
LNCOLOR=((13,31,10))
ZERO=pygame.image.load("zero.png")
CROSS=pygame.image.load("cross.png")
assert (WINDOWWIDTH>GRIDWIDTH), "Not possible to draw the window"
clk=pygame.time.Clock()
Display_surf=pygame.display.set_mode((WINDOWWIDTH,WINDOWWIDTH),0,32)
pygame.display.set_caption("Tic Tak Toe")
Display_surf.fill(BGCOLOR)
zero = pygame.image.load('zero.png')
fontObj = pygame.font.Font('freesansbold.ttf', 26)
textSurfaceObj = fontObj.render('create New', True, (0,255,0), (0,0,255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center=(150,50)
current_mov='min'
## to get grid Number
def get_grid(pos):
    global GRIDORIGIN,GRIDWIDTH
    x,y=pos
    if x<GRIDORIGIN or y<GRIDORIGIN or x>GRIDORIGIN+3*GRIDWIDTH or y>GRIDORIGIN+3*GRIDWIDTH:
        return False
    x_grid=(x-GRIDORIGIN)/GRIDWIDTH
    y_grid=(y-GRIDORIGIN)/GRIDWIDTH
    return (x_grid,y_grid)

###to get the coordinates of Grid
def get_grid_coords(pos):
    global GRIDORIGIN,GRIDWIDTH
    x_grid,y_grid=pos
    x,y=GRIDORIGIN+x_grid*GRIDWIDTH,GRIDORIGIN+y_grid*GRIDWIDTH
    return (x,y)

###to draw the grid
def draw(Display_surf):
    global GRIDORIGIN,GRIDWIDTH,BGCOLOR,LNCOLOR,GDCOLOR,textSurfaceObj,textRectObj
    Display_surf.fill(BGCOLOR)
    Display_surf.blit(textSurfaceObj,textRectObj)
    pygame.draw.rect(Display_surf,GDCOLOR,(GRIDORIGIN,GRIDORIGIN,3*GRIDWIDTH,3*GRIDWIDTH))
    for i in range(4):
        ##vertical lines
        x1,y1=GRIDORIGIN+i*GRIDWIDTH,GRIDORIGIN
        x2,y2=GRIDORIGIN+i*GRIDWIDTH,GRIDORIGIN+3*GRIDWIDTH
        pygame.draw.line(Display_surf,LNCOLOR,(x1,y1),(x2,y2),1)
        pygame.display.update()
        clk.tick(4)
    
    for i in range(4):
        ##horizintal lines
        y1,x1=GRIDORIGIN+i*GRIDWIDTH,GRIDORIGIN
        y2,x2=GRIDORIGIN+i*GRIDWIDTH,GRIDORIGIN+3*GRIDWIDTH
        pygame.draw.line(Display_surf,LNCOLOR,(x1,y1),(x2,y2),1)
        pygame.display.update()
        clk.tick(4)

##to check for matching
def  check_for_win(grid_array):
    ## ceck for horizontal matching
    for i in range(3):
        if grid_array[i][0]==grid_array[i][1] and grid_array[i][1]==grid_array[i][2]  and grid_array[i][2] !='N':
            return ((0,i),'h')
    ## check for vertical matching
    for i in range(3):
        if grid_array[0][i]==grid_array[1][i] and grid_array[1][i]==grid_array[2][i] and grid_array[1][i] !='N':
            return ((i,0),'v')
    ## check for diagonal matching
    if grid_array[0][0]==grid_array[1][1] and grid_array[1][1]==grid_array[2][2] and grid_array[1][1] !='N':
        return ((0,0),'dr')
    if grid_array[2][0]==grid_array[1][1] and grid_array[0][2]==grid_array[1][1] and grid_array[0][2] !='N':
        return ((2,0),'dl')
    return False
def check_win_move(grid_array,ply):
    ## ceck for horizontal matching
    for i in range(3):
        if grid_array[i][0]==grid_array[i][1] and grid_array[i][1]==grid_array[i][2]  and grid_array[i][2] ==ply:
            return True
    ## check for vertical matching
    for i in range(3):
        if grid_array[0][i]==grid_array[1][i] and grid_array[1][i]==grid_array[2][i] and grid_array[1][i] ==ply:
            return True
    ## check for diagonal matching
    if grid_array[0][0]==grid_array[1][1] and grid_array[1][1]==grid_array[2][2] and grid_array[1][1] ==ply:
        return True
    if grid_array[2][0]==grid_array[1][1] and grid_array[0][2]==grid_array[1][1] and grid_array[0][2]==ply:
        return True
    return False
###for drawing cross or zer0
def draw_zx(x,y,image,Display_surf):
     Display_surf.blit(image,(x,y))
draw(Display_surf)
def handler(grid_array,pos,play,Display_surf):
    global ZERO,CROSS,current_mov
    if  check_for_win(grid_array):
        return False
    if  get_grid(pos) and current_mov=='min':
        x_grid,y_grid=get_grid(pos)
        if grid_array[y_grid][x_grid]=='N':
            grid_array[y_grid][x_grid]='X'
            image=CROSS
            x,y=get_grid_coords((x_grid,y_grid))
            draw_zx(x,y,image,Display_surf)
            current_mov='max'
            return True
    elif current_mov=='max':
        grid_array,move,val=play_zero(grid_array)
        y_grid,x_grid=move
        image=ZERO
        x,y=get_grid_coords((x_grid,y_grid))
        draw_zx(x,y,image,Display_surf)
        current_mov='min'
        return True
    return False
def computer_hand(grid_array):
    global current_mov
    if  check_for_win(grid_array):
        return False
    grid_array,move,val=play_zero(grid_array)
    y_grid,x_grid=move
    image=ZERO
    x,y=get_grid_coords((x_grid,y_grid))
    draw_zx(x,y,image,Display_surf)
    current_mov='min'
    return True
def win_animation(grid_win):
    global GRIDWIDTH,Display_surf,clk
    x_grid,y_grid=grid_win[0]
    type_win=grid_win[1]
    x,y=get_grid_coords((x_grid,y_grid))
    if type_win=='h':
        y=y+GRIDWIDTH/2
        for i in range(3*GRIDWIDTH):
            pygame.draw.line(Display_surf,(164,2,78),(x,y),(x+i,y),3)
            pygame.display.update()
            clk.tick(120)
    if type_win=='v':
        x=x+GRIDWIDTH/2
        for i in range(3*GRIDWIDTH):
            pygame.draw.line(Display_surf,(164,2,78),(x,y),(x,y+i),3)
            pygame.display.update()
            clk.tick(120)
    if type_win=='dr':
        for i in range(3*GRIDWIDTH):
            pygame.draw.line(Display_surf,(164,2,78),(x,y),(x+i,y+i),3)
            pygame.display.update()
            clk.tick(120)
    if type_win=='dl':
        x=x+GRIDWIDTH
        for i in range(3*GRIDWIDTH):
            pygame.draw.line(Display_surf,(164,2,78),(x,y),(x-i,y+i),3)
            pygame.display.update()
            clk.tick(120)
def is_draw(grid_array):
    for row in grid_array:
        if 'N' in row:
            return False
    return True
def empty_slots(grid_array):
    slots=[]
    for i in range(3):
        for j in range(3):
           if grid_array[i][j]=='N':
               slots.append((i,j))
    if len(slots)==2:
        slots.reverse()
    else:random.shuffle(slots)
    return slots 
###returns new board and move
def play_x(board):
    if  is_draw(board):
        return board,(-1,-1),0
    elif check_win_move(board, 'X'):
        return board,(-1,-1),-1
    elif check_win_move(board,'Z'):
        return board,(-1,-1),1
    minm=100
    req_move=None
    for move in empty_slots(board):
        i,j=move
        new_board=[a[:] for a in board]
        new_board[i][j]='X'
        a,b,value=play_zero(new_board)
        if value<minm:
            minm=value
            req_move=(i,j)
    i,j=req_move
    board[i][j]='Z'
    return board,req_move,minm
def play_zero(board):
    if  is_draw(board):
        return board,(-1,-1),0
    elif check_win_move(board, 'Z'):
        return board,(-1,-1),1
    elif check_win_move(board,'X'):
        return board,(-1,-1),-1
    maxm=-10
    req_move=None
    for move in empty_slots(board):
        i,j=move
        new_board=[a[:] for a in board]
        new_board[i][j]='Z'
        a,b,value=play_x(new_board)
        if value>maxm:
            maxm=value
            req_move=(i,j)
    i,j=req_move
    board[i][j]='Z'
    return board,req_move,maxm
play=0               
grid_array=[['N' for i in range(3)] for j in range(3)]


while True:
    grid_win=check_for_win(grid_array)
    if grid_win:
        win_animation(grid_win)
        pygame.time.wait(2000)
        grid_array=[['N' for i in range(3)] for j in range(3)]
        draw(Display_surf)
        pygame.event.clear()
    grid_draw=is_draw(grid_array)
    if grid_draw:
        pygame.time.wait(2000)
        grid_array=[['N' for i in range(3)] for j in range(3)]
        draw(Display_surf)
        pygame.event.clear()
    if current_mov=='max':
        computer_hand(grid_array)
        pygame.event.clear()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==MOUSEBUTTONUP:
            if textRectObj.collidepoint(event.pos[0],event.pos[1]):
                grid_array=[['N' for i in range(3)] for j in range(3)]
                draw(Display_surf)
            else:
                handler(grid_array,event.pos,play,Display_surf)
    pygame.display.update()
    clk.tick(24)

    
    
