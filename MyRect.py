from pygame.locals import Color
import pygame
from math import cos, sin

class MyRect():
    def __init__(self, xpos = 0, ypos = 0, width = 0, height = 0, angle = 0):
        """ xpos, ypos = location of first vertex, width, height = rect dimentions, angle = angle of rotation about first vertex clockwise  """
        self.pointList = [ (xpos , ypos),
                           (int(xpos + width*cos(angle)), int(ypos + width*sin(angle))),
                           (int(xpos + width*cos(angle) - height*sin(angle)), int(ypos + height*cos(angle) + width*sin(angle))),
                           (int(xpos - height*sin(angle)), int(ypos + height*cos(angle))) ]
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.angle = angle
        

    def draw(self, surface):
        pygame.draw.polygon(surface, Color('red'), self.pointList)
        pygame.draw.circle(surface, Color('white'),   self.pointList[0], 5)
        pygame.draw.circle(surface, Color('white'),  self.pointList[1], 5)
        pygame.draw.circle(surface, Color('white'), self.pointList[2], 5)
        pygame.draw.circle(surface, Color('white'),  self.pointList[3], 5)
