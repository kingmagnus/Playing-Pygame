

import Category

def _PlayerEnemyResponse(collision):
    #collision = [ [entity1, entity2] , [collision lambda, x or y direction] ]

    entities = collision[0]
    l = collision[1][0]
    xy = collision[1][1]

    if xy == "x":
        entities[0].state.collisionComponent.lx = min(entities[0].state.collisionComponent.lx, l)
        entities[1].state.collisionComponent.lx = min(entities[1].state.collisionComponent.lx, l)

    elif xy == "y":
        entities[0].state.collisionComponent.ly = min(entities[0].state.collisionComponent.ly, l)
        entities[1].state.collisionComponent.ly = min(entities[1].state.collisionComponent.ly, l)
        
    else:
        entities[0].state.collisionComponent.lx = min(entities[0].state.collisionComponent.lx, l)
        entities[1].state.collisionComponent.lx = min(entities[1].state.collisionComponent.lx, l)
        entities[0].state.collisionComponent.ly = min(entities[0].state.collisionComponent.ly, l)
        entities[1].state.collisionComponent.ly = min(entities[1].state.collisionComponent.ly, l)
    

def _PlayerFloorResponse(collision):
    print "player colliding with floor"

ResponseDict = {(Category.PLAYER, Category.ENEMY) : _PlayerEnemyResponse,
                (Category.PLAYER, Category.FLOOR) : _PlayerFloorResponse}

categoryPairs = [(Category.PLAYER, Category.ENEMY), (Category.PLAYER, Category.FLOOR)]





