
from math import sqrt
from EntityRegister import EntityRegister

from IntentEffectMaps import AccelIntentMaps

class MovingSystem:

    def __init__(self, dt):
        self.__velRegister = EntityRegister(('velocityComponent', 'geometryComponent'))
        self.__colVelRegister = EntityRegister(('collisionComponent', 'velocityComponent', 'geometryComponent'))
        self.__accelRegister = EntityRegister(('accelerationComponent' 'geometryComponent'))
        self.__colAccelRegister = EntityRegister(('collisionComponent', 'accelerationComponent', 'geometryComponent'))
        self.__accelIntentRegister = EntityRegister(('accelerationComponent', 'intentComponent'))


        self.__velRegister.difference(self.__colVelRegister)
        self.__velRegister.difference(self.__accelRegister)
        self.__colVelRegister.difference(self.__colAccelRegister)
        self.__accelRegister.difference(self.__colAccelRegister)

        self.dt = dt

        self.accelIntentMaps = AccelIntentMaps()


    def registerEntities(self, entities, startId):
        self.__velRegister.registerEntities(entities, startId)
        self.__colVelRegister.registerEntities(entities, startId)
        self.__accelRegister.registerEntities(entities, startId)
        self.__colAccelRegister.registerEntities(entities, startId)
        self.__accelIntentRegister.registerEntities(entities, startId)

        self.__accelIntentRegister.printRegister()

        self.__velRegister.difference(self.__colVelRegister)
        self.__velRegister.difference(self.__accelRegister)
        self.__colVelRegister.difference(self.__colAccelRegister)
        self.__accelRegister.difference(self.__colAccelRegister)

    def move(self, entities):
        self.__updatePosition(entities)
        self.__updateVelocity(entities)
        self.__boundVelocity(entities)


        for i in self.__accelIntentRegister:
            print "x", entities[i].state.geometryComponent.location[0]
            print "y", entities[i].state.geometryComponent.location[1]
            print "vx", entities[i].state.velocityComponent.vx
            print "vy", entities[i].state.velocityComponent.vy
            print "ax", entities[i].state.accelerationComponent.ax
            print "ay", entities[i].state.accelerationComponent.ay
            print "\n\n"


    def __boundVelocity(self,entities):
        for i in self.__velRegister:
            self.__boundVelocityCode(entities,i)
        for i in self.__colVelRegister:
            self.__boundVelocityCode(entities,i)
        for i in self.__accelRegister:
            self.__boundVelocityCode(entities,i)
        for i in self.__colAccelRegister:
            self.__boundVelocityCode(entities,i)

    def __boundVelocityCode(self, e, i):
        speed = sqrt(e[i].state.velocityComponent.vx**2 + e[i].state.velocityComponent.vy**2)
        print "speed", speed
        try:
            ratio = min(speed, e[i].state.velocityComponent.maxSpeed)/ speed
            e[i].state.velocityComponent.vx *= ratio
            e[i].state.velocityComponent.vy *= ratio
            speed = sqrt(e[i].state.velocityComponent.vx**2 + e[i].state.velocityComponent.vy**2)
            print "bound speed", speed
        except ZeroDivisionError:
            pass
    
    def __updateVelocity(self, entities):
        for i in self.__accelRegister:
            self.__updateVel(entities[i])
        for i in self.__colAccelRegister:
            self.__updateVelCol(entities[i])
    
    def __updateVelCol(self, e):
        e.state.velocityComponent.vx += e.state.accelerationComponent.ax * e.state.collisionComponent.lx * self.dt
        e.state.velocityComponent.vy += e.state.accelerationComponent.ay * e.state.collisionComponent.ly * self.dt

        
    def __updateVel(self, e):
        e.state.velocityComponent.vx += e.state.accelerationComponent.ax * self.dt
        e.state.velocityComponent.vy += e.state.accelerationComponent.ay * self.dt
        
    def __updatePosition(self, entities):
        for i in self.__velRegister:
            self.__velUpdatePosition(entities[i])
        for i in self.__colVelRegister:
            self.__colVelUpdatePosition(entities[i])
        for i in self.__accelRegister:
            self.__accelUpdatePosition(entities[i])
        for i in self.__colAccelRegister:
            self.__colAccelUpdatePosition(entities[i])

    def __colAccelUpdatePosition(self, e):
        e.state.geometryComponent.location[0] += 0.5 * e.state.accelerationComponent.ax * ( e.state.collisionComponent.lx * self.dt) **2 + e.state.velocityComponent.vx * e.state.collisionComponent.lx * self.dt 
        e.state.geometryComponent.location[1] += 0.5 * e.state.accelerationComponent.ay * ( e.state.collisionComponent.ly * self.dt) **2 + e.state.velocityComponent.vy * e.state.collisionComponent.ly * self.dt 
        
    def __accelUpdatePosition(self, e):
        e.state.geometryComponent.location[0] += 0.5 * e.state.accelerationComponent.ax * self.dt **2 + e.state.velocityComponent.vx * self.dt 
        e.state.geometryComponent.location[1] += 0.5 * e.state.accelerationComponent.ay * self.dt **2 + e.state.velocityComponent.vy * self.dt 
        
    def __colVelUpdatePosition(self, e):
        e.state.geometryComponent.location[0] += e.state.velocityComponent.vx * e.state.collisionComponent.lx * self.dt
        e.state.geometryComponent.location[1] += e.state.velocityComponent.vy * e.state.collisionComponent.ly * self.dt 
            
    def __velUpdatePosition(self, e):
        e.state.geometryComponent.location[0] += e.state.velocityComponent.vx
        e.state.geometryComponent.location[1] += e.state.velocityComponent.vy
        
    def accelWithIntent(self, entities):
        for i in self.__accelIntentRegister:
            self.__accelWithIntent(entities[i])

    def __accelWithIntent(self, entity):
        accelMap = self.accelIntentMaps["Run"]
        runFn = accelMap[entity.state.intentComponent.intentID]
        runFn(entity)
