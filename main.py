

import pygame
import sys

from pygame.locals import QUIT


from World  import World


def processInput():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    

def main():
    global surface
    global commandQueue
    global world
    global cam

    FPS = 1
    timePerFrameInms = 1.0/FPS*1000
    timeSinceRender = timePerFrameInms+1

    pygame.init()
    pygame.display.set_caption('Window')    
    
    viewSize = (300,300)
    surface = pygame.display.set_mode(viewSize)
    commandQueue = []
    world = World(timePerFrameInms)

    clock = pygame.time.Clock()

    #main game loop
    while True:
        timeSinceRender += clock.tick()
        #print "timeSinceRender", timeSinceRender
        #counter = counter +1

        while timeSinceRender > timePerFrameInms:
            #Incase we take more than one frame to update
            timeSinceRender -= timePerFrameInms
            #We update untill it is time to draw the frame
            processInput()
            """ Game logic is held in the World class """
            world.update(commandQueue, timePerFrameInms)

        world.render(surface)
        

if __name__ == '__main__':
    main()
