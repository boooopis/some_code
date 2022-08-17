import pygame
import math
from Projectile import Projectile
import random

#music = pygame.mixer.music.load('zombie_noises.mp3')
#pygame.mixer.music.play(-1)

def normalize_vector(vector):
    if vector == [0, 0]:
        return [0, 0]
    pythagoras = math.sqrt(vector[0]*vector[0] + vector[1]*vector[1])
    return (vector[0] / pythagoras, vector[1] / pythagoras)



class Enemy(pygame.sprite.Sprite):
    projectiles = pygame.sprite.Group()
    def __init__(self, pos):
        super().__init__()
        enemy_changer = ['images/zombie.2.png','images/megaman1.png','images/megaman6.png',
              ]
        x = random.choice(enemy_changer)
        self.image = pygame.image.load(x)
        #self.image = pygame.image.load("images/zombie.2.png")
        self.rect = self.image.get_rect()
#if player custom sprite works, then try do the same for zombies, can change them to any of the choices        
        self.pos = list(pos)
        self.movementVector = [0, 0]
        self.movementSpeed = 1.5
        self.lastShot = pygame.time.get_ticks()
        self.weaponCooldown = 1500
        
#this process will allow the enimies to move and follow the player
        
    def move(self, enemies, playerPos, tDelta):
        self.movementVector = (playerPos[0] - self.pos[0],
                               playerPos[1] - self.pos[1])
        self.movementVector = normalize_vector(self.movementVector)
        self.pos[0] += self.movementVector[0] * self.movementSpeed * tDelta
        self.pos[1] += self.movementVector[1] * self.movementSpeed * tDelta
        
        # Collision test with other enemies
        self.movementVector = [0, 0]
        for sprite in enemies:
            if sprite is self:
                continue
            if pygame.sprite.collide_circle(self, sprite):
                self.movementVector[0] += self.pos[0] - sprite.pos[0]
                self.movementVector[1] += self.pos[1] - sprite.pos[1]

        self.movementVector = normalize_vector(self.movementVector)
        self.pos[0] += self.movementVector[0] * 0.5  # The constant is how far the sprite will be
        self.pos[1] += self.movementVector[1] * 0.5  # dragged from the sprite it collided with
        
        self.rect.topleft = self.pos
    def shoot(self, playerPos):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastShot > self.weaponCooldown:
            direction = (playerPos[0] - self.pos[0], playerPos[1] - self.pos[1])
            self.lastShot = currentTime
            self.projectiles.add(Projectile(self.pos,
                                            normalize_vector(direction),
                                            3, 500, (255, 0, 0)))
    def render(self, surface):
        surface.blit(self.image, self.pos)
