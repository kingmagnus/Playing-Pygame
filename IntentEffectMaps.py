
from pygame import Rect
from IntentMapper import IntentConstants
import SpriteKey

class SpriteIntentMaps:
    __LynSpriteSheetRectIntentDict = {
        IntentConstants.RunRight : Rect(35,0,35,45),
        IntentConstants.RunLeft : Rect(35,0,35,45),
        IntentConstants.StopRunningRight : Rect(0,0,35,45),
        IntentConstants.StopRunningLeft : Rect(0,0,35,45),
        None : Rect(0,0,35,45)
    }


    __maps = {
       SpriteKey.lynSpriteSheet : __LynSpriteSheetRectIntentDict
    }

    def __getitem__(self, SpriteKey):
        try:
            return self.__maps[SpriteKey]
        except IndexError as error:
            print ("IndexError: SpriteKey", SpriteKey, " not in __maps within IntentSpriteMaps")
            print(error)
            raise SystemExit

class AccelIntentMaps:
    def __init__(self):
        self.__runRightLeftDict = {
            IntentConstants.RunRight : self.runRightFn,
            IntentConstants.RunLeft : self.runLeftFn,
            IntentConstants.StopRunningRight : self.StopRunRightFn,
            IntentConstants.StopRunningLeft : self.StopRunLeftFn,
            None : self.NoneFn
        }

        self.__maps = {
           "Run" : self.__runRightLeftDict,
        }

    def __getitem__(self, Key):
        try:
            return self.__maps[Key]
        except IndexError as error:
            print ("IndexError: SpriteKey", SpriteKey, " not in __maps within IntentSpriteMaps")
            print(error)
            raise SystemExit


    def runRightFn(self, entity):
        print "runRightFn called"
        if entity.state.velocityComponent.vx >= entity.state.velocityComponent.maxSpeed:
            entity.state.accelerationComponent.ax = 0
        else:
            entity.state.accelerationComponent.ax = 1

    def runLeftFn(self, entity):
        print "runLeftFn called"
        if entity.state.velocityComponent.vx <= -entity.state.velocityComponent.maxSpeed:
            entity.state.accelerationComponent.ax = 0
        else:
            entity.state.accelerationComponent.ax = -1

    def StopRunRightFn(self, entity):
        print "StopRunningRightFn called"
        if entity.state.velocityComponent.vx > 0:
            entity.state.accelerationComponent.ax = -1
        if entity.state.velocityComponent.vx < 0:
            entity.state.velocityComponent.vx = 0
            entity.state.accelerationComponent.ax = 0


    def StopRunLeftFn(self, entity):
        print "StopRunLeftFn called"
        if entity.state.velocityComponent.vx < 0:
            entity.state.accelerationComponent.ax = 1
        if entity.state.velocityComponent.vx > 0:
            entity.state.velocityComponent.vx = 0
            entity.state.accelerationComponent.ax = 0

    def NoneFn(self, entity):
        print "NoneFn called"
        if entity.state.velocityComponent.vx > 0:
             self.StopRunRightFn(entity) 
        if entity.state.velocityComponent.vx < 0:
             self.StopRunLeftFn(entity)