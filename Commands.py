
import SpriteKey
import StateKey
import InputReactionMaps as IRM
from pygame import Rect

def NoReaction(entity):
    pass

def RunUp(entity):
    """try:
        entity.state.velocityComponent.direction[1] = entity.state.velocityComponent.direction[1] - 1
    except AttributeError:
        print "\n---Commands.py - RunUp: entity", entity.id, " with no velocityComponent---"
        raise SystemExit"""
    pass

def RunDown(entity):
    """try:
        entity.state.velocityComponent.direction[1] = entity.state.velocityComponent.direction[1] + 1
    except AttributeError:
        print "\n---Commands.py - RunDown: entity", entity.id, " with no velocityComponent---"
        raise SystemExit"""
    pass

def RunLeft(entity):
    try:
        entity.state.velocityComponent.direction[0] = entity.state.velocityComponent.direction[0] - 1
    except AttributeError:
        print "\n---Commands.py - RunLeft: entity", entity.id, "with no velocityComponent---"
        raise SystemExit
    try:
        entity.state.spriteComponent.spriteKey = SpriteKey.lynRunning
        entity.state.spriteComponent.spriteRect = Rect(0,0,64,30)
    except AttributeError:
        print "\n---Commands.py - RunLeft: entity", entity.id, " with no spriteComponent---"
        raise SystemExit
    try:
        entity.state.inputComponent.reactions = IRM.getInputReactionKeyMap(StateKey.PlayerRunningLeft)
    except AttributeError:
        print "\n---Commands.py - RunLeft: entity", entity.id, " with no inputComponent---\n(Can alos be a statekey error, look up how to tell)"
        raise SystemExit

def RunRight(entity):
    try:
        entity.state.velocityComponent.direction[0] = entity.state.velocityComponent.direction[0] + 1
    except AttributeError:
        print "\n---Commands.py - RunRight: entity", entity.id, " with no velocityComponent---"
        raise SystemExit
    try:
        entity.state.spriteComponent.spriteKey = SpriteKey.lynRunning
        entity.state.spriteComponent.spriteRect = Rect(0,0,64,30)
    except AttributeError:
        print "\n---Commands.py - RunRight: entity", entity.id, " with no spriteComponent---\n"
        raise SystemExit
    try:
        entity.state.inputComponent.reactions = IRM.getInputReactionKeyMap(StateKey.PlayerRunningRight)
    except AttributeError:
        print "\n---Commands.py - RunRight: entity", entity.id, " with no inputComponent---\n(Can alos be a statekey error, look up how to tell)"
        raise SystemExit

def Stand(entity):
    try:
        entity.state.velocityComponent.direction = [0,0]
    except AttributeError:
        print "\n---Commands.py - Stand: entity", entity.id, " with no velocityComponent---"
        raise SystemExit
    try:
        entity.state.spriteComponent.spriteKey = SpriteKey.lynStanding
        entity.state.spriteComponent.spriteRect = Rect(0,0,21,35)
    except AttributeError:
        print "\n---Commands.py - Stand: entity", entity.id, " with no spriteComponent---\n"
        raise SystemExit
    try:
        entity.state.inputComponent.reactions = IRM.getInputReactionKeyMap(StateKey.PlayerStanding)
    except AttributeError:
        print "\n---Commands.py - Stand: entity", entity.id, " with no inputComponent---\n(Can alos be a statekey error, look up how to tell)"
        raise SystemExit

def Duck(entity):
    try:
        entity.state.velocityComponent.direction = [0,0]
    except AttributeError:
        print "\n---Commands.py - Duck: entity", entity.id, " with no velocityComponent---"
        raise SystemExit
    try:
        entity.state.spriteComponent.spriteKey = SpriteKey.lynStanding
        entity.state.spriteComponent.spriteRect = Rect(0,0,21,35)
    except AttributeError:
        print "\n---Commands.py - Duck: entity", entity.id, " with no spriteComponent---\n"
        raise SystemExit
    try:
        entity.state.inputComponent.reactions = IRM.getInputReactionKeyMap(StateKey.PlayerDucking)
    except AttributeError:
        print "\n---Commands.py - Duck: entity", entity.id, " with no inputComponent---\n(Can alos be a statekey error, look up how to tell)"
        raise SystemExit



