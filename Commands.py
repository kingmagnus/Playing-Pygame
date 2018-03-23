
import SpriteKey
import StateKey

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
            e.state.velocityComponent.direction[1] = entity.state.velocityComponent.direction[1] - 1
        except AttributeError:
            print "\n---AttributeError Commands.py RunUp: entity", entity.id, " with no velocityComponent---"
            raise SystemExit
        return True

def RunDown(entity):
    if not mapedInput[InputConstants.State.Down]:
        return False
    for e in entities:
        try:
            e.state.inputComponent
        except AttributeError:
            continue
        try:
            e.state.velocityComponent.direction[1] = entity.state.velocityComponent.direction[1] + 1
        except AttributeError:
            print "\n---AttributeError Commands.py RunDown: entity", entity.id, " with no velocityComponent---"
            raise SystemExit
        return True

def RunLeft(entity):
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
            e.state.velocityComponent.direction[0] = entity.state.velocityComponent.direction[0] - 1
        except AttributeError:
            print "\n---AttributeError Commands.py RunLeft: entity", entity.id, "with no velocityComponent---"
            raise SystemExit
        try:
            e.state.spriteComponent.spriteKey = SpriteKey.lynRunning
            e.state.spriteComponent.spriteRect = Rect(0,0,64,30)
        except AttributeError:
            print "\n---AttributeError Commands.py RunLeft: entity", entity.id, " with no spriteComponent---"
            raise SystemExit
        return True

def RunRight(entity):
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
            entity.state.velocityComponent.direction[0] = entity.state.velocityComponent.direction[0] + 1
        except AttributeError:
            print "\n---AttributeError Commands.py RunRight: entity", entity.id, " with no velocityComponent---"
            raise SystemExit
        try:
            entity.state.spriteComponent.spriteKey = SpriteKey.lynRunning
            entity.state.spriteComponent.spriteRect = Rect(0,0,64,30)
        except AttributeError:
            print "\n---AttributeError Commands.py RunRight: entity", entity.id, " with no spriteComponent---\n"
            raise SystemExit
        return True


