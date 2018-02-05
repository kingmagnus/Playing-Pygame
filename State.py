

from Components import *


STANDING = "Standing"
JUMPING  = "Jumping"


class State:

    def __init__(self, state = STANDING):


        self._InputComponent = InputComponent[STANDING]()
        self._GraphicsComponent = GraphicsComponent[STANDING]()
        #self._physicsComponent = PhyicsComponent()

        #draw is a pointer to the function update in _graphicsComponent
        #draw is called in entity draw
        self.draw = self._GraphicsComponent.update
        #handleInput is called in world update where the command queue is passed to the input conponent where the input component looks at the current state of keys ect and adds the relevant commands to the queue.
        self.handleInput = self._InputComponent.update

        #self.handlePhyics = self._PhysicsComponent.update

    def changeState(self, state):
        self._InputComponent = InputComponent[state]()
        self._GraphicsComponent = GraphicsComponent[state]()        
        self.draw = self._GraphicsComponent.update
        self.handleInput = self._InputComponent.update
