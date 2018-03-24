
from InputMapper import InputMapper
from EntityRegister import EntityRegister


class InputSystem:
    def __init__(self):
        self.__inputRegister = EntityRegister(('inputComponent'))
        self.__commandTable = {} #{int: inputCallback}
        self.inputMapper  = InputMapper()

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

    def AddCommand(self, command, priority):
        self.__commandTable[priority] = command

