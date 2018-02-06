

class GraphicsComponent_Standing:

    def __init__(self, filename = None):
        if filename != None:
            self.mSprite = pygame.image.load(filename).convert()
        else:
            self.mSprite = None
    
    def draw(self, location, surface):
        surface.blit(self.mSprite, location)

    def loadSprite(self, filename):
        """ loads a sprite to the entity with AABB rectangle """
        self.mSprite = pygame.image.load(filename).convert()

    def getSprite(self, sprite):
        self.mSprite = sprite
