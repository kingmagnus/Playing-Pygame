
from FSMStateFactory import StateFactory, StateIDs


class FSM:
	class _Fns(object):
		__slots__ = "exitFn", "transitionFns", "entryFn"
		def __init__(self):
			self.exitFn = None
			self.transitionFns = ()
			self.entryFn = None

		def process(self, data):
			self.entryFn(data)
			for transitionFn in self.transitionFns:
				transitionFn(data)
			self.exitFn(data)

	def __init__(self):
		self.states = {
			#stateID : state
		}

		self.transitionFunctions = self._Fns() 

	def __str__(self):
		return "FSM:\n    states %s" % (self.states)

	#----------------------------------------------------------------#

	#fns for making the FMS

	def addState(self, ID):
		self.states[ID] = StateFactory(ID)

	def addTransition(self, startID, endID, testFns, transitionFns = () ):
		try:
			self.states[startID].addTransition(endID, testFns, transitionFns)
		except KeyError, message:
			print "FSM.addTransition - attepted to add transition from non existant state with ID", startID
			print message
			raise SystemExit

	#----------------------------------------------------------------#

	def run(self, data, entity):
		test, trans = self.__checkTransitions(data, entity)
		if test == True:
			self.__setTransitionFns(trans, entity)
			return True
		return False

	def __checkTransitions(self, data, entity):
		state = self.states[entity.state.inputComponent.stateID]
		for transition in state.transitions:
			if False not in (testFn(data, entity) for testFn in transition.testFns): #A good line of code :p
				return True, transition
		return False, None

	def __setTransitionFns(self, trans, entity):
		self.transitionFunctions.exitFn = self.states[entity.state.inputComponent.stateID].exitFn
		entity.state.inputComponent.stateID = trans.endID
		self.transitionFunctions.transitionFns = trans.transitionFns

		try:
			self.transitionFunctions.entryFn = self.states[trans.endID].entryFn
		except KeyError, message:
			print "FSM.__setTransitionFns - Attempted to transition to a state", trans.endID ,"that does not exist"
			print message
			raise SystemExit

