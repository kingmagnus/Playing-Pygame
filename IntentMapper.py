
from InputConstants import InputConstants

class IntentMapIDs:
    Standing = 1
    RunRight = 2
    RunLeft  = 3
    StopRunningRight  = 4
    StopRunningLeft   = 5

class IntentConstants:
    RunRight          = 2
    RunLeft           = 4
    StopRunningRight  = 1
    StopRunningLeft   = 3

class IntentMapper:
    """
    Will take mappedInput and change it into intents using an intent map deffined through the passed ID

    Arguments
    ---------
    IntentID
        Pass a value from IntentMapIDs
    """
    __slots__ = '__IntentMap'
    def __init__(self):
        self.__IntentMap = intentMapFSM.getMap

    def mapInputToIntent(self, mappedInput):
        intent = [ iMap.Intent for iMap in self.__IntentMap if iMap.isSubset(mappedInput) ]
        if len(intent) != 0:
            self.setNewIntentMap(intent)
            return intent[0] 
        else:
            return None

    def setNewIntentMap(self, intent):
        self.__IntentMap = intentMapFSM(IntentMapID)

class IntentPair:
    __slots__ = 'States', 'Actions', 'Intent'

    def __init__(self, Intent, States = set(), Actions = set()):
        self.States  = States
        self.Actions = Actions
        self.Intent  = Intent

    def isSubset(self, mappedInput):
        if mappedInput.Actions>=self.Actions and mappedInput.States>=self.States:
            return True
        return False


class intentMapFSM:

    __RunRight = [
                    IntentPair(Intent = IntentConstants.RunRight, States = set((InputConstants.State.Right,)), Actions = set()),
                    IntentPair(Intent = IntentConstants.StopRunningRight, States = set((InputConstants.State.Left,)), Actions = set()),
                    IntentPair(Intent = IntentConstants.StopRunningRight, States = set(), Actions = set())
                ]

    __RunLeft = [
                    IntentPair(Intent = IntentConstants.RunLeft, States = set((InputConstants.State.Left,)), Actions = set()),
                    IntentPair(Intent = IntentConstants.StopRunningLeft, States = set((InputConstants.State.Right,)), Actions = set()),
                    IntentPair(Intent = IntentConstants.StopRunningLeft, States = set(), Actions = set())
                ]

    __StopRuningLeftMap = [
                    IntentPair(Intent = IntentConstants.RunLeft, States = set((InputConstants.State.Left,)), Actions = set()),
                    IntentPair(Intent = IntentConstants.StopRunningLeft, States = set((InputConstants.State.Right,)), Actions = set()),
                    IntentPair(Intent = IntentConstants.StopRunningLeft, States = set(), Actions = set())
                ]

    __StopRuningRightMap = [
                    IntentPair(Intent = IntentConstants.RunRight, States = set((InputConstants.State.Right,)), Actions = set()),
                    IntentPair(Intent = IntentConstants.StopRunningRight, States = set((InputConstants.State.Left,)), Actions = set()),
                    IntentPair(Intent = IntentConstants.StopRunningLeft, States = set(), Actions = set())
                ]

    getMap = {
            IntentConstants.RunLeft : __RunLeft,
            IntentConstants.RunRight : __RunRight,
            IntentConstants.StopRuningLeft : __StopRuningLeftMap,
            IntentConstants.StopRuningRight : __stopRuningRightMap,
            None : {}
        }