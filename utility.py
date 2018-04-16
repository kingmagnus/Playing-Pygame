
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

def sortEntity(e1, e2):
    return (e1, e2) if e1.id < e2.id else (e2, e1)






