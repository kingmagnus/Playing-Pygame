

import pygame
import Category
import sys
from pygame.locals import *
from Entity import *
from Command import * 





keyMap = { "Up"   : K_w,
           "Down" : K_s,
           "Left" : K_a,
           "Right": K_d}

def update(dt):
    entity.update(dt)

def processInput():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    if pygame.key.get_pressed()[keyMap["Up"]]    == True:
        commandQueue.append(cAccelirateUp)

    if pygame.key.get_pressed()[keyMap["Down"]]  == True:
        commandQueue.append(cAccelirateDown)

    if pygame.key.get_pressed()[keyMap["Left"]]  == True:
        commandQueue.append(cAccelirateLeft)

    if pygame.key.get_pressed()[keyMap["Right"]] == True:
        commandQueue.append(cAccelirateRight)


def render():
    surface.fill(Color('black'))
    entity.draw(surface)
    pygame.display.update()

def main():
    global surface
    global entity
    global commandQueue

    filename = 'lynSprite.gif'

    pygame.init()
    pygame.display.set_caption('Testing Entity')    
    
    surface = pygame.display.set_mode((300, 300))
    entity = Entity()
    commandQueue = []

    entity.loadSprite(filename, (0,0,21,35))

    clock = pygame.time.Clock()

    FPS = 10
    timePerFrame = 1.0/FPS

    while True:
        timeSinceUpdate = clock.tick()

        while timeSinceUpdate > timePerFrame:
            #Incase we take more than one frame to update
            timeSinceUpdate -= timePerFrame
            #We update untill it is time to draw the frame
            processInput()
            #we add commands to the command queue to be implimented in the game logic

            """ Only game logic below!! """

            #exicute the commands made in processInput()
            while commandQueue != []:
                entity.performCommand(commandQueue.pop(0), timePerFrame)
            #To esure calculations are done on fixed time steps
            update(timePerFrame)

        render()
        

if __name__ == '__main__':
    main()
