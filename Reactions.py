
import InputKey
import ReactionKey

# list of reaction dictionaries
# Use the map with a playerState id to return a function which will build the relevant dict mapping keys to actions for the given state 

playerStanding = 0
#Also appears in InputComponent, this will evetualy go into a "key" class to list the states of input that can be called

def _playerStandingMap():
    return {InputKey.Map[InputKey.UP]    : ReactionKey.AccelerateUp   ,
            InputKey.Map[InputKey.DOWN]  : ReactionKey.AccelerateDown ,
            InputKey.Map[InputKey.LEFT]  : ReactionKey.AccelerateLeft ,
            InputKey.Map[InputKey.RIGHT] : ReactionKey.AccelerateRight}

Map = { playerStanding :  _playerStandingMap}
