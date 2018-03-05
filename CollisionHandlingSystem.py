

import CollisionHandling
from CollisionResponses import *

class CollisionHandlingSystem:

    def handle(self,collisions):
        for collision in collisions:
            if checkCategoryPair(collision):
                #look up the pair's response function in the dictionary ResponseDict
                ResponseDict[(collision[0][0].category, collision[0][1].category)](collision)


def checkCategoryPair(collision):
    global categoryPairs

    #print (collision[0][0].category, collision[0][1].category)

    if (collision[0][0].category, collision[0][1].category) in categoryPairs:
        return True
    if (collision[0][1].category, collision[0][0].category) in categoryPairs:
        collision[0][0], collision[0][1] = collision[0][1], collision[0][0]
        return True
    return False


