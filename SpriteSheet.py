
import pygame

class SpriteSheet():
    """ Class used to access images from a sprite sheet """

    def __init__(self, file_name):
        """ Constuctor. PAss the file name of the spritesheet """

        try:
            self.sprite_sheet = pygame.image.load(file_name).convert()
        except pygame.error, message:
            print "Unable to load spritesheet ", file_name
            raise SystemExit, message


    def getImage(self, rectangle):
        """ Returns a subimage from tuple rectangle with (x, y and with width, height) """

        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sprite_sheet, (0,0), rect)

        return image


    def getImages(self, rectangles):
        """ Returns subimages with top left location x, y and with width and height """
        return [self.getImage(rect) for rect in rectangles]


