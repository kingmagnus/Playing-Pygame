
from utility import unitVector


class MovingSystem:

    def __init__(self, dt):
        self.type = "MovingSystem"
        self.dt = dt

    def move(self, entities):
        for entity in entities:
            try:
                self._move(entity)
            except AttributeError:
                continue

    def _move(self, entity):
        distance = [ i * entity.state.velocityComponent.speed * self.dt / 1000. for i in unitVector(entity.state.velocityComponent.direction)]

        distance[0] = distance[0]*entity.state.collisionComponent.lx
        distance[1] = distance[1]*entity.state.collisionComponent.ly

        entity.state.velocityComponent.direction = [0,0]
        entity.state.collisionComponent.lx = 1
        entity.state.collisionComponent.ly = 1

        entity.state.geometryComponent.location = [sum(i) for i in zip(entity.state.geometryComponent.location, distance)]

    def accelirate(self, entity, accelitation):
        entity.state.velocityComponent.direction = [sum(i) for i in zip(entity.state.velocityComponent.direction, accelitation)]

    def handleCommand(self, command, entities):
        if command.systemType == self.type:
            for entity in entities:
                if entity.category in command.categories:
                    command.action(self, entity)
            return True
        else:
            return False
