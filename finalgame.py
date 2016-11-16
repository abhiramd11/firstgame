
import pygame
import time
import random
from random import randint
pygame.init()

green=(0,255,0)
red=(255,0,0)
black=(0,0,0)
blue=(0,0,255)

dis_w=400
dis_h=400
fps = 30
bsize = 50

#positions for the enemy blocks
y=100
a=100
b=200
c=50



gmdis=pygame.display.set_mode((dis_w,dis_h))
player_img=pygame.image.load("fighter.png")

pygame.display.set_caption('THE GAME')

pygame.display.update()

clk=pygame.time.Clock()

font=pygame.font.SysFont(None,20)

def screen_msg(msg,colour,xpos,ypos):
    screen_txt=font.render(msg,True,colour)
    gmdis.blit(screen_txt,[dis_w/2 - 150+xpos,dis_h/2-ypos])   #-150 simply to position the text


def gameloop():
    gxit = False
    gameover=False

    green = (0, 255, 0)
    red = (255, 0, 0)
    black = (0, 0, 0)
    blue = (0, 0, 255)

    dis_w = 400
    dis_h = 400
    fps = 10
    bsize = 50

    y = 50
    c = 50
    n = 50
    a = 0
    b = 0
    m = 0

    xdir = dis_w / 2
    xdir_change = 0
    ydir = dis_h-50
    ydir_change = 0
    score=0
    en1 = 0
    en2 = 0
    en3 = 0

    while not gxit:
        while gameover==True:

            gmdis.fill(black)
            screen_msg("GAME OVER, Press r to restart or q to quit", red, 0, 0)
            pygame.display.update()

            for x in pygame.event.get():
                if x.type == pygame.KEYDOWN:
                    if x.key == pygame.K_q:
                        gxit = True
                        gameover = False
                    if x.key == pygame.K_r:
                        gameloop()

        for x in pygame.event.get():
            if x.type==pygame.QUIT:
                gxit=True
            if x.type==pygame.KEYDOWN:
                if x.key==pygame.K_a:
                    xdir_change = -bsize
                    ydir_change = 0
                elif x.key == pygame.K_d:
                    xdir_change = bsize
                    ydir_change = 0
                elif x.key == pygame.K_w:
                    xdir_change = 0
                    ydir_change = -bsize
                elif x.key == pygame.K_s:
                    xdir_change = 0
                    ydir_change = bsize
            if x.type==pygame.KEYUP:
                if x.key==pygame.K_a or x.key==pygame.K_d or x.key==pygame.K_w or x.key==pygame.K_s:
                    xdir_change=0
                    ydir_change=0

        if xdir>dis_w-bsize or xdir<0 or ydir>dis_h-bsize or ydir<0:
            gameover=True

        xdir+=xdir_change
        ydir+=ydir_change
        gmdis.fill(black)
        gmdis.blit(player_img,(xdir,ydir))

        y = y + 25       #random.randrange(1,20,10)
        c = c + 25        #random.randrange(1,20,10)
        n = n + 25        #random.randrange(1,20,10)
        if y > 400:
            a = random.randrange(0,dis_w-bsize, 50)
            y = 0
            score+=1
        if c > 400:
            b = random.randrange(0,dis_w-bsize, 50)
            c = 0
            score+=1
        if n > 400:
            m = random.randrange(0,dis_w-bsize, 50)
            n = 0
            score+=1
        elif ((a==xdir and y==ydir) or (b==xdir and c==ydir) or (m==xdir and n==ydir)):
            gameover=True
        pygame.draw.rect(gmdis, red, [a, y, bsize, bsize])
        pygame.draw.rect(gmdis, blue, [b, c, bsize, bsize])
        pygame.draw.rect(gmdis, green, [m, n, bsize, bsize])
        pygame.display.update()

        screen_msg("score : "+str(score), red,250,180)
        pygame.display.update()
        clk.tick(fps)

    pygame.quit()
    quit()


gameloop()




