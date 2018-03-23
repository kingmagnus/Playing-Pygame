


import Commands 
import ReactionKey
from InputMapper import InputMapper
from System import EntityRegister

import pygame



class InputSystem:
    def __init__(self):
        __inputRegister = EntityRegister('inputComponent')
        __commandTable = {} #{int: inputCallback}
        self._inputMapper  = InputMapper()

    def handleInput(self, entities):
        mInput = self._inputMapper.MapInput(pygame.key.get_pressed())
        for key in sorted(_callbackTable):
            for i in __inputRegister:
            self.__commandTable[key](mInput, entities[i])

    def AddCommand(self, command, priority):
        self.__commandTable[priority] = command

