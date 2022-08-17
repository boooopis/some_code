import pygame
import sys, os
import random


#sprite test
pygame.init()
size = pygame.display.set_mode((450,450))
background = pygame.image.load('images/megaman1.png').convert()
clock = pygame.time.Clock()

done = False
pygame.display.flip()

size.blit(background,(0,0))
while done == False:

    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                print('d')
                background = pygame.image.load('images/megaman8.png')
                size.blit(background,(0,0))
                if event.key == pygame.K_d:
                    print('p')
                    background = pygame.image.load('images/megaman1.png')
                    size.blit(background,(0,0))
                    clock.tick(10)
                
                
