

from FSMStateFactory import StateIDs, StateFactory
from FSMTransFns import TransFns, TestFns


class GraphIDs:
    Moving = "Moving"

def FSMGraphFactory(fsm, graphID):
    """
    Will make a graph in the FSM corrisponding to the ID.

    Arguments
    ---------
        fsm - a FSM instance
        ID - StateIDs member - the ide of the produced state
    """
    try:
        __graphDict[graphID](fsm)
    except KeyError, message:
        print "FSMGraphFactory - graphID", graphID, "not found in __graphDict:"
        print  __graphDict
        raise KeyError, message
    
def Moving(fsm):

    fsm.addState(StateIDs.Running)
    fsm.addState(StateIDs.Standing)
    fsm.addState(StateIDs.StartRunning)
    fsm.addState(StateIDs.StopRunning)
    
    #fsm.addTransition(self, startID, endID, tansitionReqFn, transitionFn = None):

    fsm.addTransition(StateIDs.Standing,    StateIDs.StartRunning,    (TestFns.State_Right,),    (TransFns.Right,))
    fsm.addTransition(StateIDs.Standing,    StateIDs.StartRunning,    (TestFns.State_Left,),    (TransFns.Left,))

    fsm.addTransition(StateIDs.StartRunning,    StateIDs.Running,    (TestFns.State_Right,TestFns.Vel_Max),    (TransFns.Right,))
    fsm.addTransition(StateIDs.StartRunning,    StateIDs.Running,    (TestFns.State_Left,TestFns.Vel_Max),    (TransFns.Left,))
    fsm.addTransition(StateIDs.StartRunning,    StateIDs.StopRunning,    (TestFns.NoInput,),    (TransFns.Left,))


    fsm.addTransition(StateIDs.Running,    StateIDs.StopRunning,    (TestFns.State_Left, TestFns.Vel_Right),    (TransFns.Left,))
    fsm.addTransition(StateIDs.Running,    StateIDs.StopRunning,    (TestFns.State_Right, TestFns.Vel_Left),    (TransFns.Right,))
    fsm.addTransition(StateIDs.Running,    StateIDs.StopRunning,    (TestFns.NoInput,TestFns.Vel_Right),    (TransFns.Left,))
    fsm.addTransition(StateIDs.Running,    StateIDs.StopRunning,    (TestFns.NoInput,TestFns.Vel_Left),    (TransFns.Right,))

    fsm.addTransition(StateIDs.StopRunning,    StateIDs.Standing,    (TestFns.State_Left,),    (TransFns.Left,))
    fsm.addTransition(StateIDs.StopRunning,    StateIDs.Standing,    (TestFns.State_Right,),    (TransFns.Right,))
    fsm.addTransition(StateIDs.StopRunning,    StateIDs.Standing,    (TestFns.NoInput,),    ())

__graphDict = {
    GraphIDs.Moving : Moving
}