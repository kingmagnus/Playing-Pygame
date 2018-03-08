
import InputKey
import ReactionKey
import StateKey

# list of reaction dictionaries
# Use the map with a playerState id to return a function which will build the relevant dict mapping keys to actions for the given state 

_pressed = True

def _playerStandingMap():
    try:    
        return {#InputKey.Map[InputKey.UP]    : (_pressed, ReactionKey.RunUp),
                InputKey.Map[InputKey.DOWN]  : (_pressed, ReactionKey.Duck),
                InputKey.Map[InputKey.LEFT]  : (_pressed, ReactionKey.RunLeft),
                InputKey.Map[InputKey.RIGHT] : (_pressed, ReactionKey.RunRight)}
    except KeyError:
        print "\n---Reactions.py: InputKey not found in InputKey.Map for playerStandingMap---"
        raise SystemExit
    
def _playerRunningLeftMap():
    try:    
        return {#InputKey.Map[InputKey.UP]    : (_pressed, ReactionKey.RunUp),
                InputKey.Map[InputKey.DOWN]  : (_pressed, ReactionKey.RunDown),
                InputKey.Map[InputKey.LEFT]  : (not _pressed, ReactionKey.Stand),
                InputKey.Map[InputKey.RIGHT] : (_pressed, ReactionKey.RunRight)}
    except KeyError:
        print "\n---Reactions.py: InputKey not found in InputKey.Map for playerRunningLeftMap---"
        raise SystemExit

def _playerRunningRightMap():
    try:    
        return {#InputKey.Map[InputKey.UP]    : (_pressed, ReactionKey.RunUp),
                InputKey.Map[InputKey.DOWN]  : (_pressed, ReactionKey.RunDown),
                InputKey.Map[InputKey.LEFT]  : (_pressed, ReactionKey.RunLeft),
                InputKey.Map[InputKey.RIGHT] : (not _pressed, ReactionKey.Stand)}
    except KeyError:
        print "\n---Reactions.py: InputKey not found in InputKey.Map for playerRunningRightMap---"
        raise SystemExit

def _playerDuckingMap():
    try:    
        return {#InputKey.Map[InputKey.UP]    : (_pressed, ReactionKey.RunUp),
                InputKey.Map[InputKey.DOWN]  : (not _pressed, ReactionKey.Stand),
                InputKey.Map[InputKey.LEFT]  : (_pressed, ReactionKey.RunLeft),
                InputKey.Map[InputKey.RIGHT] : (_pressed, ReactionKey.RunRight)}
    except KeyError:
        print "\n---Reactions.py: InputKey not found in InputKey.Map for playerDuckingMap---"
        raise SystemExit


_Map = { StateKey.PlayerStanding : _playerStandingMap,
         StateKey.PlayerRunningLeft : _playerRunningLeftMap,
         StateKey.PlayerRunningRight : _playerRunningRightMap
         StateKey.PlayerDucking : _playerDuckingMap}

def getInputReactionKeyMap(stateKey):
    try:
        return _Map[stateKey]()
    except KeyError:
        print "\n---Reactions.py - getInputReactionKeyMap: stateKey", stateKey, "not in _Map---"
        raise SystemExit
