import pygame
import math
import numpy as np
from pygame import mixer

pygame.init()
window=pygame.display.set_mode((700,750))
#background=(230,230,250)
background=(229,204,255)

window.fill(background)
start_over=True
pygame.display.set_caption("Connect 4")
start_font=pygame.font.SysFont('Helvetica',50)
c4_font=pygame.font.SysFont("Arial", 100, italic=True)
mainimg=pygame.image.load('mainimg.gif')
ruleimg=pygame.image.load('rules.png')

pygame.display.update()


def show_start(x,y):
    start_text=start_font.render("Start",True,(0,0,0))
    window.blit(start_text,(x,y))
def rule_img(x,y):
    window.blit(ruleimg,(x,y))

def main_img(x,y):
    window.blit(mainimg,(x,y))
def c4_text(x,y):
    c4_text_=c4_font.render("Connect-4",True,(0,0,0))
    window.blit(c4_text_,(x,y))

def play():
        window=pygame.display.set_mode((700,750))


        #variables
        number_of_rows=6
        number_of_columns=7
        size=100
        height=(number_of_rows+1)*size
        width=number_of_columns*size
        radius=int(size/2-5)
        game_over=False
        turn=1
        over_font=pygame.font.SysFont('Helvetica',80)
        drop_sound=mixer.Sound('drop.wav')
        gameover_font=pygame.font.SysFont('Helvetica',80)
        mixer.music.load('winningsound.mp3')
        cnt=0
        result=[]
        l=[]

        window=pygame.display.set_mode((700,750))
        pygame.display.set_caption("Connect 4")
        #table
        def initialise_table():
            d=np.zeros((number_of_rows,number_of_columns))
            return d

        def table_draw(board):
            for c in range(number_of_columns):
                for r in range(number_of_rows):
                    pygame.draw.rect(window, (0,0,255), (c*size,r*size+size,size,size))
                    pygame.draw.circle(window,(0,0,0),(int(c*size+size/2),int(r*size+size+size/2)),radius)

            for c in range(number_of_columns):
                for r in range(number_of_rows):
                    if board[r][c]==1:
                        pygame.draw.circle(window,(255,0,0),(int(c*size+size/2),height-int(r*size+size/2)),radius)
                    elif board[r][c]==2:
                        pygame.draw.circle(window,(255,255,0),(int(c*size+size/2),height-int(r*size+size/2)),radius)
        pygame.display.update()


        #Winning Moves 
        def winning_moves(board,piece):
            for c in range(number_of_columns-3):
                for r in range(number_of_rows):
                    if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                            return True,r,r,c,c+3
        
            for c in range(number_of_columns):
                for r in range(number_of_rows-3):
                    if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                        return True,r,r+3,c,c
            
            for c in range(number_of_columns-3):
                for r in range(number_of_rows-3):
                    if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                        return True,r,r+3,c,c+3
            
            for c in range(number_of_columns-3):
                for r in range(3,number_of_rows):
                    if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                        return True,r,r-3,c,c+3   
            return False,0,0,0,0

        pygame.display.update()

        def piece_drop(board,piece,row,col):
            board[row][col]=piece
            drop_sound.play()

        def next_row(board,col):
            for r in range(number_of_rows):
                if board[r][col]==0:
                    return r

        def valid_location(board,col):
            return board[number_of_rows-1][col]==0


        board=initialise_table()
        table_draw(board)
        pygame.display.update()

        while not game_over:
            mixer.music.play(-1)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_over=True

                if event.type==pygame.MOUSEMOTION:
                    pygame.draw.rect(window,(0,0,0),(0,0,width,size))
                    posx=event.pos[0]
                    if turn==1:
                        pygame.draw.circle(window,(255,0,0),(posx,int(size/2)),radius)
                    else:
                        pygame.draw.circle(window,(255,255,0),(posx,int(size/2)),radius)
                pygame.display.update()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(window,(0,0,0),(0,0,width,size))
                    if turn==1:
                        print(event.pos)
                        posx=event.pos[0]
                        cnt+=1
                        col=int(math.floor(posx/size))
                        if valid_location(board,col):
                            row=next_row(board,col)
                            piece_drop(board,1,row,col)
                            result=winning_moves(board,1)
                            if result[0]:
                                #pygame.draw.line(window,(0,0,0),(int(result[3]*size+size/2),height-int(result[1]*size+size/2)),(int((result[4])*size+size/2),height-int(result[2]*size+size/2)),width=15)
                                font_1=over_font.render("Red wins!!",True,(255,0,0))
                                window.blit(font_1,(150,10))
                                game_over=True
                        print(cnt)
                        pygame.display.update()
                    
                    elif(cnt>=42):
                        for i in range(number_of_rows):
                            for j in range(number_of_columns):
                                if board[i][j]!=0:
                                    font_3=gameover_font.render("Its a Tie!!",True,(255,255,0))
                                    window.blit(font_3,(150,10))
                                    game_over=True
                        pygame.display.update()

                    else:
                        posx=event.pos[0]
                        cnt+=1
                        col=int(math.floor(posx/size))
                        if valid_location(board,col):
                            row=next_row(board,col)
                            piece_drop(board,2,row,col)
                            result=winning_moves(board,2)
                            if result[0]:
                                #pygame.draw.line(window,(0,0,0),(int(result[3]*size+size/2),height-int(result[1]*size+size/2)),(int((result[4])*size+size/2),height-int(result[2]*size+size/2)),width=15)
                                font_2=over_font.render("Yellow wins!!",True,(255,255,0))
                                window.blit(font_2,(150,10))
                                game_over=True
                        print(cnt)
                        pygame.display.update()
                    
                    pygame.display.update()
                    table_draw(board)
                    turn=turn+1
                    turn=turn%2
                    pygame.draw.line(window,(0,0,0),(int(result[3]*size+size/2),height-int(result[1]*size+size/2)),(int((result[4])*size+size/2),height-int(result[2]*size+size/2)),width=15)
                    pygame.display.update()
                    if game_over:
                        pygame.time.wait(5000)

        pygame.quit()
        quit()
while start_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_over = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            play()
                
    main_img(170,30)
    c4_text(155,100)
    show_start(280,350)
    rule_img(30,450)
    pygame.display.update()

