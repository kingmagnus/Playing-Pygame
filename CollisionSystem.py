

from CollisionDetectionSystem import CollisionDetectionSystem
from CollisionHandlingSystem import CollisionHandlingSystem
 

class CollisionSystem:

    def __init__(self, viewSize, dt):
        self.collisionDetectionSystem = CollisionDetectionSystem(viewSize, dt)
        self.collisionHandlingSystem = CollisionHandlingSystem()


    def resolveCollisions(self, entities):
            collisions = self.collisionDetectionSystem.detect(entities)
            self.collisionHandlingSystem.handle(collisions)
