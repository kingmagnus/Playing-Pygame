
from InputMapper import InputConstants

class TransFns:
	@staticmethod
	def Right(event):
		event.direction = "Right"

	@staticmethod
	def Left(event):
		event.direction = "Left"

class TestFns(object):
	@staticmethod
	def State_Right(mInput, entity):
		return (InputConstants.States.Right in mInput.States 
			and InputConstants.States.Left not in mInput.States)

	@staticmethod
	def State_Left(mInput, entity):
		return (InputConstants.States.Right not in mInput.States 
			and InputConstants.States.Left in mInput.States)

	@staticmethod
	def Vel_Left(mInput, entity):
		return entity.state.velocityComponent.vx < 0

	@staticmethod
	def Vel_Right(mInput, entity):
		return entity.state.velocityComponent.vx > 0

	@staticmethod
	def Vel_Max(mInput, entity):
		return abs(entity.state.velocityComponent.vx) >= entity.state.velocityComponent.maxSpeedx

	@staticmethod
	def NoInput(mInput, entity):
		return mInput.isEmpty()

	class TimeDelay:
		def __init__(self, delay):
			"""
			Arguments:
				delay - float - time untill test returns true in ms
			"""
			self.clock = pygame.time.Clock()
			self.timeElapsed = 0
			self.delay = delay

		def __call__(self, *args):
			self.timeElapsed =+ self.clock.tick()
			print self.timeElapsed
			return self.timeElapsed > self.delay
