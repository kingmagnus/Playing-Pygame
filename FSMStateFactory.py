
class State(object):
    """
        class for holding a node in the fsm
    
    Member Variables
    ----------------
        entryFn :
            the function called when the state becomes the active state.
        exitFn :
            the function called when the state is nolonger the active state.
        transitions :
            a list of transition objects defining the exits of the state

    Member Functions
    ----------------
        addTransition:
            Will add a transition to the state, stored in tansitions
    """
    __slots__ = "entryFn", "exitFn", "transitions"
    def __init__(self):
        self.transitions = []
    def entryFn(self, event):
        event.entryState = "Standing"
    def exitFn(self, event):
        event.exitState = "Standing"

    def addTransition(self, endID, testFns, transitionFns):
        """
        Will add a transition to the state, stored in tansitions

        Arguments
        ---------
            endID - member of StateIDs, the id of the node transitioned to
            tansitionReqFn - the function callecd to check transition
            transitionFn - the function called upon transition
        """
        self.transitions.append(Transition(endID, testFns, transitionFns))

class Transition(object):
    """
    holds the information for which state can be moved to, the requiremnt function to judge
    if transition is posible, and the trnasition function to be called when requirement is met.
    """
    __slots__ = "endID", "testFns", "transitionFns"
    def __init__(self, endID, testFns, transitionFns):
        self.endID = endID
        self.testFns = testFns
        self.transitionFns = transitionFns



class StateIDs(object):
    """
    List of IDs for the states
    """
    Running = "Running"
    Standing = "Standing"
    StartRunning = "StartRunning"
    StopRunning = "StopRunning"
    Turn = "Turn"


def StateFactory(ID):
    """
    Will return a state with the appropriate entry and exit function.

    Arguments
    ---------
        ID - StateIDs member - the ide of the produced state
    """
    mState = stateDict[ID]()
    mState.ID = ID

    return mState

class Standing(State):
    def __init__(self):
        pass
        self.transitions = []
    def entryFn(self, event):
        print "enter standing"
        event.entryState = "Standing"
    def exitFn(self, event):
        event.exitState = "Standing"

class Running(State):
    def __init__(self):
        State.__init__(self)
    def entryFn(self, event):
        print "enter Running"
        event.entryState = "Running"
    def exitFn(self, event):
        event.exitState = "Running"

class StartRunning(State):
    def __init__(self):
        State.__init__(self)
    def entryFn(self, event):
        print "enter StartRunning"
        event.entryState = "StartRunning"
    def exitFn(self, event):
        event.exitState = "StartRunning"

class StopRunning(State):
    def __init__(self):
        State.__init__(self)
    def entryFn(self, event):
        print "enter StopRunning"
        event.entryState = "StopRunning"
    def exitFn(self, event):
        event.exitState = "StopRunning"

stateDict = {
                StateIDs.Running : Running, 
                StateIDs.Standing : Standing, 
                StateIDs.StartRunning : StartRunning, 
                StateIDs.StopRunning : StopRunning, 
            }