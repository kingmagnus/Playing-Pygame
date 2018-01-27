
import pygame
from pygame.locals import *
from utility import sortEntity, appendUnique, entityCollision
from Entity import Entity

_maxDepth = 5
_capacity = 4

class QuadTree():

    def __init__(self, boundary, depth = 0):
        self.boundary = boundary
        self.contents = []
        self.subtree  = []
        self.depth    = depth

    def addEntity(self, entity, collisions = None):
        """ 
            Adds an Entity to the quad tree. If a list of collisions are passed, all collisions found when adding will be append.
        """

        if not self.boundary.colliderect(entity.AABB):
            return False

        if len(self.contents) < _capacity or self.depth > _maxDepth:
            for e in self.contents:
                 if collisions != None and entityCollision(e, entity):
                    print "collision found"""
                    collisions.append(sortEntity(entity, e))

            self.contents.append(entity)
            return True

	    """Make the subtree if the current node is full"""
        if len(self.subtree) == 0:
            self.makeSubTrees()

	    """Add the current entity to the tree"""
        for quad in self.subtree:
            quad.addEntity(entity, collisions)
    
    def addEntities(self, entities, collisions = None):
        """ Pass a list or tupple of entities which will then be added to the quadtree. If a list of collisions are passed, all collisions found when adding will be append."""
        for e in entities:
            self.addEntity(e, collisions)


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

    def makeSubTrees(self):
        """ The domain is spit into 4 quads and all contents are passed to the relevant quad """

        self.subtree.append(QuadTree(self.NWBoundary(), self.depth + 1))
        self.subtree.append(QuadTree(self.NEBoundary(), self.depth + 1))
        self.subtree.append(QuadTree(self.SWBoundary(), self.depth + 1))
        self.subtree.append(QuadTree(self.SEBoundary(), self.depth + 1))


        #Try to add contents to any tree that wants it
        for quad in self.subtree:
            quad.addEntities(self.contents)

    def drawTree(self, surface):
        """ Draws the boundaries of the quadtree """
        pygame.draw.rect(surface, Color("green"), self.boundary, 1)
        for quad in self.subtree:
            quad.drawTree(surface)

    def queryRange(self, testRect, collisions):

        if not self.boundary.colliderect(testRect):
            return

        if self.subtree == []:
            for rect in self.contents:
                if rect.colliderect(testRect) and rect != testRect:
                    appendUnique(collisions, sortRect(rect, testRect))
        else:
            for quad in self.subtree:
                quad.queryRange(testRect, collisions)

    def empty(self):
        self.contents = []
        self.subtree  = []










