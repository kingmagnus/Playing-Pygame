


from Command import * 
import pygame
from pygame.locals import *
from InputComponent import *


UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"




class InputComponent_Jumping:
    def __init__(self):
        self.keyMap = { UP   : K_w,
                        DOWN : K_s,
                        LEFT : K_a,
                        RIGHT: K_d}

        self.actionMap = { UP    : Command(action = lambda entity, dt : entity.accelirate((0, -1)), categories = [Category.PLAYER]),
                           DOWN  :Command(action = lambda entity, dt : entity.accelirate((0, 1)), categories = [Category.PLAYER]),
                           LEFT  :Command(action = lambda entity, dt : entity.accelirate((-1, 0)), categories = [Category.PLAYER]),
                           RIGHT :Command(action = lambda entity, dt : entity.accelirate((1, 0)), categories = [Category.PLAYER])}

    def update(self, commandQueue):
        if pygame.key.get_pressed()[self.keyMap[UP]]    == True:
            commandQueue.append(self.actionMap[UP])

        if pygame.key.get_pressed()[self.keyMap[DOWN]]  == True:
            commandQueue.append(self.actionMap[DOWN])

        if pygame.key.get_pressed()[self.keyMap[LEFT]]  == True:
            commandQueue.append(self.actionMap[LEFT])

        if pygame.key.get_pressed()[self.keyMap[RIGHT]] == True:
            commandQueue.append(self.actionMap[RIGHT])
