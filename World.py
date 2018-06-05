

from Entity import Entity
import Category

from StateFactory import StateFactory

from DrawingSystem import DrawingSystem
from CollisionSystem import CollisionSystem
from MovingSystem import MovingSystem
from InputSystem import InputSystem

from InputMapper import MappedInput

from Observer import Publisher

import StateKey


BACKGROUND  = 0
ACTIVELAYER = 1
FORGROUND   = 2
LAYERCOUNT  = 3





class World():
    """ Contains all objects relevant to the game world """

    def __init__(self, dt):
        viewSize = (300,300)
        self.spawnLocation = [100,100]
        self.entities = []
        self.newEntities = []
        self.sf = StateFactory()
        self.buildScene()

        #Systems for logic
        self.drawingSystem   = DrawingSystem(self.entities)
        self.collisionSystem = CollisionSystem(self.entities, viewSize, dt)
        self.movingSystem    = MovingSystem(self.entities, dt)
        self.inputSystem     = InputSystem(self.entities)

        #publishers send messages between systems
        self.inputSystem.addObserver(self.movingSystem)
        self.inputSystem.addObserver(self.drawingSystem)


    def update(self):
        #Add a command asking for the player entity to look for input
        #note that we use an optional paramiter to pass the lambda access to the command queue

        self.addNewEntities()
        self.inputSystem.handleInput()
        self.collisionSystem.resolve()
        self.movingSystem.timestep()

    def render(self, surface):
        self.drawingSystem.draw(surface)   
                          
    def buildScene(self):
        
        eTemp = Entity(Category.PLAYER, self.sf.getState(StateKey.PlayerStanding))
        eTemp.state.geometryComponent.location = [50,100]
        self.newEntities.append(eTemp)
        
        #####
        
        
        eTemp = Entity(Category.ENEMY, self.sf.getState(StateKey.EnemyStanding))
        eTemp.state.geometryComponent.location = [120,150]
        self.newEntities.append(eTemp)
        

        
        eTemp = Entity(Category.ENEMY, self.sf.getState(StateKey.EnemyStanding))
        eTemp.state.geometryComponent.location = [100,100]
        self.newEntities.append(eTemp)
        
    
        """
        eTemp = Entity(Category.ENEMY, self.sf.getState(StateKey.EnemyStanding))
        eTemp.state.geometryComponent.location = [200,130]
        self.newEntities.append(eTemp)
        """
        
        """
        eTemp = Entity(Category.ENEMY, self.sf.getState(StateKey.EnemyStanding))
        eTemp.state.geometryComponent.location = [160,30]
        self.newEntities.append(eTemp)
        """

    def addNewEntities(self):
        if len(self.newEntities) != 0:  
            self.entities.extend(self.newEntities)
            self.newEntities = []
            self.drawingSystem.registerEntities()
            self.collisionSystem.registerEntities()
            self.movingSystem.registerEntities()
            self.inputSystem.registerEntities()