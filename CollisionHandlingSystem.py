

from CollisionResponses import ResponseDict

class CollisionHandlingSystem:

    def handle(self,collisions):
        for collision in collisions:
            if self._checkCategoryPair(collision):
                #look up the pair's response function in the dictionary ResponseDict
                ResponseDict[(collision.e1.category, collision.e2.category)](collision)


    def _checkCategoryPair(self,collision):
        """ will return a bool if collision is interesting, also formats collision for the response"""
        #checks if (e1, e2) is an interesting collision
        # will swap order if needed.
        if (collision.e1.category, collision.e2.category) in ResponseDict.keys():
            return True
        if (collision.e2.category, collision.e1.category) in ResponseDict.keys():
            collision.e1, collision.e2 = collision.e2, collision.e1
            return True
        return False


