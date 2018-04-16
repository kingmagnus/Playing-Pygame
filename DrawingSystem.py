
from pygame import display
from pygame import Color

from SpriteSheet import SpriteSheet
from EntityRegister import EntityRegister

import SpriteKey

class DrawingSystem:

    def __init__(self, spriteSetId = 0):
        self.__spriteRegister = EntityRegister(('spriteComponent', 'geometryComponent'))
        #__rectRegister = EntityRegister('rectComponent', 'geometryComponent')
        try:
            self._textures = { SpriteKey.lynSpriteSheet : SpriteSheet("lynSpriteSheet.gif"),
                           SpriteKey.lynStanding      : SpriteSheet("lynSprite.gif"),
                           SpriteKey.brigandSpriteSheet : SpriteSheet("brigandSprite.gif"),
                           SpriteKey.brigandStanding  : SpriteSheet("brigandSprite.gif"),
                           SpriteKey.lynRunning  : SpriteSheet("lynRunSprite.gif")}
        except KeyError as error:
            print ("\n---DrawingSystem.py: SpriteKey not found---")
            print (error)
            raise SystemExit

    def draw(self, entities, surface):
        surface.fill(Color('black'))
        self.__drawSprites(surface, entities)
        display.update()

    def registerEntities(self, entities, startId):
        self.__spriteRegister.registerEntities(entities, startId)
        print ("drawing system registered", self.__spriteRegister.size() ,"entities")

    def __drawSprites(self, surface, entities):
        for i in self.__spriteRegister:
            surface.blit(self._textures[entities[i].state.spriteComponent.spriteKey].getImage(entities[i].state.spriteComponent.spriteRect), entities[i].state.geometryComponent.location)

