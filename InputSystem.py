
from InputMapper import InputMapper, ContextID
from EntityRegister import EntityRegister


class InputSystem:
    def __init__(self):
        self.__inputRegister = EntityRegister(('inputComponent'))
        self.inputMapper  = InputMapper()
        self.inputMapper.pushContext(ContextID.Directions)

    def registerEntities(self, entities, startId):
        self.__inputRegister.registerEntities(entities, startId)

    def handleInput(self, mappedInput):
        mappedInput = self.inputMapper.MapInput()

    def pushContext(self, contextID):
        self.inputMapper.pushContext(contextID)

    def popContext(self, contextID):
        self.inputMapper.popContext(contextID)

