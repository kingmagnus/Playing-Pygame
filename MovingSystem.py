
from math import sqrt
from EntityRegister import EntityRegister

class MovingSystem:

    def __init__(self, dt):
        __velRegister = EntityRegister('velocityComponent', 'geometryComponent')
        __colVelRegister = EntityRegister('collisionComponent', 'velocityComponent', 'geometryComponent')
        __accelRegister = EntityRegister('accelerationComponent', 'velocityComponent', 'geometryComponent')
        __colAccelRegister = EntityRegister('collisionComponent', 'accelerationComponent', 'velocityComponent', 'geometryComponent')

        __velRegister = list(set(__velRegister).difference_update(__colVelRegister, __accelRegister))
        __colVelRegister = list(set(__colVelRegister).difference_update( __colAccelRegister))
        __accelRegister = list(set(__colVelRegister).difference_update( __colAccelRegister))

        self.dt = dt

    def move(self, entities):
        self.__boundVelocity(entities)
        self.__updatePosition(entities)
        self.__updateVelocity(entities)


    def __boundVelocity(self,entities):
        for i in __velRegister:
            self.__boundVelocityCode(entities[i])
        for i in __colVelRegister:
            self.__boundVelocityCode(entities[i])
        for i in __accelRegister:
            self.__boundVelocityCode(entities[i])
        for i in __colAccelRegister:
            self.__boundVelocityCode(entities[i])

    def __boundVelocityCode(self, e)
        speed = sqrt(e.state.velovityComponent.vx**2 + e.state.velovityComponent.vy**2)
        ratio = min(speed, e.state.velovityComponent.maxSpeed)/ speed
        e.state.velovityComponent.vx *= ratio
        e.state.velovityComponent.vy *= ratio
    
    def __updateVelocity(self, entities):
        for i in __accelRegister:
            self.__updateVelocity(entities[i])
        for i in __colAccelRegister:
            self.__updateVelocityCol(entities[i])
    
    def __updateVelocityCol(self, e):
        e.state.velocityComponent.vx += e.state.accelerationComponent.ax * e.state.collisionComponent.lx * self.dt
        e.state.velocityComponent.vy += e.state.accelerationComponent.ay * e.state.collisionComponent.ly * self.dt

        
    def __updateVelocity(self, e):
        e.state.velocityComponent.vx += e.state.accelerationComponent.ax * self.dt
        e.state.velocityComponent.vy += e.state.accelerationComponent.ay * self.dt
        
    def __updatePosition(self, entities):
        for i in __velRegister:
            self.__velUpdatePosition(entities[i])
        for i in __colVelRegister:
            self.__colVelUpdatePosition(entities[i])
        for i in __accelRegister:
            self.__accelUpdatePosition(entities[i])
        for i in __colAccelRegister:
            self.__colAccelUpdatePosition(entities[i])

    def __colAccelUpdatePosition(self):
        e.state.geometryComponent.location[0] += 0.5 * e.state.accelerationComponent.ax * ( e.state.collisionComponent.lx * self.dt) **2 + e.state.velocityComponent.vx * e.state.collisionComponent.lx * self.dt 
        e.state.geometryComponent.location[1] += 0.5 * e.state.accelerationComponent.ay * ( e.state.collisionComponent.ly * self.dt) **2 + e.state.velocityComponent.vy * e.state.collisionComponent.ly * self.dt 
        
    def __accelUpdatePosition(self):
        e.state.geometryComponent.location[0] += 0.5 * e.state.accelerationComponent.ax * self.dt **2 + e.state.velocityComponent.vx * self.dt 
        e.state.geometryComponent.location[1] += 0.5 * e.state.accelerationComponent.ay * self.dt **2 + e.state.velocityComponent.vy * self.dt 
        
    def __colVelUpdatePosition(self):
        e.state.geometryComponent.location[0] += e.state.velocityComponent.vx * e.state.collisionComponent.lx * self.dt
        e.state.geometryComponent.location[1] += e.state.velocityComponent.vy * e.state.collisionComponent.ly * self.dt 
            

    def __velUpdatePosition(self):
        e.state.geometryComponent.location[0] += e.state.velocityComponent.vx
        e.state.geometryComponent.location[1] += e.state.velocityComponent.vy
        
