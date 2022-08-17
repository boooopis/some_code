import pygame
import os, sys

pygame.init()

size = (1920, 1080)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
bg = pygame.image.load("images/background.jpg").convert()



    screen.blit(bg, [0,0])
