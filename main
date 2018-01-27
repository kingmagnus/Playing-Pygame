

import pygame
import sys

from pygame.locals import *

from Player import Player
from World  import World

import Camera

def processInput():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        player.handleEvent(event, commandQueue)

    player.handleRealtimeEvent(commandQueue)
    

def main():
    global surface
    global commandQueue
    global player
    global world
    global cam

    FPS = 60
    timePerFrameInms = 1.0/FPS*1000
    timeSinceRender = timePerFrameInms+1

    pygame.init()
    pygame.display.set_caption('Testing Player')    
    
    viewSize = (300,300)
    surface = pygame.display.set_mode(viewSize)
    commandQueue = []
    player = Player()
    world = World(timePerFrameInms)
    cam = Camera.Camera(Camera.ViewTrackingMover, viewSize)

    clock = pygame.time.Clock()

    counter = 0

    while True:
        timeSinceRender += clock.tick()
        #print "timeSinceRender", timeSinceRender
        #counter = counter +1

        while timeSinceRender > timePerFrameInms:
            #Incase we take more than one frame to update
            timeSinceRender -= timePerFrameInms
            #We update untill it is time to draw the frame
            
            """ Input logic is held in the processInput which calls the Player class wherein Commands are added to the command queue to be handeled by the World class """
            processInput()

            """ Game logic is held in the World class """
            world.update(commandQueue, timePerFrameInms)

        world.render(surface)
        counter+=1
        

if __name__ == '__main__':
    main()
