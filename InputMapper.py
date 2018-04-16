

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



from InputConstants import InputConstants
import pygame 
from pygame import K_a, K_d, K_s, K_w, K_DOWN, K_RIGHT

#------------------------------------------------#

class LowerContextID:
    Directions = 0
    Attacking  = 1
    
    IDs = (Directions, Attacking)
    

class LowerContextMaker:
        
    def __getitem__(self, key):
        try:
            return self.__IDMap[key]()
        except IndexError as error:
            print ("IndexError: list index out of Range in LowerContextMaker")
            print(error)
            raise SystemExit

    
    def __Directions():
        action = {K_a: InputConstants.Action.Tilt_Left,
                  K_d: InputConstants.Action.Tilt_Right,
                  K_s: InputConstants.Action.Tilt_Down,
                  K_w: InputConstants.Action.Tilt_Up}
        state  = {K_a: InputConstants.State.Left,
                  K_d: InputConstants.State.Right,
                  K_s: InputConstants.State.Down,
                  K_w: InputConstants.State.Up}
        return action, state

    def __Attacking():
        action = {K_DOWN : InputConstants.Action.Main_Attack,
                  K_RIGHT: InputConstants.Action.Special_Attack}
        state  = {}
        return action, state


    __IDMap = {LowerContextID.Directions : __Directions,
               LowerContextID.Attacking  : __Attacking}

class HigherContextID:
    TiltAttack = 0
    
    IDs = (TiltAttack,)

class HigherContextMaker:

    def __getitem__(self, key):
        try:
            return self.__IDMap[key]()
        except IndexError as error:
            print ("IndexError: list index out of Range in LowerContextMaker")
            print(error)
            raise SystemExit
        
    def __TiltAttack():
        action = {(InputConstants.Action.Main_Attack   , InputConstants.Action.Tilt_Right) : InputConstants.Action.Tilt_Right_Main_Attack,
                  (InputConstants.Action.Main_Attack   , InputConstants.Action.Tilt_Left)  : InputConstants.Action.Tilt_Left_Main_Attack,
                  (InputConstants.Action.Main_Attack   , InputConstants.Action.Tilt_Up)    : InputConstants.Action.Tilt_Up_Main_Attack,
                  (InputConstants.Action.Main_Attack   , InputConstants.Action.Tilt_Down)  : InputConstants.Action.Tilt_Down_Main_Attack, 
                  (InputConstants.Action.Special_Attack, InputConstants.Action.Tilt_Right) : InputConstants.Action.Tilt_Right_Special_Attack,
                  (InputConstants.Action.Special_Attack, InputConstants.Action.Tilt_Left)  : InputConstants.Action.Tilt_Left_Special_Attack,
                  (InputConstants.Action.Special_Attack, InputConstants.Action.Tilt_Up)    : InputConstants.Action.Tilt_Up_Special_Attack,
                  (InputConstants.Action.Special_Attack, InputConstants.Action.Tilt_Down)  : InputConstants.Action.Tilt_Down_Special_Attack}
        state = {}
        return action, state

    
    __IDMap = {HigherContextID.TiltAttack  : __TiltAttack}

#------------------------------------------------#

class InputLowerContext:

    def __init__(self, lowerContextID):
        self._actionMap, self._stateMap = LowerContextMaker.Make(lowerContextID)

    def MapButtonToAction(self, button):
        # map a raw button to an action
        if button in self._actionMap.keys():
            action = self._actionMap[button]
            return True, action
        return False, None

    def MapButtonToState(self, button):
        # map a raw button to a state
        if button in self._stateMap.keys():
            state = self._stateMap[button]
            return True, state
        return False, None

class InputRefineContext:

    def __init__(self, HigherContextID):
        self._actionMap, self._stateMap = HigherContextMaker.Make(HigherContextID)

    def RefineLowerToHigher(self, mappedInput, action):
        # map a combo of actions to to an action
        for combo in self._actionMap.keys():
            if mappedInput.Actions >= combo: #check is one is subset of other
                mappedInput.Actions -= combo
                mappedInput.Actions.add(self._actionMap[combo])

        for combo in self._stateMap.keys():
            if mappedInput.States >= combo: #check is one is subset of other
                mappedInput.States -= combo
                mappedInput.States.add(self._stateMap[combo])

    #def MapButtonToState(self, button, action):
    #    # map a raw button to a state
    #    if button in _stateMap.keys():
    #        action = _stateMap[button]
    #        return True
    #    return False

