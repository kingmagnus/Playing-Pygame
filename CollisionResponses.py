

import Category

def _PlayerEnemyResponse(collision):

    xy = collision[1][1]

    if collision.axis == "x":
        collision.e1.state.collisionComponent.lx = min(collision.e1.state.collisionComponent.lx, collision.l)
        collision.e2.state.collisionComponent.lx = min(collision.e2.state.collisionComponent.lx, collision.l)

    elif collision.axis == "y":
        collision.e1.state.collisionComponent.ly = min(collision.e1.state.collisionComponent.ly, collision.l)
        collision.e2.state.collisionComponent.ly = min(collision.e2.state.collisionComponent.ly, collision.l)
        
    else:
        collision.e1.state.collisionComponent.lx = min(collision.e1.state.collisionComponent.lx, collision.l)
        collision.e2.state.collisionComponent.lx = min(collision.e2.state.collisionComponent.lx, collision.l)
        collision.e1.state.collisionComponent.ly = min(collision.e1.state.collisionComponent.ly, collision.l)
        collision.e2.state.collisionComponent.ly = min(collision.e2.state.collisionComponent.ly, collision.l)
    

def _PlayerFloorResponse(collision):
    print ("player colliding with floor")

ResponseDict = {(Category.PLAYER, Category.ENEMY) : _PlayerEnemyResponse,
                (Category.PLAYER, Category.FLOOR) : _PlayerFloorResponse}






