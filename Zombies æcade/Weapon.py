import pygame
import math
import random
from Projectile import Projectile

screen = (1920, 1080)
Gui = ['images/zombie.png','images/megaman1.png']#make image for every weapon
#selected, this is so the user can see what weapon they have equipped :]



class Weapon():
    def __init__(self):
        self.lastShot = 0
    
    def shoot():
        pass
    
    @staticmethod
    def normalize_vector(vector):
        if vector == [0, 0]:
            return [0, 0]    
        pythagoras = math.sqrt(vector[0]*vector[0] + vector[1]*vector[1])
        return (vector[0] / pythagoras, vector[1] / pythagoras)
    
    @staticmethod
    def rotate_vector(vector, theta):
        resultVector = (vector[0] * math.cos(theta)
                        - vector[1] * math.sin(theta),
                        vector[0] * math.sin(theta)
                        + vector[1] * math.cos(theta))
        return resultVector

class Pistol(Weapon):
    def __init__(self):
        super().__init__()
        self.weaponCooldown = 250
        
    def shoot(self, user, mousePos):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastShot > self.weaponCooldown:
            direction = (mousePos[0] - user.pos[0], mousePos[1] - user.pos[1]) \
                if mousePos != user.pos else (1, 1)
            self.lastShot = currentTime
            user.projectiles.add(Projectile(user.pos,
                                            super().normalize_vector(direction),
                                            5, 2000, (0, 0, 255)))

            
class Shotgun(Weapon):
    def __init__(self):
        super().__init__()
        self.weaponCooldown = 555
        self.spreadArc = 65
        self.projectilesCount = 9
        
    def shoot(self, user, mousePos):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastShot > self.weaponCooldown:
            direction = (mousePos[0] - user.pos[0], mousePos[1] - user.pos[1]) \
                if mousePos != user.pos else (1, 1)
            self.lastShot = currentTime
            arcDifference = self.spreadArc / (self.projectilesCount - 1)
            for proj in range(self.projectilesCount):
                theta = math.radians(arcDifference*proj - self.spreadArc/2)
                projDir = super().rotate_vector(direction, theta)
                user.projectiles.add(Projectile(user.pos,
                                                super().normalize_vector(projDir),
                                                7, 500, (232, 144, 42)))
                
class MachineGun(Weapon):
    def __init__(self):
        super().__init__()
        self.weaponCooldown = 50
        self.spreadArc = 25
        
    def shoot(self, user, mousePos):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastShot > self.weaponCooldown:
            direction = (mousePos[0] - user.pos[0], mousePos[1] - user.pos[1]) \
                if mousePos != user.pos else (1, 1)
            self.lastShot = currentTime
            theta = math.radians(random.random()*self.spreadArc - self.spreadArc/2)
            projDir = super().rotate_vector(direction, theta)   
            user.projectiles.add(Projectile(user.pos,
                                            super().normalize_vector(projDir),
                                            6, 1000, (194, 54, 16)))
class GodMode(Weapon):
    def __init__(self):
        super().__init__()
        self.weaponCooldown = 1
        self.spreadArc = 400
        
    def shoot(self, user, mousePos):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastShot > self.weaponCooldown:
            direction = (mousePos[0] - user.pos[0], mousePos[1] - user.pos[1]) \
                if mousePos != user.pos else (1, 1)
            self.lastShot = currentTime
            theta = math.radians(random.random()*self.spreadArc - self.spreadArc/2)
            projDir = super().rotate_vector(direction, theta)   
            user.projectiles.add(Projectile(user.pos,
                                            super().normalize_vector(projDir),
                                            6, 1000, (194, 54, 16)))

class knife(Weapon):
    def __init__(self):
        super().__init__()
        self.weaponCooldown = 1
    
    def shoot(self, user, mousePos):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastShot > self.weaponCooldown:
            direction = (mousePos[0] - user.pos[0], mousePos[1] - user.pos[1]) \
                if mousePos != user.pos else (1, 1)
            self.lastShot = currentTime
            user.projectiles.add(Projectile(user.pos,
                                            super().normalize_vector(direction),
                                            1, 1, (0, 0, 255)))

class rpg(Weapon):
    def __init__(self):
        super().__init__()
        self.weaponCooldown = 200
        self.spreadArc = 3

    def shoot(self, user, mousePos):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastShot > self.weaponCooldown:
            direction = (mousePos[0] - user.pos[0], mousePos[1] - user.pos[1]) \
                        if mousePos != user.pos else (1, 1)
            self.lastShot = currentTime
            user.projectiles.add(Projectile(user.pos,
                                            super().normalize_vector(direction),
                                            50, 50, (0, 0, 255)))

class minigun(Weapon):
    def __init__(self):
        super().__init__()
        self.weaponCooldown = 50
        self.spreadArc = 5

    def shoot(self, user, mousePos):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastShot > self.weaponCooldown:
            direction = (mousePos[0] - user.pos[0], mousePos[1] - user.pos[1]) \
                        if mousePos != user.pos else (1, 1)
            self.lastshot = currentTime
            user.projectiles.add(Projectile(user.pos,
                                            super().normalize_vector(direction),
                                            15, 500, (40, 0, 40)))

class Raygun(Weapon):
    def __init__(self):
        super().__init__()
        self.weaponCooldown = 555
        self.spreadArc = 65
        self.projectileCount = 9

    def shoot(self, user, mousePos):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastShot > self.weaponCooldown:
            direction = (mousePos[0] - user.pos[0], mousePos[1] - user.pos[1]) \
                        if mousePos != user.pos else (1, 1)
            self.lastshot = currentTime
            user.projectiles.add(Projectile(user.pos,
                                            super().normalize_vector(direction),
                                            7, 500, (255, 40, 40)))


class sniper(Weapon):
    def __init__(self):
        super().__init__()
        self.weaponCooldown = 1500
    
    def shoot(self, user, mousePos):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastShot > self.weaponCooldown:
            direction = (mousePos[0] - user.pos[0], mousePos[1] - user.pos[1]) \
                if mousePos != user.pos else (1, 1)
            self.lastShot = currentTime
            user.projectiles.add(Projectile(user.pos,
                                            super().normalize_vector(direction),
                                            5, 1500, (0, 0, 255)))


