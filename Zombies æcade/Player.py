import pygame
import pdb
import math
import Weapon


PLAYERCOLOR = (255, 55, 50)
pygame.init()

shoot_sound = pygame.mixer.Sound("pew.mp3")
death_sound = pygame.mixer.Sound("bruh.mp3")


def normalize_vector(vector):
    if vector == [0, 0]:
        return [0, 0]    
    pythagoras = math.sqrt(vector[0]*vector[0] + vector[1]*vector[1])
    return (vector[0] / pythagoras, vector[1] / pythagoras)

class Player(pygame.sprite.Sprite):
    projectiles = pygame.sprite.Group()
    def __init__(self, screenSize):
        super().__init__()
        self.image = pygame.image.load("images/megaman8.png")#custom character selection, multiple characters and the user choses them
        self.rect = self.image.get_rect()#make image a numeric chice and them have the image to validation
#display character selection, give all a number, when image is chose change the player sprite
#to that number.

        self.pos = [screenSize[0] // 2, screenSize[1] // 2]
        self.health = 3
        self.alive = True
        self.movementVector = [0, 0]
        self.movementSpeed = 2.5
        self.availableWeapons = [Weapon.Pistol(),
                                 Weapon.Shotgun(),
                                 Weapon.MachineGun(),
                                 Weapon.GodMode(),
                                 Weapon.knife(),
                                 Weapon.rpg(),
                                 Weapon.minigun(),
                                 Weapon.Raygun(),
                                 Weapon.sniper()]
        self.equippedWeapon = self.availableWeapons[0]

    def move(self, screenSize, tDelta):
        self.movementVector = normalize_vector(self.movementVector)
        newPos = (self.pos[0] + self.movementVector[0]*self.movementSpeed*tDelta,
                  self.pos[1] + self.movementVector[1]*self.movementSpeed*tDelta)
        if newPos[0] < 0:
            self.pos[0] = 0
        elif newPos[0] > screenSize[0] - self.rect.width:
            self.pos[0] = screenSize[0] - self.rect.width
        else:
            self.pos[0] = newPos[0]

        if newPos[1] < 0:
            self.pos[1] = 0
        elif newPos[1] > screenSize[1]-self.rect.height:
            self.pos[1] = screenSize[1]-self.rect.width
        else:
            self.pos[1] = newPos[1]
        
        self.rect.topleft = self.pos
        self.movementVector = [0, 0]
        
    def shoot(self, mousePos):
        self.equippedWeapon.shoot(self, mousePos)
        shoot_sound.play()
        
    def render(self, surface):
        surface.blit(self.image, self.pos)

            
