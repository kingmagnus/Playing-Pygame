
from pygame import display
from pygame import Color
from pygame import Rect, draw

from SpriteSheet import SpriteSheet
from EntityRegister import EntityRegister

import SpriteKey
from Observer import Observer


class DrawingSystem(Observer):

    def __init__(self, positionComponents, spriteComponents, geometryComponents):
        self.spriteComponents = spriteComponents
        self.positionComponents = positionComponents
        self.geometryComponents = geometryComponents

        try:
            self.__texturesDict = { 
                SpriteKey.lynSpriteSheet : SpriteSheet("lynSpriteSheet.gif"),
                SpriteKey.lynStanding : SpriteSheet("lynSprite.gif"),
                SpriteKey.brigandSpriteSheet : SpriteSheet("brigandSprite.gif"),
                SpriteKey.brigandStanding : SpriteSheet("brigandSprite.gif"),
                SpriteKey.lynRunning : SpriteSheet("lynRunSprite.gif")
            }
            self.__spriteRectDict = { 
                SpriteKey.lynSpriteSheet : Rect(0,0,36,33),
                SpriteKey.lynStanding : Rect(0,0,33,44),
                SpriteKey.brigandSpriteSheet : Rect(0,0,36,33),
                SpriteKey.brigandStanding : Rect(0,0,37,46),
                SpriteKey.lynRunning : Rect(0,0,52,51),
            }
        except KeyError as error:
            print("\n---DrawingSystem.py: SpriteKey not found---")
            print(error)
            raise SystemExit

    def draw(self, surface):
        surface.fill(Color('black'))
        self.__drawSprites(surface)
        self.__drawCollRect(surface)
        display.update()

    def __drawSprites(self, surface):
        for ID in self.spriteComponents.keys():
            try:
                key = self.spriteComponents[ID].spriteKey
                loc = self.positionComponents[ID]
            except KeyError, message:
                print "\nEntity id", ID," in spriteComponents but not positionComponents\n"
                print "spriteComponents\n", self.spriteComponents
                print "positionComponents\n", self.positionComponents
                raise KeyError, message
            try:
                surface.blit(self.__texturesDict[key].getImage(self.__spriteRectDict[key]), [loc.x, loc.y])
            except KeyError, message:
                if key not in self.__texturesDict.keys():
                    print "\nspriteKey", key, "not found in __texturesDict"
                if key not in self.__spriteRectDict.keys():
                    print "\nspriteKey", key, "not found in __spriteRectDict"
                raise KeyError, message



    def __drawCollRect(self, surface):
        for ID in self.spriteComponents.keys():
            loc = self.positionComponents[ID]
            geom = self.geometryComponents[ID]
            draw.rect(surface, Color('red'), Rect(loc.x, loc.y, geom.width, geom.height), 1)


    def processEvent(self, event):
        if event.entryState == "Standing":
            self.spriteComponents[event.entityID].spriteKey = SpriteKey.lynStanding
            
        if event.entryState == "Running" and event.direction == "Right":
            self.spriteComponents[event.entityID].spriteKey = SpriteKey.lynRunning

        if event.entryState == "Running" and event.direction == "Left":
            self.spriteComponents[event.entityID].spriteKey = SpriteKey.lynRunning
                


            