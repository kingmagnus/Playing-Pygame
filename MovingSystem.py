
from math import sqrt
from EntityRegister import EntityRegister
from Observer import Observer

from numpy import sign

class MovingSystem(Observer):

    def __init__(self, entities, dt):
        self.entities = entities

        self.__velRegister = EntityRegister('velocityComponent', 'geometryComponent')
        self.__colVelRegister = EntityRegister('collisionComponent', 'velocityComponent', 'geometryComponent')
        self.__accelRegister = EntityRegister('accelerationComponent' 'geometryComponent')
        self.__colAccelRegister = EntityRegister('collisionComponent', 'accelerationComponent', 'geometryComponent')

        self.__velRegister.difference(self.__colVelRegister)
        self.__velRegister.difference(self.__accelRegister)
        self.__colVelRegister.difference(self.__colAccelRegister)
        self.__accelRegister.difference(self.__colAccelRegister)

        self.dt = dt

    def registerEntities(self):
        self.__velRegister.registerEntities(self.entities)
        self.__colVelRegister.registerEntities(self.entities)
        self.__accelRegister.registerEntities(self.entities)
        self.__colAccelRegister.registerEntities(self.entities)

        self.__velRegister.difference(self.__colVelRegister)
        self.__velRegister.difference(self.__accelRegister)
        self.__colVelRegister.difference(self.__colAccelRegister)
        self.__accelRegister.difference(self.__colAccelRegister)

        print "self.__velRegister", self.__velRegister
        print "self.__colVelRegister", self.__velRegister
        print "self.__accelRegister", self.__velRegister
        print "self.__colAccelRegister", self.__velRegister

    def timestep(self):
        self.__updatePosition()
        self.__updateVelocity()

    def __updateVelocity(self):
        self.__updateVel()
        self.__updateVelCol()
        self.__boundVelocity()
        
    def __boundVelocity(self):
        self.__boundVelocityCode(self.__velRegister)
        self.__boundVelocityCode(self.__colVelRegister)
        self.__boundVelocityCode(self.__accelRegister)
        self.__boundVelocityCode(self.__colAccelRegister)

    def __boundVelocityCode(self, register):
        for i in register:
            self.entities[i].state.velocityComponent.vx = sign(self.entities[i].state.velocityComponent.vx)*min(abs(self.entities[i].state.velocityComponent.vx), self.entities[i].state.velocityComponent.maxSpeedx)
            self.entities[i].state.velocityComponent.vy = sign(self.entities[i].state.velocityComponent.vy)*min(abs(self.entities[i].state.velocityComponent.vy), self.entities[i].state.velocityComponent.maxSpeedy)
    
    def __updateVelCol(self):
        for i in self.__colAccelRegister:
            e = self.entities[i]
            e.state.velocityComponent.vx += e.state.accelerationComponent.ax * e.state.collisionComponent.lx * self.dt
            e.state.velocityComponent.vy += e.state.accelerationComponent.ay * e.state.collisionComponent.ly * self.dt
        
    def __updateVel(self):
        for i in self.__accelRegister:
            e = self.entities[i]
            e.state.velocityComponent.vx += e.state.accelerationComponent.ax * self.dt
            e.state.velocityComponent.vy += e.state.accelerationComponent.ay * self.dt
        
    def __updatePosition(self):
        self.__colAccelUpdatePosition()
        self.__accelUpdatePosition()
        self.__colVelUpdatePosition()
        self.__velUpdatePosition()        
    
    def __colAccelUpdatePosition(self):
        for i in self.__colAccelRegister:
            e = self.entities[i]
            e.state.geometryComponent.location[0] += 0.5 * e.state.accelerationComponent.ax * ( e.state.collisionComponent.lx * self.dt) **2 + e.state.velocityComponent.vx * e.state.collisionComponent.lx * self.dt 
            e.state.geometryComponent.location[1] += 0.5 * e.state.accelerationComponent.ay * ( e.state.collisionComponent.ly * self.dt) **2 + e.state.velocityComponent.vy * e.state.collisionComponent.ly * self.dt 

    def __accelUpdatePosition(self):
        for i in self.__accelRegister:
            e = self.entities[i]
            e.state.geometryComponent.location[0] += 0.5 * e.state.accelerationComponent.ax * self.dt **2 + e.state.velocityComponent.vx * self.dt 
            e.state.geometryComponent.location[1] += 0.5 * e.state.accelerationComponent.ay * self.dt **2 + e.state.velocityComponent.vy * self.dt 
        
    def __colVelUpdatePosition(self):
        for i in self.__colVelRegister:
            e = self.entities[i]
            e.state.geometryComponent.location[0] += e.state.velocityComponent.vx * e.state.collisionComponent.lx * self.dt
            e.state.geometryComponent.location[1] += e.state.velocityComponent.vy * e.state.collisionComponent.ly * self.dt 
            
    def __velUpdatePosition(self):
        for i in self.__velRegister:
            e = self.entities[i]
            e.state.geometryComponent.location[0] += e.state.velocityComponent.vx
            e.state.geometryComponent.location[1] += e.state.velocityComponent.vy
    

    def processEvent(self, event):

        if event.entryState == "Standing":
            self.entities[event.entityID].state.accelerationComponent.ax = 0
            self.entities[event.entityID].state.accelerationComponent.ay = 0
            self.entities[event.entityID].state.velocityComponent.vx = 0
            self.entities[event.entityID].state.velocityComponent.vy = 0
            return

        if event.entryState == "Running" and event.direction == "Right":
            self.entities[event.entityID].state.accelerationComponent.ax = 0
            self.entities[event.entityID].state.velocityComponent.vx = self.entities[event.entityID].state.velocityComponent.maxSpeedx
            self.entities[event.entityID].state.velocityComponent.vy = 0
            return

        if event.entryState == "Running" and event.direction == "Left":
            self.entities[event.entityID].state.accelerationComponent.ax = 0
            self.entities[event.entityID].state.velocityComponent.vx = -self.entities[event.entityID].state.velocityComponent.maxSpeedx
            self.entities[event.entityID].state.velocityComponent.vy = 0
            return

        if event.entryState == "StartRunning" and event.direction == "Right":
            self.entities[event.entityID].state.accelerationComponent.ax = self.entities[event.entityID].state.accelerationComponent.maxAccel
            return

        if event.entryState == "StartRunning" and event.direction == "Left":
            self.entities[event.entityID].state.accelerationComponent.ax = -self.entities[event.entityID].state.accelerationComponent.maxAccel
            return

        if event.entryState == "StopRunning" and event.direction == "Right":
            self.entities[event.entityID].state.accelerationComponent.ax = -self.entities[event.entityID].state.accelerationComponent.maxAccel
            return

        if event.entryState == "StopRunning" and event.direction == "Left":
            self.entities[event.entityID].state.accelerationComponent.ax = self.entities[event.entityID].state.accelerationComponent.maxAccel
            return


