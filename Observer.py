
class Observer(object):
    __slots__ = []
    def __init__(self, publisher = None):
        if publisher == None:
            return 
        publisher.addObserver(self)

    def processEvent(self, event):
        print "observer update called, should be overwriten in inheritance"


class Event(object):

    def __str__(self):
        atr = dir(self)
        atr.remove("__doc__")
        atr.remove("__module__")
        atr.remove("__str__")
        mStr = "Event:\n"
        for a in atr:
            mStr = mStr + "\n    %s %s" % (a, getattr(self, a))
        return mStr

    entryState = None
    exitState = None
    direction = None
    #ect

class Publisher(object):
    __slots__ = "observers", "events"

    def __init__(self):
        self.observers = set()

    def addObserver(self, observer):
        self.observers.add(observer)

    def removeObserver(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def publishEvent(self, event):
        for observer in self.observers:
            observer.processEvent(event)

