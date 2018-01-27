
import pygame
from pygame.locals import *
from utility import sortEntity, appendUnique, entityCollision, findCollisionTime
from Entity import Entity
from itertools import combinations

_maxDepth = 5
_capacity = 4

_uniqueId = 0

class QuadTree():

    def __init__(self, boundary, dt, depth = 0):
        self.boundary   = boundary
        self.contents   = []
        self.subtree    = []
        self.depth      = depth
        self.dt         = dt
        self.counter    = 0
        global _uniqueId
        self.id   = _uniqueId
        _uniqueId+=1

    def addEntity(self, entity):
        """ 
            Adds an Entity to the quad tree. If a list of collisions are passed, all collisions found when adding will be append.
        """

        #does the entitiy lie in the quadtree
        collisionTime = findCollisionTime(self.dt, entity.AABB, self.boundary, entity.getVelocity())
        if not collisionTime[0]:
            return False

        #are we adding to this level or do we need to pass down the tree
        if len(self.contents) < _capacity or self.depth > _maxDepth:
            self.contents.append(entity)
            return True

	    #Make the subtree if the current node is full
        if len(self.subtree) == 0:
            self.makeSubTrees()

	    #Add the current entity to the tree
        for quad in self.subtree:
            quad.addEntity(entity)

        return True
    
    def addEntities(self, entities):
        """ Pass a list or tupple of entities which will then be added to the quadtree."""
        for e in entities:
            self.addEntity(e)


    

    def makeSubTrees(self):
        """ The domain is spit into 4 quads and all contents are passed to the relevant quad """

        self.subtree.append(QuadTree(self.NWBoundary(), self.dt, self.depth + 1))
        self.subtree.append(QuadTree(self.NEBoundary(), self.dt, self.depth + 1))
        self.subtree.append(QuadTree(self.SWBoundary(), self.dt, self.depth + 1))
        self.subtree.append(QuadTree(self.SEBoundary(), self.dt, self.depth + 1))

        #Try to add contents to any tree that wants it
        for quad in self.subtree:
            quad.addEntities(self.contents)


    def empty(self):
        self.contents   = []
        self.subtree    = []


    def findCollisions(self, collisions):
        if self.subtree == []:
            for e1,e2 in combinations(self.contents, 2):
                collisionTime = findCollisionTime(self.dt, e1.AABB, e2.AABB, e1.getVelocity(), e2.getVelocity())
                if collisionTime[0]:
                    collisions.append([sortEntity(e1, e2),collisionTime[1]])
        else:
            for tree in self.subtree:
                tree.findCollisions(collisions)


    def printTree(self):
        if len(self.contents) == _capacity:
            for tree in self.subtree:
                tree.printTree()
        else:
            print "node Id", self.id
            print "entities held:"
            for e in self.contents:
                print e.id


    def drawTree(self, surface):
        """ Draws the boundaries of the quadtree """
        pygame.draw.rect(surface, Color("green"), self.boundary, 1)
        for quad in self.subtree:
            quad.drawTree(surface)



    """A collection of functions for finding the quarters of the current boudary"""
    def NWBoundary(self):
        return pygame.Rect(self.boundary.left, self.boundary.top, self.boundary.width / 2, self.boundary.height / 2)

    def NEBoundary(self):
        return pygame.Rect(self.boundary.left + self.boundary.width / 2, self.boundary.top, self.boundary.width / 2, self.boundary.height / 2)

    def SWBoundary(self):
        return pygame.Rect(self.boundary.left, self.boundary.top + self.boundary.height / 2, self.boundary.width / 2, self.boundary.height / 2)

    def SEBoundary(self):
        return pygame.Rect(self.boundary.left + self.boundary.width / 2, self.boundary.top + self.boundary.height / 2, self.boundary.width / 2, self.boundary.height / 2)
    """end of helper functions"""




