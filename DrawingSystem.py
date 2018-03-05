
from pygame import display
from pygame import Color
import pygame 
from math import cos, sin

from SpriteSheet import SpriteSheet

lynSpriteSheet = "lynSpriteSheet"
lynStanding      = "lynStanding"
brigandSpriteSheet = "brigandSpriteSheet"
brigandStanding = "brigandStanding"

class DrawingSystem:

    def __init__(self, spriteSetId = 0):
        self._textures = { lynSpriteSheet : SpriteSheet("lynSpriteSheet.gif"),
                           lynStanding      : SpriteSheet("lynSprite.gif"),
                           brigandSpriteSheet : SpriteSheet("brigandSprite.gif"),
                           brigandStanding  : SpriteSheet("brigandSprite.gif")
                         }

    def draw(self, entities, surface):
        surface.fill(Color('black'))
        for entity in entities:
            try:
                surface.blit(self._textures[entity.state.spriteComponent.spriteID].getImage(entity.state.spriteComponent.spriteRect), entity.state.geometryComponent.location)
            except AttributeError:
            #try:
                entity.state.polygonComponent
                pygame.draw.polygon(surface, Color('red'), self._getPointList(entity))
            #except AttributeError:
                #continue
        display.update()


    def _getPointList(self, entity):
        xpos = entity.state.geometryComponent.location[0]
        ypos = entity.state.geometryComponent.location[1]
        width = entity.state.geometryComponent.width
        height = entity.state.geometryComponent.height
        angle = entity.state.geometryComponent.angle

        return  [ (xpos , ypos), (int(xpos + width*cos(angle)), int(ypos + width*sin(angle))), (int(xpos + width*cos(angle) - height*sin(angle)), int(ypos + height*cos(angle) + width*sin(angle))), (int(xpos - height*sin(angle)), int(ypos + height*cos(angle))) ]

