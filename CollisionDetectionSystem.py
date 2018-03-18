
from QuadTree import QuadTree
import pygame

BACKGROUND  = 0
ACTIVELAYER = 1
FORGROUND   = 2
LAYERCOUNT  = 3


class CollisionDetectionSystem:

    def __init__(self, viewSize, dt):
        self._qTree = QuadTree(pygame.Rect(0,0,viewSize[0],viewSize[1]),dt)  

    def getCollisions(self, entities):
        #broad phase collsion detection
        self._qTree.empty()
        self._qTree.addEntities(entities)

        return self._qTree.findCollisions(self._collisions)
