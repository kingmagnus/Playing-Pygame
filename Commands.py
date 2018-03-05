
def accelerateUp(entity):
    try:
        entity.state.velocityComponent.direction[1] = entity.state.velocityComponent.direction[1] - 1
    except AttributeError:
        print "tried to accerate entity with no velocityComponent in Commands"
        raise SystemExit

def accelerateDown(entity):
    try:
        entity.state.velocityComponent.direction[1] = entity.state.velocityComponent.direction[1] + 1
    except AttributeError:
        print "tried to accerate entity with no velocityComponent in Commands"
        raise SystemExit

def accelerateLeft(entity):
    try:
        entity.state.velocityComponent.direction[0] = entity.state.velocityComponent.direction[0] - 1
    except AttributeError:
        print "tried to accerate entity with no velocityComponent in Commands"
        raise SystemExit

def accelerateRight(entity):
    try:
        entity.state.velocityComponent.direction[0] = entity.state.velocityComponent.direction[0] + 1
    except AttributeError:
        print "tried to accerate entity with no velocityComponent in Commands"
        raise SystemExit
