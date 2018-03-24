
from SpriteComponent import SpriteComponent
from GeometryComponent import GeometryComponent
from VelocityComponent import VelocityComponent
from CollisionComponent import CollisionComponent
from InputComponent import InputComponent

import StateKey
import SpriteKey

from pygame import Rect

class State:
    None

class StateFactory:
    
    def __init__(self): 
        try:      
            self._states = {StateKey.Empty          : State,
                            StateKey.PlayerStanding : self._PlayerStandingState,
                            StateKey.PlayerJumping  : self._PlayerStandingState,
                            StateKey.EnemyStanding  : self._EnemyStandingState,
                            StateKey.Floor          : self._FloorState,
                            StateKey.PlayerRunningLeft  : self._PlayerRunningLeftState,
                            StateKey.PlayerRunningRight : self._PlayerRunningRightState}
        except AttributeError as error:
            print ("\n---StateFactory.py: factory function or stateKey not defined---\n(work out how to say which)")
            print (error)
            raise SystemExit


    def getState(self, stateKey):
        try:
            return self._states[stateKey]()
        except KeyError as error:
            print ("\n---StateFactory.py: stateKey", stateKey, "not in _states---")
            print (error)
            raise SystemExit
        
        

    def _PlayerStandingState(self):
        state = State()
        state.inputComponent = InputComponent()
        state.spriteComponent = SpriteComponent(SpriteKey.lynStanding, Rect(0,0,21,35))
        state.velocityComponent = VelocityComponent(0,0,120)
        state.geometryComponent = GeometryComponent([0,0], 21, 35)
        state.collisionComponent = CollisionComponent()
        return state

    def _EnemyStandingState(self):
        state = State()
        state.spriteComponent = SpriteComponent(SpriteKey.brigandStanding, Rect(0,0,36,33))
        state.velocityComponent = VelocityComponent(0,0,120)
        state.geometryComponent = GeometryComponent([0,0], 36, 33)
        state.collisionComponent = CollisionComponent()
        return state

    def _FloorState(self):
        state = State()
        state.geometryComponent = GeometryComponent([100,300],100,10)
        state.collisionComponent = CollisionComponent()
        state.polygonComponent = True
        return state

    def _PlayerRunningLeftState():
        state = State()
        state.inputComponent = InputComponent()
        state.spriteComponent = SpriteComponent(SpriteKey.lynStanding, Rect(0,0,21,35))
        state.velocityComponent = VelocityComponent(0,0,120)
        state.geometryComponent = GeometryComponent([0,0], 21, 35)
        state.collisionComponent = CollisionComponent()
        return state
        
    def _PlayerRunningRightState():
        state = State()
        state.inputComponent = InputComponent()
        state.spriteComponent = SpriteComponent(SpriteKey.lynStanding, Rect(0,0,21,35))
        state.velocityComponent = VelocityComponent(0,0,120)
        state.geometryComponent = GeometryComponent([0,0], 21, 35)
        state.collisionComponent = CollisionComponent()
        return state







