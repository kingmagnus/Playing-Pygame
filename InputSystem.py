


import Commands 
import ReactionKey

import pygame



class InputSystem:
    def __init__(self):
        self.responseDict = {ReactionKey.AccelerateUp   : Commands.accelerateUp,
                             ReactionKey.AccelerateDown : Commands.accelerateDown,
                             ReactionKey.AccelerateLeft : Commands.accelerateLeft, 
                             ReactionKey.AccelerateRight: Commands.accelerateRight}
        
    def handleInput(self, entities):
        # 1. for all entities try to access input component, if not there continue to the next entity
        # 2. for each key in the entity's input component, use the appropriate response from the respeonse dictionry 
        
        for entity in entities:
            try:
                reactions = []
                for key in entity.state.inputComponent.reactions.keys():
                    if pygame.key.get_pressed()[key]:
                        reaction = entity.state.inputComponent.reactions[key]
                        self.responseDict[reaction](entity)                    

            except AttributeError:
                continue
            except KeyError:
                print "---reaction key not found in responseDict---"
                raise SystemExit
            


