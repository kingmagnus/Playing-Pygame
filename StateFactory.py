
from State import *
from Components import *
from SpriteSheet import *


NONE     = "None"
PLAYER_STANDING = "Player Standing"
PLAYER_JUMPING  = "Player Jumping"
ENEMY_STANDING = "Enemy Standing"

lynSpriteSheet = "lynSpriteSheet"
lynSprite      = "lynSprite"
brigandSpriteSheet = "brigandSpriteSheet"
brigandSprite = "brigandSprite"

class StateFactory:
    
    def __init__(self):

        self._textures = {lynSpriteSheet : SpriteSheet("lynSpriteSheet.gif"),
                          lynSprite      : SpriteSheet("lynSprite.gif"),
                          brigandSpriteSheet : SpriteSheet("brigandSprite.gif"),
                          brigandSprite  : SpriteSheet("brigandSprite.gif")}
       
        self.states = { NONE            : State,
                         PLAYER_STANDING : self._PlayerStandingState,
                         PLAYER_JUMPING  : self._PlayerStandingState,
                         ENEMY_STANDING  : self._EnemyStandingState}


    def _PlayerStandingState(self):
        state = State()
        state.InputComponent = InputComponent[STANDING]()
        state.GraphicsComponent = GraphicsComponent[STANDING]()
        state.GraphicsComponent.getSprite(self._textures[lynSprite].sprite_sheet)
        return state

    def _EnemyStandingState(self):
        state = State()
        state.GraphicsComponent = GraphicsComponent[STANDING]()
        state.GraphicsComponent.getSprite(self._textures[brigandSprite].sprite_sheet)
        return state


    

