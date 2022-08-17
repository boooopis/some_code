import pygame
import sys
from pygame.locals import *

  
score = 500
pygame.init() 
clock = pygame.time.Clock() 
screen = pygame.display.set_mode([600, 500]) 
base_font = pygame.font.Font(None, 32)
name = ''  
# create rectangle
input_rect = pygame.Rect(200, 200, 140, 32)  
color_active = pygame.Color('lightskyblue3')  
color_passive = pygame.Color('chartreuse4')
color = color_passive  
active = False

  
while active == False:
    for event in pygame.event.get():
      # if user types QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True  
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            else:
                name += event.unicode   
    # it will set background color of screen
    pygame.display.flip()
    if active:
        color = color_active
    else:
        color = color_passive      
    # draw rectangle and argument passed which should be on screen
    pygame.draw.rect(screen, color, input_rect)
    text_surface = base_font.render(name, True, (255, 255, 255)) 
    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width()+10)      
    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pygame.display.flip() 
    # clock.tick(60) means that for every second at most
    # 60 frames should be passed.
    clock.tick(60)

if active == True:
    x = name[0:3]#cuts variable name to be from letters 1 - 3
    file = open('score.txt','a+')#adds to the file rather than over writting it
    f = file.write('\n')#goes to teh next line
    f = file.write(str(score))#stores score
    f = file.write(' , ')#creates a gap
    f = file.write(str(x))#stores variable x, name cut down.
    file.close

    print(x)

