import pygame
import time
import random
from random import randint

pygame.init()
dis = pygame.display.set_mode((600,600))
pygame.display.update()
pygame.display.set_caption("Snake Game by Libuntu v2.3")
snake_face = pygame.image.load("C:\smile.png")
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
black =(0,0,0)
green  = (34,145,64)
game_over = False
x = 300
y = 300
snake_block = 20
x_change = 0
y_change = 0
skor = 0
pygame.draw.line(dis, (0, 0, 0), [300, 300], [500, 600], 5)
 
def snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

clock = pygame.time.Clock()

yem_x = random.randint(20, 580)
yem_y = random.randint(20, 580)

def drawYem():
    pygame.draw.rect(dis, blue, [yem_x, yem_y, 15, 15])

def skor_txt(msg,color):
    mesg = pygame.font.SysFont(None, 30).render(msg, True, color)
    dis.blit(mesg, [20, 20])

def mesaj(msg,color):
    mesg = pygame.font.SysFont(None, 100).render(msg, True, color)
    dis.blit(mesg, [90, 250])

snake_list = []
snake_len = 1

while not game_over:
    pygame.draw.line(dis, black, [0, 0], [0, 600], 10)
    pygame.draw.line(dis, black, [0, 0], [600, 0], 10)
    pygame.draw.line(dis, black, [600, 0], [600, 600], 10)
    pygame.draw.line(dis, black, [0, 600], [600, 600], 10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_block
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = snake_block
                y_change = 0 
            if event.key == pygame.K_UP:
                y_change = -snake_block
                x_change = 0
                #pygame.event.set_allowed(pygame.K_RIGHT)
            if event.key == pygame.K_DOWN:
                y_change = snake_block
                x_change = 0


    #if x > 590 or x < 10 or y > 590 or y < 10:
        #game_over = True

    if x == 0:
        x = 600
    if x == 620:
        x = 0
    if y == 0:
        y = 600
    if y == 620:
        y = 0
    x += x_change
    y += y_change

    skor_txt("Skorun: " + str(skor), white)
    drawYem()
    dis.blit(snake_face, (x,y))
    #pygame.draw.rect(dis, white,[x, y, snake_block, snake_block])

    if  x + 15 > yem_x and x - 15 < yem_x and y - 15 < yem_y and y + 15 > yem_y:
        skor += 1
        snake_len += 1
        yem_x = random.randint(20, 580)
        yem_y = random.randint(20, 580)
        drawYem()
    pygame.display.update()
    dis.fill(green)
    snake_head = []
    snake_head.append(x)
    snake_head.append(y)
    snake_list.append(snake_head)

    if len(snake_list) > snake_len:
        del snake_list[0]
    for x1 in snake_list[:-1]:
        if x1 == snake_head:
            game_over = True   
    
    snake(snake_block, snake_list)
    
    if  0 <= skor < 5:
        clock.tick(5)
    if 5 <= skor < 10:
        clock.tick(7)
    if 10 <= skor < 15:
        clock.tick(10)
    if 15 <= skor < 25:
        clock.tick(13) 
    if 25 <= skor < 35:
        clock.tick(16)
    if 35 <= skor:
        clock.tick(20) 

skor_txt("Skorun: " + str(skor), white)        
mesaj("GAME OVER",white)
pygame.display.update()
time.sleep(5)
pygame.quit()
quit()