
import pygame 
from pygame import K_a, K_d, K_s, K_w, K_DOWN, K_RIGHT

#------------------------------------------------#




class InputConstants:
    #Do Not Use 0!!!
    class Actions:
        #Lower Actions
        Tilt_Right = 1
        Tilt_Left = 2
        Tilt_Up = 3
        Tilt_Down = 4

    class States:
        Right = 10
        Left = 20
        Up = 30
        Down = 40

    class Ranges:
        Range_One = 100
        Range_Two = 200

class InputContext(object):
    __slots__ = '__actionMap', '__stateMap'

    def __init__(self):
        self.__actionMap = {
                            K_a: InputConstants.Actions.Tilt_Left,
                            K_d: InputConstants.Actions.Tilt_Right,
                            K_s: InputConstants.Actions.Tilt_Down,
                            K_w: InputConstants.Actions.Tilt_Up
                        }
        self.__stateMap = {
                            K_a: InputConstants.States.Left,
                            K_d: InputConstants.States.Right,
                            K_s: InputConstants.States.Down,
                            K_w: InputConstants.States.Up
                        }

    def MapButtonToAction(self, button):
        # map a raw button to an action
        if button in self.__actionMap.keys():
            action = self.__actionMap[button]
            return action
        return None

    def MapButtonToState(self, button):
        # map a raw button to a state
        if button in self.__stateMap.keys():
            state = self.__stateMap[button]
            return state
        return None

#------------------------------------------------#

class MappedInput(object):
    __slots__ = 'Actions', 'States'

    Actions = set()
    States  = set()

    def __str__(self):
        return "MappedInput:\n    Actions are %s\n    States is %s" % (self.Actions, self.States)

    def isEmpty(self):
        if len(self.Actions) == 0 and len(self.States) == 0:
            return True
        return False

    def EatAction(self, action):
        self.Actions.remove(action)

    def EatState(self, state):
        self.States.remove(state)

#------------------------------------------------#

class RawInput:

    class Button(object):
        __slots__ = 'pressed', 'previouslyPressed'
        def __init__(self):
            self.pressed = False
            self.previouslyPressed = False

    def __init__(self): # pass pygame.key.get_pressed()
        self.__buttons = tuple(self.Button() for i in range(133)) # pygame has 133 Button inputs

    def size(self):
        return len(self.__buttons)

    def __len__(self):
        return len(self.__buttons)

    def __getitem__(self, i):
        try:
            return self.__buttons[i]
        except IndexError as error:
            print ("IndexError: list index out of Range in RawInput.__buttons")
            print(error)
            raise SystemExit

    def Update(self):
        """
        Calls pygame.key.get_pressed() and updates self.__buttons, recoriding their last state and their current state
        """
        rawInput = pygame.key.get_pressed()
        for i in range(133):
            self.__buttons[i].previouslyPressed = self.__buttons[i].pressed
            self.__buttons[i].pressed = rawInput[i]


#------------------------------------------------#

class InputMapper:
    """
    Class that will process input into actions and states useable by systems.

    The raw input is translated into actions and sates using InputContext

    Fns:
        MapInput()
            This will take all input since it was last called and return an instance of the 
            mapped input class containg all actions and states the input maps to
 
        Clear()
            Dont use

    """

    def __init__(self):
        self.__rawInput = RawInput()
        self.__context = InputContext()
        self.__mappedInput = MappedInput()

    def Clear(self):
        self.__mappedInput.Actions.clear()
        self.__mappedInput.States.clear()
        # Note: we do NOT clear states, because they need to remain set
        # across frames so that they don't accidentally show "off" for
        # a tick or two while the raw input is still pending.

        # Play with this to understand it

    def MapInput(self): # pass pygame.key.get_pressed()
        self.__rawInput.Update() # update pressed and not pressed
        self.Clear() # remover all actions and states from mappedinput
        for i in range(self.__rawInput.size()):
            self.__RawToInput(i, self.__rawInput[i])
        #self._RefineInput() 
        return self.__mappedInput

    #
    # fns for finding input

    def __RawToInput(self, button, buttonState):

        #checks if a button was newly pressed to prevent being called again for actions
        if buttonState.pressed and not buttonState.previouslyPressed:
            action =self.__context.MapButtonToAction(button)
            if action:
                self.__mappedInput.Actions.add(action)
                return

        #checks if a button if held for states
        if buttonState.pressed:
            state = self.__context.MapButtonToState(button)
            if state:
                self.__mappedInput.States.add(state)
                return

        #if the button corisponds to an action/state that does not need to be active we remove it from _mappedInput
        #self._MapAndEatButton(button)

    # end
    #


    
















#https://www.gamedev.net/articles/programming/general-and-gameplay-programming/designing-a-robust-input-handling-system-for-games-r2975



#raw input gathering

#input mapping 
#despatching 

#high level handler



#contexts dictate what inputs are available eg menu, title screen, mainn game


#Types of input:
# 1. Actions - single thing eg. cast spell, open door - one off actions that occure when buttion is pressed (releced), do not depend on key repeat
# 2. States - continuous activities - running shooting. Will be a binary flag - state is on or off. If on, the corrisponding action is performed , if off then not
# 3. Ranges - input can take a range of values (say 0,1 or -1, 1) good for analoge input 

# Each context defiens an input map - takes raw input and translate to final type of input, "an input mapper is really a set of code that can convert raw input IDs to high-level context-dependent IDs"
# one to one fn between context and inputmap
# More than one context can be active at one, eg. one for walking/running around willbe used all the time, and others might be dependent on things such as the current weapon
#one posible implimentation is a list of contexts, and if one reacts then stop, if not pass to the next in the list
# "Chain of Responsibility pattern"


# callbacks code design 
# (Callback - a fn pointer)
# 1. Each frame get raw input
# 2. Evaluate current contexts to find list of actions, states and ranges
# 3. put input into approprite structure 
# 4. pass structure through ordered list of callbacks
# 5. if callback uses input, remove input from structure

# Summery: 
# raw input -> context List -> input data structure -> callback list -> Callback data structure -> perform callbacks
