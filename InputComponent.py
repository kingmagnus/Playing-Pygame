
import InputReactionMaps as IRM
import StateKey

class InputComponent:
    def __init__(self, stateKey = StateKey.PlayerStanding):
            self.reactions = IRM.getInputReactionKeyMap(stateKey)





