
import pygame
import sys
from pygame.locals import *
from StandingState import StandingState
from GraphicsComponent import *
import Category

from utility import unitVector, getSize


_uniqueId = 0


class Entity():
    """ The Entity class is responsible for individual elements of the scene """

    def __init__(self, category = Category.NONE, Location = [0,0], Direction = [0,0], AABB = pygame.Rect(0,0,0,0)):
        """ sets Velocity, Location, Direction. Type describes the type of the entitiy """
        global _uniqueId
        self.mDirection = Direction
        self.mLocation = Location
        self.mCategory = category
        self.AABB      = AABB
        self.speed     = 120 #in px/s
        self.id        = _uniqueId
        self.lx        = 1
    	self.ly        = 1
        self.mVCorrection = [0,0]
        self._state    = StandingState()

        self._GraphicsComponent = GraphicsComponent()
        #self._PhysicsComponent  = PhysicsComponent()
        #self._InputComponent    = InputComponent()#(slef._State)

        self.getSprite  = self._GraphicsComponent.getSprite
        self.loadSprite = self._GraphicsComponent.loadSprite

        _uniqueId+=1

    def draw(self, surface, drawBounds = False):
        """ calls the grapihcs component """
        self._GraphicsComponent.update(self, surface)


    def update(self, dt):
        """ moves the entity through its velocity for a time step dt"""
        #as dt in ms and velocity in px/s
        distance = [ i * self.speed * dt / 1000. for i in unitVector(self.mDirection)]
        distance[0] = distance[0]*self.lx
        distance[1] = distance[1]*self.ly

        #if self.mCategory == Category.PLAYER:
        #    print "distance", distance, "abs(distance)", (distance[0]**2 + distance[1]**2)**0.5

        self.mDirection = [0,0]
        self.mVCorrection = [0,0]
        self.lx = 1
        self.ly = 1
        self.move(distance)

    def move(self, distance):
        """ moves the sprite """
        self.mLocation = [sum(i) for i in zip(self.mLocation, distance)]
        self.AABB.left = self.mLocation[0]
        self.AABB.top  = self.mLocation[1]

    def setLocation(self, location):
        """ moves the sprite """
        self.mLocation = location
        self.AABB.left = location[0]
        self.AABB.top  = location[1]

    def accelirate(self, acceliration):
        self.mDirection = [sum(i) for i in zip(self.mDirection, acceliration)]

    def performCommand(self, command, dt):
        if self.mCategory in command.categories:
            command.action(self, dt)

    def getVelocity(self):
        return [ i * self.speed for i in unitVector(self.mDirection)] 

    def applyView(self, camAplyView):
        self.AABB  = camAplyView(self.AABB)
        self.mLocation = self.AABB.topleft
        
    def setArea(self, rect):
        self.AABB = pygame.Rect(rect)







