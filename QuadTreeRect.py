
import pygame
from pygame.locals import *
from utility import sortRect, appendUnique
from Entity import Entity

_maxDepth = 5
_capacity = 4

class QuadTree():

    def __init__(self, boundary, depth = 0):
        self.boundary = boundary
        self.contents = []
        self.subtree  = []
        self.depth    = depth

    def addObject(self, rect, collisions = None):
        """ 
            Adds an object to the quad tree:
            rect is a rectangle to be added to all quads it intersects
            collisions is a list of all rects in the quadtree the new rect collides with
        """

        if not self.boundary.colliderect(rect):
            return False

        if len(self.contents) < _capacity or self.depth > _maxDepth:
            for testRect in self.contents:
                 if collisions != None and rect.colliderect(testRect):
                    collisions.append(sortRect(rect, testRect))

            self.contents.append(rect)
            return True

        if len(self.subtree) == 0:
            self.makeSubTrees()

        for quad in self.subtree:
            quad.addObject(rect, collisions)
    
    def NWBoundary(self):
        return pygame.Rect(self.boundary.left, self.boundary.top, self.boundary.width / 2, self.boundary.height / 2)

    def NEBoundary(self):
        return pygame.Rect(self.boundary.left + self.boundary.width / 2, self.boundary.top, self.boundary.width / 2, self.boundary.height / 2)

    def SWBoundary(self):
        return pygame.Rect(self.boundary.left, self.boundary.top + self.boundary.height / 2, self.boundary.width / 2, self.boundary.height / 2)

    def SEBoundary(self):
        return pygame.Rect(self.boundary.left + self.boundary.width / 2, self.boundary.top + self.boundary.height / 2, self.boundary.width / 2, self.boundary.height / 2)


    def makeSubTrees(self):
        """ The domain is spit into 4 quads and all contents are passed to the relevant quad """

        self.subtree.append(QuadTree(self.NWBoundary(), self.depth + 1))
        self.subtree.append(QuadTree(self.NEBoundary(), self.depth + 1))
        self.subtree.append(QuadTree(self.SWBoundary(), self.depth + 1))
        self.subtree.append(QuadTree(self.SEBoundary(), self.depth + 1))

        for rect in self.contents:
            for quad in self.subtree:
                if quad.addObject(rect):
                    break

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










