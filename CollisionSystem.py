

from CollisionDetectionSystem import CollisionDetectionSystem
from CollisionHandlingSystem import CollisionHandlingSystem
from EntityRegister import EntityRegister

class CollisionSystem:

    def __init__(self, viewSize, dt):
        __collisionRegister = EntityRegister('collisionComponent')
        self.CDS = CollisionDetectionSystem(viewSize, dt)
        self.CHS = CollisionHandlingSystem()


    def resolveCollisions(self, entities):
            collisions = self.CDS.getCollisions(entities, __collisionRegister)
            self.CHS.handle(collisions)
