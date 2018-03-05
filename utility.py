
def unitVector(vec):
    size = getSize(vec)
    if(size == 0):
        return vec
    else:
        size = float(size)
        return [x / size for x in vec]

def getSize(vec):
    size = 0
    for x in vec:
        size += x**2
    size = size**0.5
    return size

def sortRect(rect1, rect2):
    if rect1.left < rect2.left:
        return (rect1, rect2) 
    else:
        return (rect2, rect1)

def appendUnique(mList, mObject):
    if mObject not in mList:
        mList.append(mObject)

def entityCollision(e1, e2):
    return e1.AABB.colliderect(e2.AABB)

def sortEntity(e1, e2):
    if e1.id < e2.id:
        return (e1, e2) 
    else:
        return (e2, e1)



def findCollisionTime(dt, entity1, entity2):
    """ 
        Returns a tuple, the first element determining if there is a collision, the second the paramiter between 0 and 1 for how long into the time step untill a collision. If no collision time, the second element will be None

        dt = time step checked
        r1, r2 = the AABB that we are checking
        v1, v2 = the velocity of past rects
    """
    e1left   = entity1.state.geometryComponent.location[0]
    e1top    = entity1.state.geometryComponent.location[1]
    e1right  = e1left + entity1.state.geometryComponent.width 
    e1bottom = e1top + entity1.state.geometryComponent.height 
    
    try:
        v1 = [ i * entity1.state.velocityComponent.speed for i in unitVector(entity1.state.velocityComponent.direction)]
    except AttributeError:
        v1 = [0,0]

    e2left   = entity2.state.geometryComponent.location[0]
    e2top    = entity2.state.geometryComponent.location[1]
    e2right  = e2left + entity2.state.geometryComponent.width 
    e2bottom = e2top + entity2.state.geometryComponent.height 

    try:   
        v2 = [ i * entity2.state.velocityComponent.speed for i in unitVector(entity2.state.velocityComponent.direction)]
    except AttributeError:
        v2 = [0,0]


    if v1[0]-v2[0] == 0 and v1[1]-v2[1] == 0:
        if e1left < e2right and e2left < e1right and e1top < e2bottom and e2top < e1bottom:
            return (True, (0,"y"))
        else:
            return (False, None)


    if v1[0]-v2[0] == 0:
        #if there is no relative velocity in the x direction, we need to check if they ovlerlap on the x axis
        if e1left < e2right and e2left < e1right:
            l1 = 0
            l2 = 1
        else:
            return (False, None)
    else:
        # find lambda for objects first and last overlap along x axix 
        l1 = (e1left - e2right) * 1000 / ((v2[0] - v1[0]) * dt)
        l2 = (e1right - e2left) * 1000 / ((v2[0] - v1[0]) * dt)

    if v1[1]-v2[1] == 0:
        #if there is no relative velocity in the y direction, we need to check if they overlap
        if e1top < e2bottom and e2top < e1bottom:
            l3 = 0
            l4 = 1
        else:
            return (False, None)
    else:
        # find lambda for objects first and last overlap along y axis
        l3 = (e1top - e2bottom) * 1000 / ((v2[1] - v1[1]) * dt)
        l4 = (e1bottom - e2top) * 1000 / ((v2[1] - v1[1]) * dt)

    dlx = [l1,l2]
    dlx.sort()
    
    dly = [l3,l4]
    dly.sort()


    #if the following inequalities are <=, the objects get stuck together

    if dlx[0] < dly[1] and dlx[1] > dly[0]:
        dl = [max(dlx[0],dly[0]), min(dlx[1],dly[1])]
        if dlx[0] > dly[0]:
            xy = "x"        
        elif dlx[0] < dly[0]:
            xy = "y" 
        else:
            xy = "xy"
    else:
        return (False, None)

    if dl[0] < 1 and dl[1] > 0:
        return (True, (max(dl[0],0), xy))

    return (False, None)


def checkInBoundary(dt, entity, r2):
    """ 
        Returns a bool, true if then entity is in the boundary during the time dt


        dt = time step checked
        entity = the entity that we are checking
        boundary = the pygame.Rect we are checking against
    """
    eleft   = entity.state.geometryComponent.location[0]
    etop    = entity.state.geometryComponent.location[1]
    eright  = eleft + entity.state.geometryComponent.width 
    ebottom = etop + entity.state.geometryComponent.height 

    try:
        return _checkInBoundaryWithV(dt, entity, r2)
    except AttributeError:
        return _checkInBoundaryWithOutV(dt, entity, r2)  


def _checkInBoundaryWithV(dt, entity, r2):
    """ 
        Returns a bool, true if then entity is in the boundary during the time dt



        dt = time step checked
        entity = the entity that we are checking

        boundary = the pygame.Rect we are checking against
    """
    v1 = [ i * entity.state.velocityComponent.speed for i in unitVector(entity.state.velocityComponent.direction)]
    eleft   = entity.state.geometryComponent.location[0]
    etop    = entity.state.geometryComponent.location[1]
    eright  = eleft + entity.state.geometryComponent.width 
    ebottom = etop + entity.state.geometryComponent.height 


    if v1[0] == 0:
        #if there is no relative velocity in the x direction, we need to check if they ovlerlap on the x axis
        if eleft < r2.right and r2.left < eright:
            l1 = 0
            l2 = 1
        else:
            return False
    else:
        # find lambda for objects first and last overlap along x axix 
        l1 = (eleft - r2.right) * 1000 / (- v1[0] * dt)
        l2 = (eright - r2.left) * 1000 / (- v1[0] * dt)

    if v1[1] == 0:
        #if there is no relative velocity in the y direction, we need to check if they overlap
        if etop < r2.bottom and r2.top < ebottom:
            l3 = 0

            l4 = 1
        else:
            return False
    else:
        # find lambda for objects first and last overlap along y axis
        l3 = (etop - r2.bottom) * 1000 / (- v1[1] * dt)
        l4 = (ebottom - r2.top) * 1000 / (- v1[1] * dt)

    dlx = [l1,l2]
    dlx.sort()
    
    dly = [l3,l4]
    dly.sort()


    #if the following inequalities are <=, the objects get stuck together

    if dlx[0] < dly[1] and dlx[1] > dly[0]:
        dl = [max(dlx[0],dly[0]), min(dlx[1],dly[1])]
    else:
        return False

    if dl[0] < 1 and dl[1] > 0:
        return True

    return False


def _checkInBoundaryWithOutV(dt, entity, r2):
    """ 
        Returns a bool, true if then entity is in the boundary during the time dt


        dt = time step checked
        entity = the entity that we are checking
        boundary = the pygame.Rect we are checking against
    """
    eleft   = entity.state.geometryComponent.location[0]
    etop    = entity.state.geometryComponent.location[1]
    eright  = eleft + entity.state.geometryComponent.width 
    ebottom = etop + entity.state.geometryComponent.height 

    if eleft < r2.right and r2.left < eright:
        l1 = 0
        l2 = 1
    else:
        return False
    
    if etop < r2.bottom and r2.top < ebottom:
        l3 = 0
        l4 = 1
    else:
        return False
    
    dlx = [l1,l2]
    dlx.sort()
    
    dly = [l3,l4]
    dly.sort()

    #if the following inequalities are <=, the objects get stuck together

    if dlx[0] < dly[1] and dlx[1] > dly[0]:
        dl = [max(dlx[0],dly[0]), min(dlx[1],dly[1])]
    else:
        return False

    if dl[0] < 1 and dl[1] > 0:
        return True

    return False





