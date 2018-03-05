
from SpriteComponent import SpriteComponent
from GeometryComponent import GeometryComponent
from VelocityComponent import VelocityComponent
from CollisionComponent import CollisionComponent
from InputComponent import InputComponent

from pygame import Rect

NONE     = "None"
PLAYER_STANDING = "Player Standing"
PLAYER_JUMPING  = "Player Jumping"
ENEMY_STANDING = "Enemy Standing"
FLOOR = "Floor"

lynSpriteSheet = "lynSpriteSheet"
lynStanding      = "lynStanding"
brigandSpriteSheet = "brigandSpriteSheet"
brigandStanding = "brigandStanding"

class State:
    None

class StateFactory:
    
    def __init__(self):       
        self._states = { NONE            : State,
                        PLAYER_STANDING : self._PlayerStandingState,
                        PLAYER_JUMPING  : self._PlayerStandingState,
                        ENEMY_STANDING  : self._EnemyStandingState,
                        FLOOR           : self._FloorState
                      }

    def getState(self, stateID):
        try:
            return self._states[stateID]
        except KeyError:
            print "--- stateID not in state Dict ---"
            raise SystemExit
        

    def _PlayerStandingState(self):
        state = State()
        state.inputComponent = InputComponent()
        state.spriteComponent = SpriteComponent(lynStanding, Rect(0,0,21,35))
        state.velocityComponent = VelocityComponent(120,[0,0])
        state.geometryComponent = GeometryComponent([0,0], 21, 35)
        state.collisionComponent = CollisionComponent()
        return state

    def _EnemyStandingState(self):
        state = State()
        state.spriteComponent = SpriteComponent(brigandStanding, Rect(0,0,36,33))
        state.velocityComponent = VelocityComponent(120,[0,0])
        state.geometryComponent = GeometryComponent([0,0], 36, 33)
        state.collisionComponent = CollisionComponent()
        return state

    def _FloorState(self):
        state = State()
        state.geometryComponent = GeometryComponent([100,300],100,10)
        state.collisionComponent = CollisionComponent()
        state.polygonComponent = True
        return state
        








