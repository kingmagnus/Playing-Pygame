
from Entity import Entity
import Category



def checkCategoryPair(collision):
    global categoryPairs

    if (collision[0][0].mCategory, collision[0][1].mCategory) in categoryPairs:
        return True
    if (collision[0][1].mCategory, collision[0][0].mCategory) in categoryPairs:
        collision[0][0], collision[0][1] = collision[0][1], collision[0][0]
        return True
    return False

def _PlayerEnemyResponse(collision):
    #print "_PlayerEnemyResponse"

    entities = collision[0]
    l = collision[1][0]
    xy = collision[1][1]

    if xy == "x":
        entities[0].lx = min(entities[0].lx, l)
        entities[1].lx = min(entities[1].lx, l)
        #print "xy", xy, "l", l, "entities[0].lx", entities[0].lx, "entities[1].lx", entities[1].lx

    elif xy == "y":
        entities[0].ly = min(entities[0].ly, l)
        entities[1].ly = min(entities[1].ly, l)
        
    else:
        entities[0].lx = min(entities[0].lx, l)
        entities[1].lx = min(entities[1].lx, l)
        entities[0].ly = min(entities[0].ly, l)
        entities[1].ly = min(entities[1].ly, l)
    
    #This is wrong, it stops ll motion at the point of collision, we only want it stoped in the diretion of collision.




#Buffer variable so that we can move objects to before they collide not the exact instance to prevent sticking
_EPSILON = 0.0001

counter = 0

categoryPairs = [(Category.PLAYER, Category.ENEMY)]

ResponseDict = {(Category.PLAYER, Category.ENEMY) : _PlayerEnemyResponse}
