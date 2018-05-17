from IntentMapper import IntentMapper
from EntityRegister import EntityRegister

class IntentSystem:
    def __init__(self):
        self.__intentMapper = IntentMapper()
        self.__playerRegister = EntityRegister(('inputComponent', 'intentComponent'))

    def registerEntities(self, entities, startId):
        self.__playerRegister.registerEntities(entities, startId)
        print("intent system registered", self.__playerRegister.size() ,"entities")

    def setPlayerIntent(self, mappedInput, entities):
        intent = self.__intentMapper.mapInputToIntent(mappedInput)
        self.__setIntent(intent, entities)

    def pushIntentMap(self, IntentMapID):
        self.__intentMapper = IntentMapper(IntentMapID)

    def __setIntent(self, intent, entities):
        for i in self.__playerRegister:
            entities[i].state.intentComponent.intentID = intent

