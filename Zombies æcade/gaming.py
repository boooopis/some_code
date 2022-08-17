# -*- coding: utf-8 -*-

#445'maingame', 280'mainmenu', 184'weapon', 32'projectile', 71'player', 60'enemy'
#1072 all

#score saving and loading system brokey need fix, fix then pretty much done 
#try to keep game running wean lives are gone, then make score save there and then end game

import pygame
import random
import os, sys
import pdb
from Player import Player
from Enemy import Enemy
from Projectile import Projectile
from pygame.locals import *
from time import sleep


#this section is creating the players screen size, background color and displaying
#the players health
pygame.init()
pygame.font.init()
size    = (1920, 1080)
BGCOLOR = (255, 255, 255)
screen = pygame.display.set_mode((1920,1080))
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
scoreFont = pygame.font.Font("fonts/UpheavalPro.ttf", 30)
enemFont = pygame.font.Font("fonts/UpheavalPro.ttf", 30)
healthFont = pygame.font.Font("fonts/OmnicSans.ttf", 50)
healthRender = healthFont.render('z', True, pygame.Color('red'))
pygame.display.set_caption("zombies arcade")
bg = pygame.image.load("images/background.jpg").convert()
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
FONT = pygame.font.Font(None, 65)


WeaponGui = ['images/megaman1.png','images/megaman2.png',
              'images/megaman3.png','images/megaman4.png',
              'images/megaman5.png','images/megaman6.png',
              'images/megaman7.png','images/megaman8.png']
bulletpicture = pygame.image.load("images/megaman2.png").convert_alpha()

done = False
hero = pygame.sprite.GroupSingle(Player(screen.get_size()))
enemies = pygame.sprite.Group()
lastEnemy = 0
score = 0
clock = pygame.time.Clock()

input_rect = pygame.Rect(200, 200, 140, 32)  
color_active = pygame.Color('lightskyblue3')  
color_passive = pygame.Color('chartreuse4')
color = color_passive 
base_font = pygame.font.Font(None, 32)

input_map = {'move up': pygame.K_w, 'move down': pygame.K_s,
             'move right': pygame.K_d, 'move left': pygame.K_a,
             'quit': pygame.K_q, 'main menu': pygame.K_m,
             'pistol': pygame.K_1,'shotgun': pygame.K_2,
             'machine gun': pygame.K_3,'knife': pygame.K_4,
             '?': pygame.K_5,'weapon god': pygame.K_o,
             'unlim health': pygame.K_l,'change character': pygame.K_p,
             }#holds the name of the function and what key does it,
              #so the user can change it later in the game

player_sprites = ['images/megaman1.png','images/megaman2.png']

#plays music file on loop until the end of the game

music = pygame.mixer.music.load("jumpe_monke.mp3")
pygame.mixer.music.play(-1)



                





#this will allow the player to kill enimies and allow them to move
def move_entities(hero, enemies, timeDelta):
    score = 0
    hero.sprite.move(screen.get_size(), timeDelta)
    for enemy in enemies:
        enemy.move(enemies, hero.sprite.rect.topleft, timeDelta)
        enemy.shoot(hero.sprite.rect.topleft)
    for proj in Enemy.projectiles:
        proj.move(screen.get_size(), timeDelta)
        if pygame.sprite.spritecollide(proj, hero, False):
            proj.kill()
            hero.sprite.health -= 1
            if hero.sprite.health == 0:
                hero.sprite.alive = False
    for proj in Player.projectiles:
        proj.move(screen.get_size(), timeDelta)
        enemiesHit = pygame.sprite.spritecollide(proj, enemies, True)
        if enemiesHit:
            proj.kill()
            score += len(enemiesHit)
    return score
#this renders in the enimies and the enimies projectiles
def render_entities(hero, enemies):
    hero.sprite.render(screen)
    for proj in Player.projectiles:
        proj.render(screen)
    for proj in Enemy.projectiles:
        proj.render(screen)
    for enemy in enemies:
        enemy.render(screen)



#this allows the user to move the player where they want to    

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                selected_action = None
                for surf, rect, action in key_list:
                    # See if the user clicked on one of the rects.
                    if rect.collidepoint(event.pos):
                        selected_action = action

            screen.blit(bg, (0,0))
            # Blit the action-key table. Draw a rect around the
            # selected action.
            for surf, rect, action in key_list:
                screen.blit(surf, rect)
                if selected_action == action:
                    pygame.draw.rect(screen, green, rect, 2)

            pygame.display.flip()
            clock.tick(60)

