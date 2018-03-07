
from pygame import display
from pygame import Color
import pygame 
from math import cos, sin

from SpriteSheet import SpriteSheet
import SpriteKey


class DrawingSystem:

    def __init__(self, spriteSetId = 0):
        try:
            self._textures = { SpriteKey.lynSpriteSheet : SpriteSheet("lynSpriteSheet.gif"),
                           SpriteKey.lynStanding      : SpriteSheet("lynSprite.gif"),
                           SpriteKey.brigandSpriteSheet : SpriteSheet("brigandSprite.gif"),
                           SpriteKey.brigandStanding  : SpriteSheet("brigandSprite.gif"),
                           SpriteKey.lynRunning  : SpriteSheet("lynRunSprite.gif")}
        except KeyError:
            print "\n---DrawingSystem.py: SpriteKey not found---"
            raise SystemExit

    def draw(self, entities, surface):
        surface.fill(Color('black'))
        for entity in entities:
            #try:
            surface.blit(self._textures[entity.state.spriteComponent.spriteKey].getImage(entity.state.spriteComponent.spriteRect), entity.state.geometryComponent.location)
            #except AttributeError:
            #    pass
        display.update()


    def _getPointList(self, entity):
        xpos = entity.state.geometryComponent.location[0]
        ypos = entity.state.geometryComponent.location[1]
        width = entity.state.geometryComponent.width
        height = entity.state.geometryComponent.height
        angle = entity.state.geometryComponent.angle

        return  [ (xpos , ypos), (int(xpos + width*cos(angle)), int(ypos + width*sin(angle))), (int(xpos + width*cos(angle) - height*sin(angle)), int(ypos + height*cos(angle) + width*sin(angle))), (int(xpos - height*sin(angle)), int(ypos + height*cos(angle))) ]

