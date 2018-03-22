


import Commands 
import ReactionKey
from InputMapper import InputMapper


import pygame



class InputSystem:
    def __init__(self):
        _commandTable = {} #{int: inputCallback}
        self._inputMapper  = InputMapper()

    def handleInput(self, entities):
        mInput = self._inputMapper.MapInput(pygame.key.get_pressed())
        for key in sorted(_callbackTable):
                self._commandTable[key](mInput, entities)

    def AddCommand(self, command, priority):
        self._commandTable[priority] = command

