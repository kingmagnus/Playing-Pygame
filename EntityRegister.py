

class EntityRegister:
    def __init__(self, attributes):
        self.__attributes = attributes
        self.__register = []
        self.__count = 0

    def __iter__(self):
        return self

    def next(self):
        if self.__count == len(self.__register)
            self.__count = 0
            raise StopIteration
        self.__count += 1
        return self.__register[self.__count -1]

    def __checkAttributes(self, entitiy)
        for atribute in self.__attributes:
            if not hasattr(entitiy, atribute):
                return False 
        return True

    def registerEntities(self, entities, startId):
        for i in range(startId, len(entities)):
            if __checkAttributes(entities[i]):
                self.register.append(i)
    
    def reRegisterEntities(self, entities):
        del self.register[:]
        self.registerEntities(entities, 0)

