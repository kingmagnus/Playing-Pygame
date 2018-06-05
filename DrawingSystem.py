
from pygame import display
from pygame import Color
from pygame import Rect, draw

from SpriteSheet import SpriteSheet
from EntityRegister import EntityRegister

import SpriteKey
from Observer import Observer


class DrawingSystem(Observer):

    def __init__(self, entities, spriteSetId = 0):
        self.entities = entities
        self.__spriteRegister = EntityRegister('spriteComponent', 'geometryComponent')
        #__rectRegister = EntityRegister('rectComponent', 'geometryComponent')

        try:
            self.__textures = { 
                                SpriteKey.lynSpriteSheet : SpriteSheet("lynSpriteSheet.gif"),
                                SpriteKey.lynStanding      : SpriteSheet("lynSprite.gif"),
                                SpriteKey.brigandSpriteSheet : SpriteSheet("brigandSprite.gif"),
                                SpriteKey.brigandStanding  : SpriteSheet("brigandSprite.gif"),
                                SpriteKey.lynRunning  : SpriteSheet("lynRunSprite.gif")
                            }
            self.__spriteRect = { 
                SpriteKey.lynSpriteSheet : Rect(0,0,36,33),
                SpriteKey.lynStanding      : Rect(0,0,33,44),
                SpriteKey.brigandSpriteSheet : Rect(0,0,36,33),
                SpriteKey.brigandStanding  : Rect(0,0,37,46),
                SpriteKey.lynRunning  : Rect(0,0,52,51),
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

    def registerEntities(self):
        self.__spriteRegister.registerEntities(self.entities)
        print "DrawingSystem", self.__spriteRegister

    def __drawSprites(self, surface):
        for i in self.__spriteRegister:
            try:
                key = self.entities[i].state.spriteComponent.spriteKey
                loc = self.entities[i].state.geometryComponent.location
                surface.blit(self.__textures[key].getImage(self.__spriteRect[key]), loc)
            except IndexError, message:
                print "\nIndex", i," in spriteRegister out of range"
                print "spriteRegister", self.__spriteRegister
                print "len(entities)", len(self.entities)
                print "entities", self.entities, "\n"
                raise IndexError, message

    def __drawCollRect(self, surface):
        for i in self.__spriteRegister:
            e = self.entities[i]
            x = e.state.geometryComponent.location[0]
            y = e.state.geometryComponent.location[1]
            width = e.state.geometryComponent.width
            height = e.state.geometryComponent.height
            draw.rect(surface, Color('red'), Rect(x,y,width, height), 1)


    def processEvent(self, event):
        if event.entryState == "Standing":
            self.entities[event.entityID].state.spriteComponent.spriteKey = SpriteKey.lynStanding
            
        if event.entryState == "Running" and event.direction == "Right":
            self.entities[event.entityID].state.spriteComponent.spriteKey = SpriteKey.lynRunning

        if event.entryState == "Running" and event.direction == "Left":
            self.entities[event.entityID].state.spriteComponent.spriteKey = SpriteKey.lynRunning
                


            