

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

#------------------------------------------------#

class _LowerContextID:
    Directions = 0
    Attacking  = 1
    
    IDs = [Directions, Attacking]
    

class LowerContextMaker:

    def Make(self, ID):
        return self._IDMap[ID]()
        
    def _Directions(self):
        action = {K_a: InputConstants.Action.Tilt_Left,
                  K_d: InputConstants.Action.Tilt_Right,
                  K_s: InputConstants.Action.Tilt_Down,
                  K_w: InputConstants.Action.Tilt_Up}
        state  = {K_a: InputConstants.State.Left,
                  K_d: InputConstants.State.Right,
                  K_s: InputConstants.State.Down,
                  K_w: InputConstants.State.Up}
        return action, state

    def _Attacking(self):
        action = {K_down : InputConstants.Action.Main_Attack,
                  K_Right: InputConstants.Action.Special_Attack}
        state  = {}
        return action, state


    _IDMap = {_LowerContextID.Directions : _Directions,
             _LowerContextID.Attacking  : _Attacking}

class _HigherContextID:
    TiltAttack = 0
    
    IDs = [TiltAttack]

class HigerContextMaker:

    def Make(self, ID):
        return self._IDMap[ID]()
        
    def _TiltAttack(self):
        action = {(InputConstants.Action.Main_attack   , InputConstants.Action.Tilt_Right) : InputConstants.Action.Tilt_Right_Main_Attack,
                  (InputConstants.Action.Main_attack   , InputConstants.Action.Tilt_Left)  : InputConstants.Action.Tilt_Left_Main_Attack,
                  (InputConstants.Action.Main_attack   , InputConstants.Action.Tilt_Up)    : InputConstants.Action.Tilt_Up_Main_Attack,
                  (InputConstants.Action.Main_attack   , InputConstants.Action.Tilt_Down)  : InputConstants.Action.Tilt_Down_Main_Attack, 
                  (InputConstants.Action.Special_attack, InputConstants.Action.Tilt_Right) : InputConstants.Action.Tilt_Right_Special_Attack,
                  (InputConstants.Action.Special_attack, InputConstants.Action.Tilt_Left)  : InputConstants.Action.Tilt_Left_Special_Attack,
                  (InputConstants.Action.Special_attack, InputConstants.Action.Tilt_Up)    : InputConstants.Action.Tilt_Up_Special_Attack,
                  (InputConstants.Action.Special_attack, InputConstants.Action.Tilt_Down)  : InputConstants.Action.Tilt_Down_Special_Attack}
        state = {}
        return action, state

    
    _IDMap = {_HigherContextID.TiltAttack  : _TiltAttack}

#------------------------------------------------#

class InputLowerContext:

    def __init__(self, lowerContextID):
        self._actionMap, self._stateMap = LowerContextMaker.Make(lowerContextID)

    def MapButtonToAction(self, button, action):
        # map a raw button to an action
        if button in self._actionMap.keys():
            action = self._actionMap[button]
            return True
        return False

    def MapButtonToState(self, button, action):
        # map a raw button to a state
        if button in self._stateMap.keys():
            action = self._stateMap[button]
            return True
        return False

class InputRefineContext:

    def __init__(self, HigherContextID):
        self._actionMap, self._stateMap = HigherContextMaker.Make(lowerContextID)

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
        self._buttons = (self.Button(),) * 133 # pygame has 133 Button inputs

    def size():
        return 133

    def __getitem__(self, i):
        try:
            return self._buttons[i]
        except IndexError:
            print "IndexError: list index out of Range in RawInput"
            raise SystemExit

    def Update(self, rawInput): # pass pygame.key.get_pressed()
        for i in range(133):
            self._buttons[i].previouslyPressed = self._buttons[i].pressed
            self._buttons[i].pressed = rawInput[i]

#------------------------------------------------#

class InputMapper:

    _rawInput = RawInput()
    _inputLowerContext = {}                  #{contextID: InputContext}
    _activeLowerContexts = set()
    _inputHigherContext = {}                 #{contextID: InputContext}
    _activeHigherContexts = set()
    _mappedInput = MappedInput()

    def __init__(self):
        #make all contexts
        for ID in _LowerContextID.IDs:
            self._inputLowerContext[ID] = self.InputLowerContext(ID)
        for ID in _HigherContextID.IDs:
            self._inputHigherContext[ID] = self.InputHigherContext(ID)

    def Clear(self):
        self._mappedInput.Actions.clear()
        self._mappedInput.States.clear()
        # Note: we do NOT clear states, because they need to remain set
        # across frames so that they don't accidentally show "off" for
        # a tick or two while the raw input is still pending.

        # Play with this to understand it

    def MapInput(self, rawInput): # pass pygame.key.get_pressed()
        self._rawInput.Update(rawInput) # update pressed and not pressed
        self.clear() # remover all actions and states from mappedinput
        for i in self._rawInput.size():
            _RawToLowerInput(i, rInput[i])
        _RefineLowerInput() 
        return _mappedInput        

    #
    # fns for dealing with contexts
    def pushLowerContext(self, contextID):
        self._activeLowerContexts.add(self._inputLowerContext[contextID])

    def popLowerContext():
        self._activeLowerContexts.remove(self._inputLowerContext[contextID])

    def pushHigherContext(self, contextID):
        self._activeHeigherContexts.add(self._inputHeigherContext[contextID])

    def popHeigherContext():
        self._activeHeigherContexts.remove(self._inputHeigherContext[contextID])
    # end
    #


    #
    # fns for finding input
    def _MapButtonToAction(self, button, actions):
        for context in self._activeLowerContexts:
            if context.MapButtonToAction(button, action):
                return True
        return False

    def _MapButtonToState(self, button, state):
        for context in self._activeLowerContexts:
            if context.MapButtonToState(button, state):
                return True
        return False

    def _RawToLowerInput(self, button, buttonState):
        action = 1
        state  = 2

        #checks if a button was newly pressed to prevent being called again for actions
        if buttonState.pressed and not buttonState.previouslypressed:
            if self._MapButtonToAction(button, action):
                self._mappedInput.Actions.add(action)
                return

        #checks if a button if held for states
        if buttonState.pressed:
            if self._MapButtonToState(button, state):
                self._mappedInput.States.add(state)
                return

        #if the button corisponds to an action/state that does not need to be active we remove it from _mappedInput
        #self._MapAndEatButton(button)

    def _RefineLowerInput(self):
        for hContext in self._activeHigherContexts:
            hContext.RefineLowerToHigher(_mappedInput)
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


    














