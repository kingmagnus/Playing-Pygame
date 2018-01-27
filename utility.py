
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


def findCollisionTime(dt, r1, r2, v1=(0,0), v2 = (0,0)):
    """ 
        Returns a tuple, the first element determining if there is a collision, the second the paramiter between 0 and 1 for how long into the time step untill a collision. If no collision time, the second element will be None

        dt = time step checked
        r1, r2 = the AABB that we are checking
        v1, v2 = the velocity of past rects
    """
    if v1[0]-v2[0] == 0 and v1[1]-v2[1] == 0:
        if r1.colliderect(r2):
            return (True, (0,"y"))
        else:
            return (False, None)


    if v1[0]-v2[0] == 0:
        #if there is no relative velocity in the x direction, we need to check if they ovlerlap on the x axis
        if r1.left < r2.right and r2.left < r1.right:
            l1 = 0
            l2 = 1
        else:
            return (False, None)
    else:
        # find lambda for objects first and last overlap along x axix 
        l1 = (r1.left - r2.right) * 1000 / ((v2[0] - v1[0]) * dt)
        l2 = (r1.right - r2.left) * 1000 / ((v2[0] - v1[0]) * dt)

    if v1[1]-v2[1] == 0:
        #if there is no relative velocity in the y direction, we need to check if they overlap
        if r1.top < r2.bottom and r2.top < r1.bottom:
            l3 = 0
            l4 = 1
        else:
            return (False, None)
    else:
        # find lambda for objects first and last overlap along y axis
        l3 = (r1.top - r2.bottom) * 1000 / ((v2[1] - v1[1]) * dt)
        l4 = (r1.bottom - r2.top) * 1000 / ((v2[1] - v1[1]) * dt)

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





