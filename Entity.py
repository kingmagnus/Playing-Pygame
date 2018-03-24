
import Category

from StateFactory import State 

_uniqueId = 0


class Entity():
    """ The Entity class is responsible for individual elements of the scene """

    #Entity shouldnt hold the containers and should only be an ID, 
    #The components should be in tables where the components are indexed by the entity id.
    #I've not done this becuase I cannot think of how to do it without pointers

    def __init__(self, category = Category.NONE, state = State()):

        global _uniqueId
        self.category  = category
        self.id        = _uniqueId #used in collision detection ordering
        self.state     = state

        _uniqueId+=1






