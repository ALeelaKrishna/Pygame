import pygame, sys
from pygame.locals import *

pygame.init()

display_width = 1920
display_height = 1020

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('My First Lady')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False

LadyImg = pygame.image.load('w1.jpg')
Fridge = pygame.image.load('fridge.png')
Fridge = pygame.transform.scale(Fridge, (250,250))

count = 0
pygame.font.init()

#SysFont(FONT TYPE,SIZE)
myfont = pygame.font.SysFont('Comic', 25)

W_Y =  display_height/3   
W_X =  1  
images = ['w1.jpg','w2.jpg','w3.jpg','w4.jpg','w7.jpg','w8.jpg','w9.jpg']
imagesr = ['w1r.jpg','w2r.jpg','w3r.jpg','w4r.jpg','w7r.jpg','w8r.jpg','w9r.jpg']
counter = 0
W_Right = True

while count!=5:
    # for event in pygame.event.get():
    #     if event.type == KEYDOWN and event.key == K_q:
    #         crashed = True
    counter = (counter + 1) % len(images)
    if(W_Right and W_X > display_width/3):
        W_Right = False
        count = count + 1

    elif(not W_Right and W_X < 10):
        W_Right = True

    elif(W_Right and W_X < display_width/3):
        LadyImg = pygame.image.load(imagesr[counter])
        W_X = W_X + 15
        # print(y)

    elif(not W_Right and W_X > 0):
        LadyImg = pygame.image.load(images[counter])
        W_X = W_X - 15
        # print(y)
    
    
    # LadyImg = pygame.image.load(images[counter])
    # print('Image' + str(counter))

    #RENDER(TEXT,ANTI ALIASING,COLOR)
    textsurface = myfont.render('Apples: '+ str(count), True, (173, 0, 0))
    gameDisplay.fill(white)
    
    #BLIT(OBJECT(text,image....etc),POSITION)
    gameDisplay.blit(LadyImg, (W_X,W_Y))
    gameDisplay.blit(Fridge,(display_width/3 ,W_Y-50))
    gameDisplay.blit(textsurface,(display_width/3+90,W_Y-5))

    pygame.display.update()
    
    #number of frames
    clock.tick(5)

pygame.quit()
quit()