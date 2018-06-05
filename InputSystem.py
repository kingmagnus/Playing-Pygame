
from InputMapper import InputMapper
from EntityRegister import EntityRegister
from FSM import FSM
from FSMGraphFactory import GraphIDs, FSMGraphFactory
from Observer import Observer, Event, Publisher

class InputSystem(Observer, Publisher):
    """
        This system takes raw inpout from the keyboard and translates into actions 
        and states held in an instance of "InputMapper".

        All code to do so is held within the InputMapper.
    """
    def __init__(self, entities):
        Observer.__init__(self)
        Publisher.__init__(self)
        self.entities = entities
        self.__inputRegister = EntityRegister('inputComponent')
        self.inputMapper  = InputMapper()

        self.fsm = FSM()
        FSMGraphFactory(self.fsm, GraphIDs.Moving)

    def registerEntities(self):
        self.__inputRegister.registerEntities(self.entities)
        print "input Register", self.__inputRegister

    def handleInput(self):
        mappedInput = self.inputMapper.MapInput()
        for i in self.__inputRegister:
            if self.fsm.run(mappedInput, self.entities[i]):
                inputEvent = Event()
                inputEvent.entityID = i
                self.fsm.transitionFunctions.process(inputEvent)
                self.publishEvent(inputEvent)