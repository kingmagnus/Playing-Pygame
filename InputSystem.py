
from InputMapper import InputMapper, ContextID
from EntityRegister import EntityRegister


class InputSystem:
    def __init__(self):
        self.__inputRegister = EntityRegister(('inputComponent'))
        self.inputMapper  = InputMapper()
        self.inputMapper.pushContext(ContextID.Directions)

    def registerEntities(self, entities, startId):
        self.__inputRegister.registerEntities(entities, startId)

    def handleInput(self, entities):
        mInput = self.inputMapper.MapInput()
        for i in mInput.Actions:
            print (i)
        for i in mInput.States:
            print (i)  
        #for key in sorted(self._callbackTable):
        #    for i in self.__inputRegister:
        #        self.__commandTable[key](mInput, entities[i])

    def pushContext(self, contextID):
        self.inputMapper.pushContext(contextID)

    def popContext(self, contextID):
        self.inputMapper.popContext(contextID)