def process_keys(keys, hero, input_map, score):#pass argument variable to change key input, user can change key input
    player_sprites = ['images/megaman1.png','images/megaman8.png']
    x = random.choice(player_sprites)#sprites work but change way too fast
    #only change picture wean movement key is pressed
    #gets the name from input_map at the top of the file and sees what key its bind to,
    #if the key gets changed mid game then the variable name will now have that keybind

        
    if keys[input_map['move right']]:
        hero.sprite.movementVector[0] += 1
        hero.sprite.image = pygame.image.load(x) 
    if keys[input_map['move left']]:
        hero.sprite.movementVector[0] -= 1
        hero.sprite.image = pygame.image.load(x) 
    if keys[input_map['move up']]:
        hero.sprite.movementVector[1] -= 1
        hero.sprite.image = pygame.image.load(x)
    if keys[input_map['move down']]:
        hero.sprite.movementVector[1] += 1
        hero.sprite.image = pygame.image.load(x)
    if keys[input_map['quit']]:
        updateFile(score)
        os.system('main_menu.py')
        pygame.quit()
        sys.exit()
    if keys[input_map['main menu']]:
        updateFile(score)
        os.system('main_menu.py')
        pygame.quit()
        sys.exit()
    elif keys[input_map['pistol']]:
        hero.sprite.equippedWeapon = hero.sprite.availableWeapons[0]
    elif keys[input_map['shotgun']]:
        hero.sprite.equippedWeapon = hero.sprite.availableWeapons[1]
    elif keys[input_map['machine gun']]:
        hero.sprite.equippedWeapon = hero.sprite.availableWeapons[2]
    elif keys[input_map['knife']]:
        hero.sprite.equippedWeapon = hero.sprite.availableWeapons[4]
    elif keys[input_map['?']]:
        hero.sprite.equippedWeapon = hero.sprite.availableWeapons[5]
    elif keys[input_map['weapon god']]:
        hero.sprite.equippedWeapon = hero.sprite.availableWeapons[3]
    elif keys[input_map['unlim health']]:
        hero.sprite.health = 0
   # elif keys[input_map['change character']]:
    #    hero.sprite.image = pygame.image.load()

    clock.tick(60)


  
#different character choices, allows the user to press the key and the sprite will change
#issue, pressing it once changes the sprite many times                
            
       
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inp_map = assignment_menu(input_map)
    if keys[pygame.K_m]:
        os.system('main_menu.py')
        pygame.quit()
        sys.exit()

    
#need to fix the scoreboard

#try except useage
  
def updateFile(score):
    name = ''

    active = False
    while active == False:
        for event in pygame.event.get():
          # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos) and name!='':
                    active = True
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_ESCAPE:
                    #active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-100]#if backspace is pressed all the name
                else:               #characters will gone
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
        input_rect.w = max(500, text_surface.get_width()-10)      
        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pygame.display.flip()
        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        clock.tick(60)
       

        if active == True:
           
            x = name[0:10]#allows the first 10 characters to be in the nam
       
            print(x)
            myFile = open("score.csv","a+")
            f = myFile.write("\n")
            f = myFile.write(str(x))
            f = myFile.write(str(score))
            myFile.close()
            pygame.display.flip()

            os.system('main_menu.py')
            pygame.quit()
            sys.exit()

                

#make the inout box look better
    return(score)



def process_mouse(mouse, hero):
    if mouse[0]:
        hero.sprite.shoot(pygame.mouse.get_pos())

#def timer():
    #x = pygame.time.get_ticks()
    #print(x/60)
    

def main():
#function providesw the pause and menu pop up for changing key binds
    done = False
    hero = pygame.sprite.GroupSingle(Player(screen.get_size()))
    player = hero
   

    while hero.sprite.alive and done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True# Enter the key assignment menu.
            else: inp_map = assignment_menu(input_map)
            inp_map_key(keys, hero)

        pressed_keys = pygame.key.get_pressed()


#game plays until lives have ran out
def game_loop():
    done = False
    hero = pygame.sprite.GroupSingle(Player(screen.get_size()))
    enemies = pygame.sprite.Group()
    lastEnemy = pygame.time.get_ticks()
    score = 0
        # This dict maps actions to the corresponding key scancodes.




        
    while hero.sprite.alive and not done:#while the player has lives the game loop runs
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        currentTime = pygame.time.get_ticks()
        #enemy_ping(enemies)
        #timer()
        
#use enemies variable to show how many enemies are on
#to the screen
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    inp_map = assignment_menu(input_map)

        
          
        screen.blit(bg, (0, 0))
        
        #process_keys(keys, hero)
        process_mouse(mouse, hero)
        process_keys(keys, hero, input_map, score)

             
        
        # Enemy spawning process
        if lastEnemy < currentTime - 200 and len(enemies) < 100:
            spawnSide = random.random()
            if spawnSide < 0.3:
                enemies.add(Enemy((0, random.randint(0, size[1]))))
            elif spawnSide < 0.55:
                enemies.add(Enemy((size[0], random.randint(0, size[1]))))
            elif spawnSide < 0.8:
                enemies.add(Enemy((random.randint(0, size[0]), 0)))
            else:
                enemies.add(Enemy((random.randint(0, size[0]), size[1])))
            lastEnemy = currentTime
        
        score += move_entities(hero, enemies, clock.get_time()/17)
        render_entities(hero, enemies)
        
        # Health and score render
        for hp in range(hero.sprite.health):
            screen.blit(healthRender, (15 + hp*35, 0))
        scoreRender = scoreFont.render(str(score), True, pygame.Color('white'))
        scoreRect = scoreRender.get_rect()
        scoreRect.right = size[0] - 20
        scoreRect.top = 20
        screen.blit(scoreRender, scoreRect)
        pygame.display.flip()
        clock.tick(244)
        







#this will pause the game and the enemies until the user presses unpause
        #dont need this no mo, control menu better :)
def pause():
    pause = 1
    print("paused")
    while pause:
        clock.tick(0)#this freezes the game until the escape key is pressed
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:#if escape key is pressed then the game pauses
                    pygame.time.delay(0)
                    pause = 0
                if event.key == pygame.K_SPACE:#if space bar is pressed it unpauses
                    pause = 0

                
                



done = game_loop()
while not done:#while the game is running check what keys are pressed
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    currentTime = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            updateFile(score)
    #ends game
        if done == True:
            updateFile(score)
        if keys[pygame.K_r]:
            done = game_loop()
        if keys[pygame.K_q]:
            updateFile(score)
            




#ends game
sys.exit()
pygame.quit()
