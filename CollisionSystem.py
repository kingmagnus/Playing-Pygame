

import CollisionDetectionSystem as cds
import CollisionHandlingSystem as chs
 

class CollisionSystem:

    def __init__(self, viewSize, dt):
        self.collisionDetectionSystem = cds.CollisionDetectionSystem(viewSize, dt)
        self.collisionHandlingSystem = chs.CollisionHandlingSystem()


    def resolveCollisions(self, entities):
            collisions = self.collisionDetectionSystem.detect(entities)
            self.collisionHandlingSystem.handle(collisions)
