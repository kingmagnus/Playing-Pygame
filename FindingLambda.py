
from math import sqrt
from Collision import Collision
from utility import sortEntity

def findCollision(dt, e1, e2):
    """Returns a bool indicating if the two entities collided and a collision class which records the two entities and the lambda at which they collide"""

    da_x = 0
    da_y = 0
    if hasattr(e1.state, "accelerationComponent"):
        da_x += e1.state.accelerationComponent.ax
        da_y += e1.state.accelerationComponent.ay
    if hasattr(e2.state, "accelerationComponent"):
        da_x -= e2.state.accelerationComponent.ax
        da_y -= e2.state.accelerationComponent.ay

    dv_x = 0
    dv_y = 0
    if hasattr(e1.state, "velocityComponent"):
        dv_x += e1.state.velocityComponent.vx
        dv_y += e1.state.velocityComponent.vy
    if hasattr(e2.state, "velocityComponent"):
        dv_x -= e2.state.velocityComponent.vx
        dv_y -= e2.state.velocityComponent.vy

    dx0_rl = (e1.state.geometryComponent.location[0] + e1.state.geometryComponent.width) - e2.state.geometryComponent.location[0]
    dx0_lr = e1.state.geometryComponent.location[0] - (e2.state.geometryComponent.location[0] + e2.state.geometryComponent.width)
    dy0_tb = e1.state.geometryComponent.location[1] - (e2.state.geometryComponent.location[1] + e2.state.geometryComponent.height)
    dy0_bt = (e1.state.geometryComponent.location[1] + e1.state.geometryComponent.height) - e2.state.geometryComponent.location[1]

    if da_x != 0:
        test, lx = __findLForAccel(dt, da_x, dv_x, dx0_lr, dx0_rl)
    elif dv_x != 0:
        test, lx = __findLForVel(dt, dv_x, dx0_lr, dx0_rl)
    else:
        test, lx = __findLForPos(dt, dx0_lr, dx0_rl)

    if test == False:
        return False, None

    if da_y != 0:
        test, ly = __findLForAccel(dt, da_y, dv_y, dy0_tb, dy0_bt)
    elif dv_y != 0:
        test, ly = __findLForVel(dt, dv_y, dy0_tb, dy0_bt)
    else:
        test, ly = __findLForPos(dt, dy0_tb, dy0_bt)

    if test == False:
        return False, None

    L = 10 # L > 1 impies no collision

    for l1 in lx:
        if l1[0] > 1 or l1[1]<0:
            continue
        for l2 in ly:
            if l2[0] > 1 or l2[1]<0:
                continue
            if l1[0] <= l2[0] <= l1[1]:
                L = min(L, l2[0])
                axis = "y"
            if l2[0] <= l1[0] <= l2[1]:
                L = min(L, l1[0])
                axis = "x"

    if L < 0 or L > 1:
        return False, None
    else:
        print "collision found!!!"
        return True, Collision(e1, e2, L, axis)


def __findLForAccel(dt, da, dv, dx0_lr, dx0_rl):

    dis_lr = (dv)**2 - 2*da*dx0_lr
    if dis_lr >= 0:
        lx_1lr = (-dv + sqrt(dis_lr))/(da*dt)
        lx_2lr = (-dv - sqrt(dis_lr))/(da*dt)
        lx_1lr, lx_2lr = min(lx_1lr, lx_2lr), max(lx_1lr, lx_2lr)

    dis_rl = (dv)**2 - 2*da*dx0_rl
    if dis_rl >= 0:
        lx_1rl = (-dv + sqrt(dis_rl))/(da*dt)
        lx_2rl = (-dv - sqrt(dis_rl))/(da*dt)
        lx_1rl, lx_2rl = min(lx_1rl, lx_2rl), max(lx_1rl, lx_2rl)

    if dis_lr < 0 and dis_rl < 0:
        return False, None


    lx = []
    if dis_rl > 0 and dis_lr >0:
        temp = (max(0,min(lx_1rl, lx_1lr)), min(1,max(lx_1rl, lx_1lr)))
        if temp[0] <= temp[1]:
            lx.append(temp)
        temp = (max(0,min(lx_2lr, lx_2rl)), min(1,max(lx_2rl, lx_2lr)))
        if temp[0] <= temp[1]:
            lx.append(temp)

    elif dis_rl > 0:
        temp = (max(0,min(lx_1rl, lx_2rl)), min(1,max(lx_1rl, lx_2rl)))
        if temp[0] < temp[1]: 
            lx.append(temp)
    else:
        temp = (max(0,min(lx_1lr, lx_2lr)), min(1,max(lx_1lr, lx_2lr)))
        if temp[0] < temp[1]:
            lx.append(temp)


    #find the intersection of dl and [0,1]
    if len(lx)!=0:
        return True, lx
    else:
        return False, None



def __findLForVel(dt, dv, dx0_l, dx0_r):
    # x1 = x10 + vx1*dt*lx 
    # x2 = x20 + vx2*dt*lx
    # x1 = x2 => 0 = dx0 + dvx*dt*lx 
    # => lx = -dx0 / (dvx*dt)

    l_1 = -dx0_r / (dv*dt)
    l_2 = -dx0_l / (dv*dt)
    
    L = sorted((min(l_1, l_2), max(l_1, l_2)))

    if L[0] <= 1 and L[1] >= 0:
        L = [L]
        return True, L
    else:
        return False, None

def __findLForPos(dt, dx0_less, dx0_great):
    if dx0_less < 0 and dx0_great > 0:
        return True, [(0,1)]
    else:
        return False, None


def inBoundary(dt, e1, r1):
    """ returns a bool indicating if the entitiy is in the rect over the timestep dt """

    da_x = 0
    da_y = 0
    if hasattr(e1.state, "accelerationComponent"):
        da_x = e1.state.accelerationComponent.ax
        da_y = e1.state.accelerationComponent.ay

    dv_x = 0
    dv_y = 0
    if hasattr(e1.state, "velocityComponent"):
        dv_x = e1.state.velocityComponent.vx
        dv_y = e1.state.velocityComponent.vy

    dx0_rl = (e1.state.geometryComponent.location[0] + e1.state.geometryComponent.width) - r1.left
    dx0_lr = e1.state.geometryComponent.location[0] - r1.right
    dy0_tb = e1.state.geometryComponent.location[1] - r1.bottom
    dy0_bt = (e1.state.geometryComponent.location[0] + e1.state.geometryComponent.height)+ r1.top

    if da_x != 0:
        test, lx = __findLForAccel(dt, da_x, dv_x, dx0_lr, dx0_rl)
    elif dv_x != 0:
        test, lx = __findLForVel(dt, dv_x, dx0_lr, dx0_rl)
    else:
        test, lx = __findLForPos(dt, dx0_lr, dx0_rl)

    if test == False:
        return False

    if da_y != 0:
        test, ly = __findLForAccel(dt, da_y, dv_y, dy0_tb, dy0_bt)
    elif dv_y != 0:
        test, ly = __findLForVel(dt, dv_y, dy0_tb, dy0_bt)
    else:
        test, ly = __findLForPos(dt, dy0_tb, dy0_bt)

    if test == False:
        return False

    L = 10 # L > 1 impies no collision

    for l1 in lx:
        if l1[0] > 1 or l1[1]<0:
            continue
        for l2 in ly:
            if l2[0] > 1 or l2[1]<0:
                continue
            if l1[0] <= l2[0] <= l1[1]:
                L = min(L, l2[0])
            if l2[0] <= l1[0] <= l2[1]:
                L = min(L, l1[0])

    if L < 0 or L > 1:
        return False
    else:
        return True
