
from pygame import display
from pygame import Color
import pygame 
from math import cos, sin

from SpriteSheet import SpriteSheet
import SpriteKey
from System import EntityRegister

class DrawingSystem:

    def __init__(self, spriteSetId = 0):
        __drawingRegister = EntityRegister('spriteComponent', 'geometryComponent')
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
        for i in __drawingRegister:
            surface.blit(self._textures[entities[i].state.spriteComponent.spriteKey].getImage(entities[i].state.spriteComponent.spriteRect), entities[i].state.geometryComponent.location)

        display.update()


