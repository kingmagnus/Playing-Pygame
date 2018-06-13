

from Entity import Entity
import Category

from SpriteComponent import SpriteComponent
from GeometryComponent import GeometryComponent
from VelocityComponent import VelocityComponent
from CollisionComponent import CollisionComponent
from AccelerationComponent import AccelerationComponent
from InputComponent import InputComponent
from PositionComponent import PositionComponent

from DrawingSystem import DrawingSystem
from CollisionSystem import CollisionSystem
from MovingSystem import MovingSystem
from InputSystem import InputSystem

from InputMapper import MappedInput

from Observer import Publisher

import StateKey
import SpriteKey
import FSMStateFactory as fsm


BACKGROUND  = 0
ACTIVELAYER = 1
FORGROUND   = 2
LAYERCOUNT  = 3


_uniqueEntityID = 0


class World():
    """ Contains all objects relevant to the game world """

    def __init__(self, dt):
        viewSize = (300,300)
        self.spawnLocation = [100,100]

        self.geometryComponents = {}
        self.inputComponents = {}
        self.positionComponents = {}
        self.velocityComponents = {}
        self.accelirationComponents = {}
        self.spriteComponents = {}
        self.collisionComponents = {}

        #Systems for logic
        self.drawingSystem   = DrawingSystem(self.positionComponents, self.spriteComponents, self.geometryComponents)
        self.collisionSystem = CollisionSystem(self.positionComponents, self.velocityComponents, self.accelirationComponents, self.geometryComponents, self.collisionComponents, viewSize, dt)
        self.movingSystem    = MovingSystem(self.positionComponents, self.velocityComponents, self.accelirationComponents, self.collisionComponents, dt)
        self.inputSystem     = InputSystem(self.inputComponents, self.velocityComponents)

        #publishers send messages between systems
        self.inputSystem.addObserver(self.movingSystem)
        self.inputSystem.addObserver(self.drawingSystem)


        self.buildScene()


    def update(self):
        #Add a command asking for the player entity to look for input
        #note that we use an optional paramiter to pass the lambda access to the command queue

        self.inputSystem.handleInput()
        self.collisionSystem.resolve()
        self.movingSystem.timestep()

    def render(self, surface):
        self.drawingSystem.draw(surface)   
                          
    def buildScene(self):
        
        global _uniqueEntityID
        ID = _uniqueEntityID
        _uniqueEntityID += 1

        self.inputComponents[ID] = InputComponent(fsm.StateIDs.Standing)
        self.spriteComponents[ID] = SpriteComponent(SpriteKey.lynStanding)
        self.velocityComponents[ID] = VelocityComponent(0,0,120)
        self.positionComponents[ID] = PositionComponent(20,100)
        self.geometryComponents[ID] = GeometryComponent(21, 35)
        self.accelirationComponents[ID] = AccelerationComponent(0,0)
        self.collisionComponents[ID] = CollisionComponent()
        
        #####
        
        ID = _uniqueEntityID
        _uniqueEntityID += 1
        
        self.spriteComponents[ID] = SpriteComponent(SpriteKey.brigandStanding)
        self.velocityComponents[ID] = VelocityComponent(0,0,120)
        self.positionComponents[ID] = PositionComponent(200,100)
        self.geometryComponents[ID] = GeometryComponent(21, 35)
        self.accelirationComponents[ID] = AccelerationComponent(0,0)
        self.collisionComponents[ID] = CollisionComponent()
        


        """
        eTemp = Entity(Category.ENEMY, self.sf.getState(StateKey.EnemyStanding))
        eTemp.state.geometryComponent.location = [120,150]
        self.newEntities.append(eTemp)
        
        eTemp = Entity(Category.ENEMY, self.sf.getState(StateKey.EnemyStanding))
        eTemp.state.geometryComponent.location = [100,100]
        self.newEntities.append(eTemp)
        
        eTemp = Entity(Category.ENEMY, self.sf.getState(StateKey.EnemyStanding))
        eTemp.state.geometryComponent.location = [200,130]
        self.newEntities.append(eTemp)
        
        eTemp = Entity(Category.ENEMY, self.sf.getState(StateKey.EnemyStanding))
        eTemp.state.geometryComponent.location = [160,30]
        self.newEntities.append(eTemp)
        """
