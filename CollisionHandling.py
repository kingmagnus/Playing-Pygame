
from Entity import Entity
import Category



def checkCategoryPair(collision):
    global categoryPairs

    if (collision[0][0].category, collision[0][1].category) in categoryPairs:
        return True
    if (collision[0][1].category, collision[0][0].category) in categoryPairs:
        collision[0][0], collision[0][1] = collision[0][1], collision[0][0]
        return True
    return False

def _PlayerEnemyResponse(collision):
    #collision = [ [entity1, entity2] , [collision lambda, x or y direction] ]

    entities = collision[0]
    l = collision[1][0]
    xy = collision[1][1]

    if xy == "x":
        entities[0].state.collisionComponent.lx = min(entities[0].state.collisionComponent.lx, l)
        entities[1].state.collisionComponent.lx = min(entities[1].state.collisionComponent.lx, l)
        #print "xy", xy, "l", l, "entities[0].lx", entities[0].lx, "entities[1].lx", entities[1].lx

    elif xy == "y":
        entities[0].state.collisionComponent.ly = min(entities[0].state.collisionComponent.ly, l)
        entities[1].state.collisionComponent.ly = min(entities[1].state.collisionComponent.ly, l)
        
    else:
        entities[0].state.collisionComponent.lx = min(entities[0].state.collisionComponent.lx, l)
        entities[1].state.collisionComponent.lx = min(entities[1].state.collisionComponent.lx, l)
        entities[0].state.collisionComponent.ly = min(entities[0].state.collisionComponent.ly, l)
        entities[1].state.collisionComponent.ly = min(entities[1].state.collisionComponent.ly, l)
    
    #This is wrong, it stops ll motion at the point of collision, we only want it stoped in the diretion of collision.




#Buffer variable so that we can move objects to before they collide not the exact instance to prevent sticking
_EPSILON = 0.0001

counter = 0

categoryPairs = [(Category.PLAYER, Category.ENEMY)]

ResponseDict = {(Category.PLAYER, Category.ENEMY) : _PlayerEnemyResponse}
