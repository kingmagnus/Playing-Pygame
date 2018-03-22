

from CollisionDetectionSystem import CollisionDetectionSystem
from CollisionHandlingSystem import CollisionHandlingSystem
 

class CollisionSystem:

    def __init__(self, viewSize, dt):
        self.CDS = CollisionDetectionSystem(viewSize, dt)
        self.CHS = CollisionHandlingSystem()


    def resolveCollisions(self, entities):
            collisions = self.CDS.getCollisions(entities)
            self.CHS.handle(collisions)
