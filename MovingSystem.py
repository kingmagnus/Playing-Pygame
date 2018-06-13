
from math import sqrt
from EntityRegister import EntityRegister
from Observer import Observer

from numpy import sign

class MovingSystem(Observer):

    def __init__(self, positionComponents, velocityComponents, accelerationComponents, 
                    collisionComponents, dt):

        self.positionComponents = positionComponents
        self.velocityComponents = velocityComponents
        self.accelerationComponents = accelerationComponents
        self.collisionComponents = collisionComponents

        self.dt = dt

    def timestep(self):
        vel = set(self.velocityComponents.keys())
        accel = set(self.accelerationComponents.keys())
        col = set(self.collisionComponents.keys())
        
        vel = vel - accel
        colAccel = col & accel
        accel = accel - col
        colVel = col & vel
        vel = vel - colVel

        self.__colAccelUpdatePosition(colAccel)
        self.__accelUpdatePosition(accel)
        self.__colVelUpdatePosition(colVel)
        self.__velUpdatePosition(vel)  

        self.__updateVel(vel) 
        self.__updateVel(accel)
        self.__updateVelCol(colVel)
        self.__updateVelCol(colAccel)

        self.__boundVelocity()
        
    def __boundVelocity(self):
        for ID in self.velocityComponents.keys():
            self.velocityComponents[ID].vx = sign(self.velocityComponents[ID].vx)*min(abs(self.velocityComponents[ID].vx), self.velocityComponents[ID].maxSpeedx)
            self.velocityComponents[ID].vy = sign(self.velocityComponents[ID].vy)*min(abs(self.velocityComponents[ID].vy), self.velocityComponents[ID].maxSpeedy)
    
    def __updateVelCol(self, velCol):
        for ID in velCol:
            self.velocityComponents[ID].vx += self.accelerationComponents[ID].ax * self.collisionComponents[ID].lx * self.dt
            self.velocityComponents[ID].vy += self.accelerationComponents[ID].ay * self.collisionComponents[ID].ly * self.dt
        
    def __updateVel(self, vel):
        for ID in vel:
            self.velocityComponents[ID].vx += self.accelerationComponents[ID].ax * self.dt
            self.velocityComponents[ID].vy += self.accelerationComponents[ID].ay * self.dt
        
    def __colAccelUpdatePosition(self, colAccel):
        for ID in colAccel:
            print "ax", self.accelerationComponents[ID].ax, "vx", self.velocityComponents[ID].vx, "lx", self.collisionComponents[ID].lx
            self.positionComponents[ID].x += 0.5 * self.accelerationComponents[ID].ax * ( self.collisionComponents[ID].lx * self.dt) **2 + self.velocityComponents[ID].vx * self.collisionComponents[ID].lx * self.dt 
            self.positionComponents[ID].y += 0.5 * self.accelerationComponents[ID].ay * ( self.collisionComponents[ID].ly * self.dt) **2 + self.velocityComponents[ID].vy * self.collisionComponents[ID].ly * self.dt 

    def __accelUpdatePosition(self, accel):
        for ID in accel:
            self.positionComponents[ID].x += 0.5 * self.accelerationComponents[ID].ax * self.dt**2 + self.velocityComponents[ID].vx * self.dt 
            self.positionComponents[ID].y += 0.5 * self.accelerationComponents[ID].ay * self.dt**2 + self.velocityComponents[ID].vy * self.dt 
        
    def __colVelUpdatePosition(self, colVel):
        for ID in colVel:
            self.positionComponents[ID].x += self.velocityComponents[ID].vx * self.collisionComponents[ID].lx * self.dt
            self.positionComponents[ID].y += self.velocityComponents[ID].vy * self.collisionComponents[ID].ly * self.dt 
            
    def __velUpdatePosition(self, vel):
        for ID in vel:
            self.positionComponents[ID].x += self.velocityComponents[ID].vx
            self.positionComponents[ID].y += self.velocityComponents[ID].vy
    

    def processEvent(self, event):

        if event.entryState == "Standing":
            self.accelerationComponents[event.entityID].ax = 0
            self.accelerationComponents[event.entityID].ay = 0
            self.velocityComponents[event.entityID].vx = 0
            self.velocityComponents[event.entityID].vy = 0
            return

        if event.entryState == "Running" and event.direction == "Right":
            self.accelerationComponents[event.entityID].ax = 0
            self.velocityComponents[event.entityID].vx = self.velocityComponents[event.entityID].maxSpeedx
            self.velocityComponents[event.entityID].vy = 0
            return

        if event.entryState == "Running" and event.direction == "Left":
            self.accelerationComponents[event.entityID].ax = 0
            self.velocityComponents[event.entityID].vx = -self.velocityComponents[event.entityID].maxSpeedx
            self.velocityComponents[event.entityID].vy = 0
            return

        if event.entryState == "StartRunning" and event.direction == "Right":
            self.accelerationComponents[event.entityID].ax = self.accelerationComponents[event.entityID].maxAccel
            return

        if event.entryState == "StartRunning" and event.direction == "Left":
            self.accelerationComponents[event.entityID].ax = -self.accelerationComponents[event.entityID].maxAccel
            return

        if event.entryState == "StopRunning" and event.direction == "Right":
            self.accelerationComponents[event.entityID].ax = -self.accelerationComponents[event.entityID].maxAccel
            return

        if event.entryState == "StopRunning" and event.direction == "Left":
            self.accelerationComponents[event.entityID].ax = self.accelerationComponents[event.entityID].maxAccel
            return


