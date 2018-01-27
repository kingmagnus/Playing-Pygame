


import pygame
from Entity import *
from Command import * 
from SpriteSheet import *
from QuadTree import QuadTree
import Category
import CollisionHandling
import Camera

BACKGROUND  = 0
ACTIVELAYER = 1
FORGROUND   = 2
LAYERCOUNT  = 3

lynSpriteSheet = "lynSpriteSheet"
lynSprite      = "lynSprite"
brigandSpriteSheet = "brigandSpriteSheet"
brigandSprite = "brigandSprite"



class World():
    """ Contains all objects relevant to the game world """

    def __init__(self, dt):
        viewSize = (300,300)
        self.spawnLocation = [100,100]
        self.layers = [[],[],[]]
        self.loadTextures()
        self.buildScene()
        self.qTree = QuadTree(pygame.Rect(0,0,viewSize[0],viewSize[1]),dt)
        self.counter = 0
        self.cam = Camera.Camera(Camera.ViewEntityTrackingMover, viewSize)



    def update(self, commandQueue, dt):
        """Applies the command Queue to the entities, finds how the orld should respond (collisions ect.) and then updates the entities """


        #Process all commands (dt = timePerFrame)
        while commandQueue != []:
            command = commandQueue.pop(0)
            for entity in self.layers[ACTIVELAYER]:
                entity.performCommand(command, dt)

        #broad phase collsion detection
        self.qTree.empty()
        self.qTree.addEntities(self.layers[ACTIVELAYER])

        collisions = []

        self.qTree.findCollisions(collisions)

        self.handleCollisions(collisions)


        #finaly change the world
        for layer in self.layers:
            for entity in layer:
                entity.update(dt)

    def render(self, surface):
        self.cam.updateView(self.layers[ACTIVELAYER][0])
        surface.fill(Color('black'))
        for layer in self.layers:
            for entity in layer:
                entity.applyView(self.cam.applyView)
                entity.draw(surface)
        #self.qTree.drawTree(surface)

        #all drawing occurs before the update
        pygame.display.update()

        

    def loadTextures(self):
        self.textures = { lynSpriteSheet : SpriteSheet("lynSpriteSheet.gif"),
                          lynSprite      : SpriteSheet("lynSprite.gif"),
                          brigandSpriteSheet : SpriteSheet("brigandSprite.gif"),
                          brigandSprite  : SpriteSheet("brigandSprite.gif")}
                          
    def buildScene(self):
        
        eTemp = Entity(Category.PLAYER)
        eTemp.getSprite(self.textures[lynSprite].sprite_sheet, (0,0,21,35))
        eTemp.setLocation((100,100))
        self.layers[ACTIVELAYER].append(eTemp)

        
        #####


        eTemp = Entity(Category.ENEMY)
        eTemp.getSprite(self.textures[brigandSprite].sprite_sheet, (0,0,36,33))
        eTemp.setLocation((100+21,100))
        self.layers[ACTIVELAYER].append(eTemp)
        
        eTemp = Entity(Category.ENEMY)
        eTemp.getSprite(self.textures[brigandSprite].sprite_sheet, (0,0,36,33))
        eTemp.setLocation((100,100-33))
        self.layers[ACTIVELAYER].append(eTemp)
        
        eTemp = Entity(Category.ENEMY)
        eTemp.getSprite(self.textures[brigandSprite].sprite_sheet, (0,0,36,33))
        eTemp.setLocation((50,200))
        self.layers[ACTIVELAYER].append(eTemp)
        
        eTemp = Entity(Category.ENEMY)
        eTemp.getSprite(self.textures[brigandSprite].sprite_sheet, (0,0,36,33))
        eTemp.setLocation((200,200))
        self.layers[ACTIVELAYER].append(eTemp)
        

    def handleCollisions(self, collisions):
        #if collisions!= []:
        #    print "collision found"
        #    print collisions[0][1]

        for collision in collisions:
            if CollisionHandling.checkCategoryPair(collision):
                #look up the pair's response function in the dictionary ResponseDict
                a = CollisionHandling.ResponseDict[(collision[0][0].mCategory, collision[0][1].mCategory)]
                a(collision)



















