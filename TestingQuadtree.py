
import pygame
import sys
from pygame.locals import *
from Entity import *
from QuadTree import QuadTree


def update(dt):
    for e in entities:
        e.update(dt)
    qTree.empty()
    collisions = []
    qTree.addEntities(entities, collisions)

    #print "collisions\n", collisions

def processInput():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    if pygame.key.get_pressed()[K_w] == True:
        entity.accelirate((0, -1)) 
    if pygame.key.get_pressed()[K_s] == True:
        entity.accelirate((0, 1)) 
    if pygame.key.get_pressed()[K_a] == True:
        entity.accelirate((-1, 0)) 
    if pygame.key.get_pressed()[K_d] == True:
        entity.accelirate((1, 0)) 


def render():
    surface.fill(Color('black'))
    for e in entities:    
        e.draw(surface)#, True)
    #qTree.drawTree(surface)
    pygame.display.update()

def main():
    global surface
    global entities
    global qTree
    global collisions

    WindowSize = (300,300)

    playerFilename = 'lynSprite.gif'
    enemyFilename  = 'brigandSprite.gif'

    pygame.init()
    pygame.display.set_caption('Testing Entity')    
    surface = pygame.display.set_mode(WindowSize)

    qTree = QuadTree(pygame.Rect(0,0,WindowSize[0],WindowSize[1]))

    collisions = []

    entities = []

    e1 = Entity()
    e1.loadSprite(playerFilename, (0,0,21,35))
    e1.setLocation((100,100))
    entities.append(e1)

    e2 = Entity()
    e2.loadSprite(enemyFilename, (0,0,36,33))
    e2.setLocation((115,115))
    entities.append(e2)

    e3 = Entity()
    e3.loadSprite(enemyFilename, (0,0,36,33))
    e3.setLocation((0,0))
    entities.append(e3)

    e4 = Entity()
    e4.loadSprite(enemyFilename, (0,0,36,33))
    e4.setLocation((150,100))
    entities.append(e4)

    e5 = Entity()
    e5.loadSprite(enemyFilename, (0,0,36,33))
    e5.setLocation((100,150))
    entities.append(e5)


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
            #To esure calculations are done on fixed time steps
            update(timePerFrame)


        render()
        

if __name__ == '__main__':
    main()
