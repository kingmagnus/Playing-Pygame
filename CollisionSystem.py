
from QuadTree import QuadTree
from pygame import Rect
from math import sqrt
from Collision import Collision
from utility import sortEntity
from itertools import combinations
from Observer import Observer, Event, Publisher


class CollisionSystem(Observer, Publisher):

    def __init__(self, positionComponents, velocityComponents, accelerationComponents, 
                    geometryComponents, collsionComponents, viewSize, dt):
        Observer.__init__(self)
        Publisher.__init__(self)

        self.positionComponents = positionComponents
        self.velocityComponents = velocityComponents
        self.accelerationComponents = accelerationComponents
        self.geometryComponents = geometryComponents
        self.collsionComponents = collsionComponents
        self.dt = dt
        self.interestingCollisions = ["Box", "Box"]

        self.__qTree = QuadTree(Rect(0,0,viewSize[0],viewSize[1]))

    def resolve(self):
        self.__qTree.empty()
        self.__qTree.addEntities(self)
        collisions = self.__qTree.findCollisions(self)
        for collision in collisions:
            self.publishEvent(collision)


    def findCollisions(self, entityIDs):
        """Returns a bool indicating if the two entities collided and a collision class which records the two entities and the lambda at which they collide"""
        collisions = []
        for e1id,e2id in combinations(entityIDs, 2):
            if( (self.collsionComponents[e1id].category,self.collsionComponents[e2id].category) in self.interestingCollisions
                or (self.collsionComponents[e2id].category,self.collsionComponents[e1id].category) in self.interestingCollisions ):
                continue

            da_x = 0
            da_y = 0
            dv_x = 0
            dv_y = 0
            if e1id in self.accelerationComponents.keys():
                da_x += self.accelerationComponents[e1id].ax
                da_y += self.accelerationComponents[e1id].ay
                dv_x += self.velocityComponents[e1id].vx
                dv_y += self.velocityComponents[e1id].vy
            elif e1id in self.velocityComponents.keys():
                dv_x += self.velocityComponents[e1id].vx
                dv_y += self.velocityComponents[e1id].vy

            if e2id in self.accelerationComponents.keys():
                da_x -= self.accelerationComponents[e2id].ax
                da_y -= self.accelerationComponents[e2id].ay
                dv_x -= self.velocityComponents[e2id].vx
                dv_y -= self.velocityComponents[e2id].vy
            elif eid in self.velocityComponents.keys():
                dv_x -= self.velocityComponents[e2id].vx
                dv_y -= self.velocityComponents[e2id].vy

            loc1 = self.positionComponents[e1id]
            loc2 = self.positionComponents[e2id]
            geom1 = self.geometryComponents[e1id]
            geom2 = self.geometryComponents[e2id]

            dx0_rl = (loc1.x + geom1.width) - loc2.x
            dx0_lr = loc1.x - (loc2.x + geom2.width)
            dy0_tb = loc1.y - (loc2.y + geom1.height)
            dy0_bt = (loc1.y + geom1.height) - loc2.y

            if da_x != 0:
                test, lx = self.__findLForAccel(da_x, dv_x, dx0_lr, dx0_rl)
            elif dv_x != 0:
                test, lx = self.__findLForVel(dv_x, dx0_lr, dx0_rl)
            else:
                test, lx = self.__findLForPos(dx0_lr, dx0_rl)

            if test == False:
                continue

            if da_y != 0:
                test, ly = self.__findLForAccel(da_y, dv_y, dy0_tb, dy0_bt)
            elif dv_y != 0:
                test, ly = self.__findLForVel(dv_y, dy0_tb, dy0_bt)
            else:
                test, ly = self.__findLForPos(dy0_tb, dy0_bt)

            if test == False:
                continue

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
                continue
            else:
                print "collision found!!!"
                collisions.append(Collision(e1id, e2id, L, axis))
        return collisions

    def __findLForAccel(self, da, dv, dx0_lr, dx0_rl):

        dis_lr = (dv)**2 - 2*da*dx0_lr
        if dis_lr >= 0:
            lx_1lr = (-dv + sqrt(dis_lr))/(da*self.dt)
            lx_2lr = (-dv - sqrt(dis_lr))/(da*self.dt)
            lx_1lr, lx_2lr = min(lx_1lr, lx_2lr), max(lx_1lr, lx_2lr)

        dis_rl = (dv)**2 - 2*da*dx0_rl
        if dis_rl >= 0:
            lx_1rl = (-dv + sqrt(dis_rl))/(da*self.dt)
            lx_2rl = (-dv - sqrt(dis_rl))/(da*self.dt)
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



    def __findLForVel(self, dv, dx0_l, dx0_r):
        # x1 = x10 + vx1*dt*lx 
        # x2 = x20 + vx2*dt*lx
        # x1 = x2 => 0 = dx0 + dvx*dt*lx 
        # => lx = -dx0 / (dvx*dt)

        l_1 = -dx0_r / (dv*self.dt)
        l_2 = -dx0_l / (dv*self.dt)
        
        L = sorted((min(l_1, l_2), max(l_1, l_2)))

        if L[0] <= 1 and L[1] >= 0:
            L = [L]
            return True, L
        else:
            return False, None

    def __findLForPos(self, dx0_less, dx0_great):
        if dx0_less < 0 and dx0_great > 0:
            return True, [(0,1)]
        else:
            return False, None


    def inBoundary(self, r1):
        """ returns a bool indicating if the entitiy is in the rect over the timestep dt """

        eInBoundary = []
        for e1id in self.collsionComponents.keys():
            da_x = 0
            da_y = 0
            dv_x = 0
            dv_y = 0
            if e1id in self.accelerationComponents.keys():
                da_x += self.accelerationComponents[e1id].ax
                da_y += self.accelerationComponents[e1id].ay
                dv_x += self.velocityComponents[e1id].vx
                dv_y += self.velocityComponents[e1id].vy
            elif e1id in self.velocityComponents.keys():
                dv_x += self.velocityComponents[e1id].vx
                dv_y += self.velocityComponents[e1id].vy

            loc1 = self.positionComponents[e1id]
            geom1 = self.geometryComponents[e1id]

            dx0_rl = (loc1.x + geom1.width) - r1.x
            dx0_lr = loc1.x - (r1.x + r1.width)
            dy0_tb = loc1.y - (r1.y + r1.height)
            dy0_bt = (loc1.y + geom1.height) - r1.y

            if da_x != 0:
                test, lx = self.__findLForAccel(da_x, dv_x, dx0_lr, dx0_rl)
            elif dv_x != 0:
                test, lx = self.__findLForVel(dv_x, dx0_lr, dx0_rl)
            else:
                test, lx = self.__findLForPos(dx0_lr, dx0_rl)

            if test == False:
                continue

            if da_y != 0:
                test, ly = self.__findLForAccel(da_y, dv_y, dy0_tb, dy0_bt)
            elif dv_y != 0:
                test, ly = self.__findLForVel(dv_y, dy0_tb, dy0_bt)
            else:
                test, ly = self.__findLForPos(dy0_tb, dy0_bt)

            if test == False:
                continue

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
                continue
            else:
                eInBoundary.append(e1id)
        return eInBoundary

   

