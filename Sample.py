import pygame, sys
from pygame.locals import *

pygame.init()

display_width = 1020
display_height = 768

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('My First Lady')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
LadyImg = pygame.image.load('w1.jpg')

x =  display_height/3   
y =  800  
images = ['w1.jpg','w2.jpg','w3.jpg','w4.jpg','w7.jpg','w8.jpg','w9.jpg']
counter = 0
forward = True
backward = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        # if event.type == KEYDOWN and event.key == K_LEFT:
    if(forward and y > 0):
        LadyImg = pygame.image.load(images[counter])
        print('Image' + str(counter))
        counter = (counter + 1) % len(images)
        y = y - 15
        # if event.type == KEYDOWN and event.key == K_RIGHT:
        #     LadyImg = pygame.image.load(images[counter])
        #     print('Image' + str(counter))
        #     counter = (counter + 1) % len(images)
        #     y = y + 15
        # if event.type == KEYUP and event.key == K_LEFT:
        #     LadyImg = pygame.image.load(images[counter])
        #     print('Image' + str(counter))
        #     counter = (counter + 1) % len(images)
        #     y = y - 15
        # if event.type == KEYUP and event.key == K_RIGHT:
        #     LadyImg = pygame.image.load(images[counter])
        #     print('Image' + str(counter))
        #     counter = (counter + 1) % len(images)
        #     y = y + 15
    elif(forward and y < 0):
        backward = True
        forward = False
    elif(backward and y < 900):
        LadyImg = pygame.image.load(images[counter])
        print('Image' + str(counter))
        counter = (counter + 1) % len(images)
        y = y + 15
    elif(backward and y>900):
        backward = False
        forward = True
    gameDisplay.fill(white)
    gameDisplay.blit(LadyImg, (y,x))

    pygame.display.update()
    clock.tick(3)

pygame.quit()
quit()
