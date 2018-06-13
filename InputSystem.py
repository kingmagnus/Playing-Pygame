
from InputMapper import InputMapper
from FSM import FSM
from FSMGraphFactory import GraphIDs, FSMGraphFactory
from Observer import Observer, Event, Publisher

class InputSystem(Observer, Publisher):
    """
        This system takes raw inpout from the keyboard and translates into actions 
        and states held in an instance of "InputMapper".

        All code to do so is held within the InputMapper.
    """
    def __init__(self, inputComponents, velocityComponents):
        Observer.__init__(self)
        Publisher.__init__(self)
        self.inputComponents = inputComponents
        self.velocityComponents = velocityComponents
        self.inputMapper  = InputMapper()

        self.fsm = FSM()
        FSMGraphFactory(self.fsm, GraphIDs.Moving)

    def handleInput(self):
        mappedInput = self.inputMapper.MapInput()
        for ID in self.inputComponents:
            if self.fsm.run(mappedInput, inputComponent = self.inputComponents[ID], velocityComponent = self.velocityComponents[ID]):
                inputEvent = Event()
                inputEvent.entityID = ID
                self.fsm.transitionFunctions.process(inputEvent)
                self.publishEvent(inputEvent)