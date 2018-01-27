

from SpriteSheet import *

class SpriteAnimation():
    """Collects images from sprite sheet for animation"""

    def __init__(self, filename, rects, count, loop = False, frames = 1):
        """construct a SpriteAnimation

           rects is a list of rectangels on the spritesheet 

           loop is a bool that casuses next to return to the origional sprite when it has reached the last sprite

           count is the number of sprites

           frames is the number of frames per sprite"""

        self.filename = filename
        ss = SpriteSheet(filename)
        self.images = ss.getImages(rects)
        self.counter = 0
        self.loop = loop
        self.frames = frames

    def next(self):
        if self.counter >= len(self.images):
            if not self.loop:
                raise StopIteration
            else:
                self.counter = 0
        
        image = self.images[self.counter]
        self.counter +=1
        return image

    def __add__(self, ss):
        self.images.extend(ss.images)
        return self










