
from math import sqrt

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

    def _move(self, e):
        
        self._boundVelocity(e)
        self._updatePosition(e)
        self._updateVelocity(e)


    def _boundVelocity(self,e):
        speed = sqrt(e.state.velovityComponent.vx**2 + e.state.velovityComponent.vy**2)
        ratio = min(speed, e.state.velovityComponent.maxSpeed)/ speed
        e.state.velovityComponent.vx *= ratio
        e.state.velovityComponent.vy *= ratio
        
    def _updateVelocity(self, e):
        try:
            e.state.velocityComponent.vx += e.state.accelerationComponent.ax * e.state.collisionComponent.lx * self.dt
            e.state.velocityComponent.vy += e.state.accelerationComponent.ay * e.state.collisionComponent.ly * self.dt
            return
        except AttributeError:
            pass
        
        try:
            e.state.velocityComponent.vx += e.state.accelerationComponent.ax * self.dt
            e.state.velocityComponent.vy += e.state.accelerationComponent.ay * self.dt
            return
        except AttributeError:
            return
        
    def _updatePosition(self, e):
        try:
            e.state.geometryComponent.location[0] += 0.5 * e.state.accelerationComponent.ax * ( e.state.collisionComponent.lx * self.dt) **2 + e.state.velocityComponent.vx * e.state.collisionComponent.lx * self.dt 
            e.state.geometryComponent.location[1] += 0.5 * e.state.accelerationComponent.ay * ( e.state.collisionComponent.ly * self.dt) **2 + e.state.velocityComponent.vy * e.state.collisionComponent.ly * self.dt 
            return
        except AttributeError:
            pass
        
        try:
            e.state.geometryComponent.location[0] += 0.5 * e.state.accelerationComponent.ax * ( e.state.collisionComponent.lx * self.dt) **2 + e.state.velocityComponent.vx * self.dt 
            e.state.geometryComponent.location[1] += 0.5 * e.state.accelerationComponent.ay * ( e.state.collisionComponent.ly * self.dt) **2 + e.state.velocityComponent.vy * self.dt 
            return
        except AttributeError:
            pass
        
        try:
            e.state.geometryComponent.location[0] += e.state.velocityComponent.vx * e.state.collisionComponent.lx * self.dt
            e.state.geometryComponent.location[1] += e.state.velocityComponent.vy * e.state.collisionComponent.ly * self.dt 
            return
        except AttributeError:
            pass
        
        e.state.geometryComponent.location[0] += e.state.velocityComponent.vx
        e.state.geometryComponent.location[1] += e.state.velocityComponent.vy
        return