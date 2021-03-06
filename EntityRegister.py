

class EntityRegister(object):
    __slots__ = "__attributes", "__register", "__count"
    def __init__(self, *args):
        self.__attributes = args
        self.__register = []
        self.__count = 0

    def __iter__(self):
        return self

    def __str__(self):
        return "EntityRegister: \n    Attributes are %s\n    Register is %s" % (self.__attributes, self.__register)

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

    def registerEntities(self, entities):
        for i in range(len(entities)):
            if i not in self.__register and self.__checkComponents(entities[i]):
                self.__register.append(i)
    
    def reRegisterEntities(self, entities):
        del self.__register[:]
        self.__registerEntities(entities, 0)

    def difference(self, register):
        self.__register = list(set(self.__register).difference(register))
        
    def size(self):
        return len(self.__register)

