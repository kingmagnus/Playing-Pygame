

from EntityRegister import EntityRegister
from QuadTree import QuadTree
from pygame import Rect

class CollisionSystem:

    def __init__(self, viewSize, dt):
        self.__collisionRegister = EntityRegister(('collisionComponent'))
        self.__qTree = QuadTree(Rect(0,0,viewSize[0],viewSize[1]),dt)
        self.__collisions = []
        self.__responseDict = {}

    def registerEntities(self, entities, startId):
        self.__collisionRegister.registerEntities(entities, startId)

    def resolve(self, entities):
            self.__findCollisions(entities)
            self.__handle()

    def __findCollisions(self, entities):
        #broad phase collsion detection
        self.__qTree.empty()
        del self.__collisions[:]
        self.__qTree.addEntities(entities, self.__collisionRegister)
        self.__collisions = self.__qTree.findCollisions()

    def __handle(self):
        for collision in self.__collisions:
            if self.__checkCategoryPair(collision):
                #look up the pair's response function in the dictionary ResponseDict
                #ResponseDict[(collision.e1.category, collision.e2.category)](collision)
                pass

    def __checkCategoryPair(self,collision):
        """ will return a bool if collision is interesting, also formats collision for the response"""
        #checks if (e1, e2) is an interesting collision
        # will swap order if needed.
        if (collision.e1.category, collision.e2.category) in self.__responseDict.keys():
            return True
        if (collision.e2.category, collision.e1.category) in self.__responseDict.keys():
            collision.e1, collision.e2 = collision.e2, collision.e1
            return True
        return False
