

class EntityRegister:
    __slots__ = "__attributes", "__register", "__count"
    def __init__(self, attributes):
        self.__attributes = attributes
        self.__register = []
        self.__count = 0

    def __iter__(self):
        return self

    def printRegister(self):
        print self.__register

    def printAttributes(self):
        print self.__attributes

    def next(self):
        if self.__count == len(self.__register):
            self.__count = 0
            raise StopIteration
        self.__count += 1
        return self.__register[self.__count -1]

    def __checkComponents(self, e):
        for atribute in self.__attributes:
            if not hasattr(e.state, atribute):
                return False 
        return True

    def registerEntities(self, entities, startId):
        for i in range(startId, len(entities)):
            if i not in self.__register and self.__checkComponents(entities[i]):
                self.__register.append(i)
    
    def reRegisterEntities(self, entities):
        del self.__register[:]
        self.__registerEntities(entities, 0)

    def difference(self, register):
        self.__register = list(set(self.__register).difference(register))
        
    def size(self):
        return len(self.__register)

