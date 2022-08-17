
import pygame
import os, sys
from pygame.locals import *


pygame.init()
pygame.font.init()

input_map = {'move up': pygame.K_w, 'move down': pygame.K_s,
             'move right': pygame.K_d, 'move left': pygame.K_a,
             'quit': pygame.K_q, 'main menu': pygame.K_m,
             'pistol': pygame.K_1,'shotgun': pygame.K_2,
             'machine gun': pygame.K_3,'knife': pygame.K_4,
             'weapon 5': pygame.K_5,'weapon god': pygame.K_o,
             'unlim health': pygame.K_l,
             }




f = open("score.csv","r")
file_contents = f.read()
score = file_contents
name = 'harvey'
X = 1920
Y = 1080

#names of colours
WHITE = (255,255,255)
BLACK = (  0,  0,  0)
RED   = (255,  80,  80)
GREEN = (  40, 255,  25)
BLUE  = (  0,  0,255)
YELLOW = (255,255, 0)
white = (255,255,255)
clock = pygame.time.Clock()
name = ''
input_rect = pygame.Rect(200, 200, 140, 32)
active = False
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive
FONT = pygame.font.Font(None, 65)

#function that creates the button
def button_create(text, rect, inactive_color, active_color, action):
    font = pygame.font.Font(None, 40)
    button_rect = pygame.Rect(rect)
    text = font.render(text, True, BLACK)
    text_rect = text.get_rect(center=button_rect.center)
    
    return [text, text_rect, button_rect, inactive_color, active_color, action, False]


def button_check(info, event):
    text, text_rect, rect, inactive_color, active_color, action, hover = info
    if event.type == pygame.MOUSEMOTION:
        # hover = True/False   
        info[-1] = rect.collidepoint(event.pos)
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if hover and action:      
            action()

#function to draw the button on the screen
def button_draw(screen, info):
    text, text_rect, rect, inactive_color, active_color, action, hover = info
    if hover:
        color = active_color
    else:
        color = inactive_color
    pygame.draw.rect(screen, color, rect)
    screen.blit(text, text_rect)


def create_key_list(input_map):
    #A list of surfaces of the action names + assigned keys, rects and the actions.
    key_list = []
    for y, (action, value) in enumerate(input_map.items()):
        surf = FONT.render('{}: {}'.format(action, pygame.key.name(value)), True, white)
        rect = surf.get_rect(topleft=(400, y*40+50))
        key_list.append([surf, rect, action])
    return key_list

def assignment_menu(input_map):
    #Allow the user to change the key assignments in this menu.
    #The user can click on an action-key pair to select it and has to press
    #a keyboard key to assign it to the action in the `input_map` dict.    
    selected_action = None
    key_list = create_key_list(input_map)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if selected_action is not None:
                    # Assign the pygame key to the action in the input_map dict.
                    input_map[selected_action] = event.key
                    selected_action = None
                    # Need to re-render the surfaces.
                    key_list = create_key_list(input_map)
                if event.key == pygame.K_ESCAPE:  # Leave the menu.
                    # Return the updated input_map dict to the main function.
                    return input_map
            

            screen.blit(bg, (0,0))
            # Blit the action-key table. Draw a rect around the
            # selected action.
            for surf, rect, action in key_list:
                screen.blit(surf, rect)
                if selected_action == action:
                    pygame.draw.rect(screen, GREEN, rect, 2)

            pygame.display.flip()
            clock.tick(30)
            
#defines what button 1 does
def on_click_button_1():
    global stage
    stage = 'game'
    os.system("gaming.py")
    pygame.quit()
    sys.exit()

#defines what button 2 does
def on_click_button_2():
    global stage
    stage = 'options'

#defines what button 3 does
def on_click_button_3():
    global stage
    global running

    stage = 'exit'
    running = False
    pygame.quit()
    sys.exit()

#defines what button return does
def on_click_button_return():
    global stage
    stage = 'menu'

#defines what button score does
def on_click_button_score():
    global stage
    stage = 'score'
    f = open("score.csv","r")
    file_contents = f.read()
    score = file_contents


        

#defines what button scorenum
def on_click_button_scorenum():
    global stage
    stage ='score'




#defines what button controls
def on_click_button_controls():
    global stage
    stage = 'controls'
    input_map = {'controls for game,(can be changed in game)':pygame.K_ESCAPE,
             'move up': pygame.K_w, 'move down': pygame.K_s,
             'move right': pygame.K_d, 'move left': pygame.K_a,
             'quit': pygame.K_q, 'main menu': pygame.K_m,
             'pistol': pygame.K_1,'shotgun': pygame.K_2,
             'machine gun': pygame.K_3,'knife': pygame.K_4,
             'weapon 5': pygame.K_5,'weapon god': pygame.K_o,
             'unlim health': pygame.K_l,
             }

    #need fixing, needs to display it onto the screen, not just printing to shell
    inp_map = assignment_menu(input_map)
    
    print(input_map)
    
def on_click_button_control_map():
    global stage
    stage = 'controls'

       
#initialises pygame
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_rect = screen.get_rect()
bg = pygame.image.load("images/zomb_arcade.png")


    
# - objects -

stage = 'menu'

button_1 = button_create("GAME", (885, 450, 200, 75), RED,
                         BLUE, on_click_button_1)
button_2 = button_create("OPTIONS", (885, 550, 200, 75),
                         RED, BLUE, on_click_button_2)
button_3 = button_create("EXIT", (885, 750, 200, 75),
                         RED, BLUE, on_click_button_3)

button_return = button_create("RETURN", (885, 400, 200, 75),
                              RED, BLUE, on_click_button_return)
button_score = button_create("SCOREBOARD", (885, 650, 200, 75),
                             RED, BLUE, on_click_button_score)
button_scorenum = button_create("highscore is"+ score +"!", (250, 250, 500, 500),
                                RED,BLUE, on_click_button_scorenum)
button_controls = button_create("Controls", (885,650,200,75),
                                RED,BLUE, on_click_button_controls)
button_control_map = button_create("s",(885,650,200,75),
                                   RED, BLUE, on_click_button_control_map)
# - mainloop -
running = True

while running:
    screen.blit(bg, [0,0])
    # - events -
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if stage == 'menu':
            button_check(button_1, event)
            button_check(button_2, event)
            button_check(button_3, event)
            button_check(button_score,event)
        elif stage == 'game':
            button_check(button_return, event)
        elif stage == 'options':
            button_check(button_return, event)
            button_check(button_3, event)
            button_check(button_controls,event)
        elif stage == 'score':
            button_check(button_return, event)
            button_check(button_3, event)
           # button_check(button_save_score, event)
        elif stage == 'controls':
            button_check(button_return,event)
            
            
            
        #elif stage == 'exit':
    screen.blit(bg, [0,0])

    if stage == 'menu':
        button_draw(screen, button_1)
        button_draw(screen, button_2)
        button_draw(screen, button_3)
        button_draw(screen, button_score)
    elif stage == 'game':
        button_draw(screen, button_return)
    elif stage == 'options':
        button_draw(screen, button_return)
        button_draw(screen, button_3)
        button_draw(screen, button_controls)
    elif stage == 'score':
        button_draw(screen, button_return)
        button_draw(screen, button_scorenum)
        button_draw(screen, button_3)
       # button_draw(screen, button_save_score)
    elif stage == 'controls':
        button_draw(screen, button_return)
        button_draw(screen, button_controls)
    #elif stage == 'exit':
    #    pass

    pygame.display.update()

# - end -

pygame.quit()
sys.exit()
