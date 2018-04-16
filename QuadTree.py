
import pygame
from pygame.locals import Color
from itertools import combinations
from FindingOverlap import inBoundary

from FindingLambda import findCollision

_maxDepth = 5
_capacity = 4

_uniqueId = 0

class QuadTree():

    def __init__(self, boundary, dt, depth = 0):
        self.boundary   = boundary
        self.contents   = []
        self.subtree    = []
        self.depth      = depth
        self.counter    = 0
        self.dt         = dt
        global _uniqueId
        self.id   = _uniqueId
        _uniqueId+=1

    def addEntity(self, entity):
        """ 
            Adds an Entity to the quad tree. If a list of collisions are passed, all collisions found when adding will be append.
        """

        #does the entitiy lie in the quadtree's bondary
        if not inBoundary(self.dt, entity, self.boundary):
            return False

        #are we adding to this level or do we need to pass down the tree
        if len(self.contents) < _capacity or self.depth > _maxDepth:
            self.contents.append(entity)
            return True

	#Make the subtree if the current node is full
        if len(self.subtree) == 0:
            self.makeSubTrees()

	#Add the current entity to the subtree
        for quad in self.subtree:
            quad.addEntity(entity)

        return True
    
    def addEntities(self, entities, collisionRegister):
        """ Pass a list or tupple of entities which will then be added to the quadtree."""
        for i in collisionRegister:
            self.addEntity(entities[i])

    def makeSubTrees(self):
        """ The domain is spit into 4 quads and all contents are passed to the relevant quad """

        self.subtree.append(QuadTree(self._NWBoundary(), self.dt, self.depth + 1))
        self.subtree.append(QuadTree(self._NEBoundary(), self.dt, self.depth + 1))
        self.subtree.append(QuadTree(self._SWBoundary(), self.dt, self.depth + 1))
        self.subtree.append(QuadTree(self._SEBoundary(), self.dt, self.depth + 1))

        #Try to add contents to any tree that wants it
        for quad in self.subtree:
            quad.addEntities(self.contents)


    def empty(self):
        self.contents   = []
        self.subtree    = []


    def findCollisions(self, collisions = []):
        if self.subtree == []:
            for e1,e2 in combinations(self.contents, 2):
                test, collision = findCollision(self.dt, e1, e2)
                if test:
                    collisions.append(collision)
        else:
            for tree in self.subtree:
                tree.findCollisions(collisions)
        return collisions


    def drawTree(self, surface):
        """ Draws the boundaries of the quadtree """
        pygame.draw.rect(surface, Color("green"), self.boundary, 1)
        for quad in self.subtree:
            quad.drawTree(surface)



    """A collection of functions for finding the quarters of the current boudary"""
    def _NWBoundary(self):
        return pygame.Rect(self.boundary.left, self.boundary.top, self.boundary.width / 2, self.boundary.height / 2)

    def _NEBoundary(self):
        return pygame.Rect(self.boundary.left + self.boundary.width / 2, self.boundary.top, self.boundary.width / 2, self.boundary.height / 2)

    def _SWBoundary(self):
        return pygame.Rect(self.boundary.left, self.boundary.top + self.boundary.height / 2, self.boundary.width / 2, self.boundary.height / 2)

    def _SEBoundary(self):
        return pygame.Rect(self.boundary.left + self.boundary.width / 2, self.boundary.top + self.boundary.height / 2, self.boundary.width / 2, self.boundary.height / 2)
    """end of helper functions"""




