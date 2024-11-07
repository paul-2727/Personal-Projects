import pygame
import random
from sys import exit

pygame.init()

window = pygame.display.set_mode((1920,1080)) 
pygame.display.set_caption("Python Hehehe")
blue  = (0  ,0  ,255) #RGB
green = (0  ,255,0  ) #RGB
red   = (255,0  ,0  ) #RGB
black = (0  ,0  ,0  ) #RGB
white = (255,255,255) #RGB
clock=pygame.time.Clock()
gameover=True
s_x=300
s_y=200
m_x=360
m_y=200
x_change=0
y_change=0
snake_list=[]
maxlenght=1
snakespeed=10
score=-1
font = pygame.font.Font(None, 36)
score_surface = font.render("Score: {}".format(score), True, white) 
score_rect = score_surface.get_rect(center=(300, 200))
start=True
def game():
    gameover=True
    s_x=300
    s_y=200
    m_x=360
    m_y=200
    x_change=0
    y_change=0
    snake_list=[]
    maxlenght=1
    snakespeed=10
    score=-1
    font = pygame.font.Font(None, 36)
    score_surface = font.render("Score: {}".format(score), True, white) 
    score_rect = score_surface.get_rect(center=(300, 200))
    def restart():
        global gameover, s_x, s_y, m_x, m_y, x_change, y_change, snake_list, maxlenght, snakespeed, score,start
        start=True
        gameover = True
        s_x = 300
        s_y = 200
        m_x = 360
        m_y = 200
        x_change = 0
        y_change = 0
        snake_list = []
        maxlenght = 1
        snakespeed = 10
        score = -1
        window.fill(pygame.Color("black"))
        font_surface = font.render("Score: {}".format(score), True, pygame.Color("white"))
        window.blit(score_surface, (0, 0))
        game()
    def destructorsnake(snake_list):
        for x in snake_list:
            pygame.draw.rect(window,green,[x[0],x[1],10,10])
    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-10
                    y_change=0
                if event.key==pygame.K_RIGHT:
                    x_change=10
                    y_change=0
                if event.key==pygame.K_UP:
                    x_change=0
                    y_change=-10
                if event.key==pygame.K_DOWN:
                    x_change=0
                    y_change=10
                if event.key == pygame.K_r:
                    restart()
        s_x+=x_change
        s_y+=y_change
        window.fill(black)
        pygame.draw.rect(window,red,[m_x,m_y,10,10])
        snake_Head=[]
        snake_Head.append(s_x)
        snake_Head.append(s_y)
        snake_list.append(snake_Head)
        if len(snake_list)>maxlenght:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x== snake_Head:
                gameover=False
        
        destructorsnake(snake_list)
    
        if s_x > 600 or s_x < 0:
            gameover=False
        if s_y > 400 or s_y< 0:
            gameover=False    
    
        pygame.display.update()

        if s_x == m_x and s_y == m_y:
            maxlenght+=1
            snakespeed+=1
            m_x=round(random.randrange(10,510)/10.0)*10.0
            m_y=round(random.randrange(10,390)/10.0)*10.0
        if snakespeed>=60:
            snakespeed=60
        clock.tick(snakespeed)

    while gameover==False:
        score=maxlenght-1
        score_surface = font.render("Score: {}".format(score), True, white) 
        window.fill(black)
        window.blit(score_surface, score_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_r:
                    restart()

        pygame.display.update()
        clock.tick(60)
while start:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            start=False
    pygame.display.update()
    clock.tick(60)
    game()