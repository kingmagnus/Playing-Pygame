
import SpriteKey

from pygame import Rect
from InputConstants import InputConstants

def NoReaction(entity):
    pass

def RunUp(mapedInput, entities):
    if not mapedInput[InputConstants.State.Up]:
        return False
    for e in entities:
        try:
            e.state.inputComponent
        except AttributeError:
            continue
        try:
            e.state.velocityComponent
            e.state.velocityComponent.direction[1] -= 1
        except AttributeError as error:
            print ("\n---AttributeError Commands.py RunUp: entity", e.id, " with no velocityComponent---")
            print (error)
            raise SystemExit
        return True

def RunDown(mapedInput, entities):
    if not mapedInput[InputConstants.State.Down]:
        return False
    for e in entities:
        try:
            e.state.inputComponent
        except AttributeError:
            continue
        try:
            e.state.velocityComponent.direction[1] += 1
        except AttributeError as error:
            print ("\n---AttributeError Commands.py RunDown: entity", e.id, " with no velocityComponent---")
            print (error)
            raise SystemExit
        return True

def RunLeft(mapedInput, entities):
    if not mapedInput[InputConstants.State.Left]:
        return False
    if mapedInput[InputConstants.State.Right]:
        return False
    for e in entities:
        try:
            e.state.inputComponent
        except AttributeError:
            continue
        try:
            e.state.velocityComponent.direction[0] -= 1
        except AttributeError as error:
            print ("\n---AttributeError Commands.py RunLeft: entity", e.id, "with no velocityComponent---")
            print (error)
            raise SystemExit
        try:
            e.state.spriteComponent.spriteKey = SpriteKey.lynRunning
            e.state.spriteComponent.spriteRect = Rect(0,0,64,30)
        except AttributeError as error:
            print ("\n---AttributeError Commands.py RunLeft: entity", e.id, " with no spriteComponent---")
            print (error)
            raise SystemExit
        return True

def RunRight(mapedInput, entities):
    if not mapedInput[InputConstants.State.Right]:
        return False
    if mapedInput[InputConstants.State.Left]:
        return False
    for e in entities:
        try:
            e.state.inputComponent
        except AttributeError:
            continue

        try:
            e.state.velocityComponent.direction[0] +=  1
        except AttributeError as error:
            print ("\n---AttributeError Commands.py RunRight: entity", e.id, " with no velocityComponent---")
            print (error)
            raise SystemExit
        try:
            e.state.spriteComponent.spriteKey = SpriteKey.lynRunning
            e.state.spriteComponent.spriteRect = Rect(0,0,64,30)
        except AttributeError as error:
            print ("\n---AttributeError Commands.py RunRight: entity", e.id, " with no spriteComponent---\n")
            print (error)
            raise SystemExit
        return True


