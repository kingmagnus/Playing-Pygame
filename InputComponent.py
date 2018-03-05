
import Reactions

playerStanding = 0

class InputComponent:
    def __init__(self, inputId = playerStanding):
        try:
            self.reactions = Reactions.Map[inputId]()
        except KeyError:
            print "inputID", inputId, "not in the reactions map"
            raise SystemExit





