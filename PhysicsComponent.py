

class PhysicsComponent:
    gravityAcceliration = (0,1)
    _falling = Command(action = lambda entity, dt : entity.accelirate((0, 1)), categories = [Category.PLAYER])


    def update(self, commandQueue):
        commandQueue.append(_falling)