#------------------------------------------------#

class MappedInput:
    Actions = set()
    States  = set()
    
    def EatAction(self, action):
        self.Actions.remove(action)

    def EatState(self, state):
        self.States.remove(state)

#------------------------------------------------#

class RawInput:

    class Button:
        pressed = False
        previouslyPressed = False

    def __init__(self): # pass pygame.key.get_pressed()
        self.__buttons = (self.Button(),) * 133 # pygame has 133 Button inputs

    def size(self):
        return len(self.__buttons)

    def __getitem__(self, i):
        try:
            return self.__buttons[i]
        except IndexError as error:
            print ("IndexError: list index out of Range in RawInput")
            print(error)
            raise SystemExit

    def Update(self, rawInput): # pass pygame.key.get_pressed()
        if rawInput[K_a]:
            print ("K_a pressed") 
        for i in range(133):
            self.__buttons[i].previouslyPressed = self.__buttons[i].pressed
            self.__buttons[i].pressed = rawInput[i]

#------------------------------------------------#

class InputMapper:

    def __init__(self):
        self.__rawInput = RawInput()
        self.__inputLowerContext = {}                  #{contextID: InputContext}
        self.__activeLowerContexts = set()
        self.__inputHigherContext = {}                 #{contextID: InputContext}
        self.__activeHigherContexts = set()
        self._mappedInput = MappedInput()
        
        lowerContextMaker = LowerContextMaker()
        higherContextMaker = HigherContextMaker()
        
        #make all contexts
        for key in LowerContextID.IDs:
            self.__inputLowerContext[key] = lowerContextMaker[key]
        for key in HigherContextID.IDs:
            self.__inputHigherContext[key]= higherContextMaker[key]

    def Clear(self):
        self._mappedInput.Actions.clear()
        self._mappedInput.States.clear()
        # Note: we do NOT clear states, because they need to remain set
        # across frames so that they don't accidentally show "off" for
        # a tick or two while the raw input is still pending.

        # Play with this to understand it

    def MapInput(self): # pass pygame.key.get_pressed()
        self.__rawInput.Update(pygame.key.get_pressed()) # update pressed and not pressed
        self.Clear() # remover all actions and states from mappedinput
        for i in range(self.__rawInput.size()):
            self._RawToLowerInput(i, self.__rawInput[i])
        self._RefineLowerInput() 
        return self._mappedInput        

    #
    # fns for dealing with contexts
    def pushLowerContext(self, contextID):
        self.__activeLowerContexts.add(self.__inputLowerContext[contextID])

    def popLowerContext(self, contextID):
        self.__activeLowerContexts.remove(self.__inputLowerContext[contextID])

    def pushHigherContext(self, contextID):
        self.__activeHeigherContexts.add(self.__inputHeigherContext[contextID])

    def popHeigherContext(self, contextID):
        self.__activeHeigherContexts.remove(self.__inputHeigherContext[contextID])
    # end
    #


    #
    # fns for finding input
    def _MapButtonToAction(self, button):
        for context in self._activeLowerContexts:
            test, action = context.MapButtonToAction(button)
            if test:
                return True, action
        return False, None

    def _MapButtonToState(self, button):
        for context in self._activeLowerContexts:
            test, state = context.MapButtonToState(button)
            if test:
                return True, state
        return False, None

    def _RawToLowerInput(self, button, buttonState):

        #checks if a button was newly pressed to prevent being called again for actions
        if buttonState.pressed and not buttonState.previouslypressed:
            test, action = self._MapButtonToAction(button)
            if test:
                self._mappedInput.Actions.add(action)
                return

        #checks if a button if held for states
        if buttonState.pressed:
            test, state = self._MapButtonToAction(button)
            if test:
                self._mappedInput.States.add(state)
                return

        #if the button corisponds to an action/state that does not need to be active we remove it from _mappedInput
        #self._MapAndEatButton(button)

    def _RefineLowerInput(self):
        for hContext in self.__activeHigherContexts:
            hContext.RefineLowerToHigher(self._mappedInput)
    # end
    #

    def _MapAndEatButton(self, button):
        """Will remove action/state from mapped input if button is an action/state"""
        action = 1
        state  = 1

        if self._MapButtonToLowerAction(button, action):
            self._mappedInput.EatAction(action)

        if self._MapButtonToLowerState(button, state):
            self._mappedInput.EatState(state)


    














