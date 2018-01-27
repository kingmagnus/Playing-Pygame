
import Category

class Command():
    """ The Command class holds actions for the entities to act out and a list of categories that should act on the command """
    def __init__(self, action = 0, categories = [Category.NONE]):
        self.action = action
        self.categories = categories


cAccelirateUp    = Command(action = lambda entity, dt : entity.accelirate((0, -1)), categories = [Category.PLAYER])

cAccelirateDown  = Command(action = lambda entity, dt : entity.accelirate((0, 1)), categories = [Category.PLAYER])

cAccelirateLeft  = Command(action = lambda entity, dt : entity.accelirate((-1, 0)), categories = [Category.PLAYER])

cAccelirateRight = Command(action = lambda entity, dt : entity.accelirate((1, 0)), categories = [Category.PLAYER])
