

from CollisionDetectionSystem import CollisionDetectionSystem
from CollisionHandlingSystem import CollisionHandlingSystem
from EntityRegister import EntityRegister
from QuadTree import QuadTree

class CollisionSystem:

    def __init__(self, viewSize, dt):
        self.__collisionRegister = EntityRegister('collisionComponent')
        self.__qTree = QuadTree(pygame.Rect(0,0,viewSize[0],viewSize[1]),dt)
        self.__collisions = []

    def registerEntities(self, entities, startId):
        __collisionRegister.registerEntities(entities, startId)

    def resolve(self, entities):
            self.__findCollisions(entities)
            self.__handle()

    def __findCollisions(self, entities):
        #broad phase collsion detection
        self._qTree.empty()
        del self.__collisions[:]
        self.__qTree.addEntities(entities, self.__collisionRegister)
        self.__collisions = self.__qTree.findCollisions()

    def __handle(self):
        for collision in self.__collisions:
            if self.__checkCategoryPair(collision):
                #look up the pair's response function in the dictionary ResponseDict
                ResponseDict[(collision.e1.category, collision.e2.category)](collision)

    def __checkCategoryPair(self,collision):
        """ will return a bool if collision is interesting, also formats collision for the response"""
        #checks if (e1, e2) is an interesting collision
        # will swap order if needed.
        if (collision.e1.category, collision.e2.category) in ResponseDict.keys():
            return True
        if (collision.e2.category, collision.e1.category) in ResponseDict.keys():
            collision.e1, collision.e2 = collision.e2, collision.e1
            return True
        return False
