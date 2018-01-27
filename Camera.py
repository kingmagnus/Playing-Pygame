
from pygame import Rect

class Camera(object):
    def __init__(self, view_updater, viewSize):
        """	camera_func - describes how the camera should move when update is called
	        width - the width of the camera
	        height - the height of the camera """
        #self.camera_func is a function which describes how the view should change 
        self.view_updater = view_updater
        #self.view is the rect describing where in the world we render
        self.view = (0, 0, viewSize[0], viewSize[1])
        self.halfCenter = [viewSize[0]/2, viewSize[1]/2]

    def applyView(self, target):
        """ moves the passed target by moving it relative to the view"""
        return target.move(self.view.topleft)

    def updateView(self, target):
        """moves the camera based on the location of target, usualy the player"""
        self.view = self.view_updater(self.view, target)




#####################################




def ViewTrackingMover(view, target_rect):
    #changing from world coordinates to view coordinates
    tCenterX, tCenterY    = target_rect.center
    _, _, vWidth, vHeight = view
    
    return Rect( -tCenterX + vWidth /2, -tCenterY + vHeight/2, vWidth, vHeight)

def ViewEntityTrackingMover(view, target_entity):
    #changing from world coordinates to view coordinates
    tCenterX, tCenterY    = target_entity.AABB.center
    _, _, vWidth, vHeight = view
    
    return Rect( -tCenterX + vWidth /2, -tCenterY + vHeight/2, vWidth, vHeight)







