from FSMStateFactory import StateFactory, StateIDs


class FSM:
	class _Fns(object):
		__slots__ = "exitFn", "transitionFns", "entryFn"
		def __init__(self):
			self.exitFn = None
			self.transitionFns = ()
			self.entryFn = None

		def process(self, inputEvent):
			"""
				Called from InputSystem when an a transition is made.
				Takes an inputEvent which it adds inforation to for publishing to other systems.
			"""
			self.entryFn(inputEvent)
			for transitionFn in self.transitionFns:
				transitionFn(inputEvent)
			self.exitFn(inputEvent)

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

	#fns for running the fsm with an inputcomponent

	def run(self, inputData, **kargs):
		test, trans = self.__checkTransitions(inputData, kargs)
		if test == True:
			self.__setTransitionFns(trans, kargs["inputComponent"])
			return True
		return False

	def __checkTransitions(self, inputData, components):
		state = self.states[components["inputComponent"].stateID]
		for transition in state.transitions:
			if False not in (testFn(inputData, components) for testFn in transition.testFns): #A good line of code :D
				return True, transition
		return False, None

	def __setTransitionFns(self, trans, inputComponent):
		self.transitionFunctions.exitFn = self.states[inputComponent.stateID].exitFn
		inputComponent.stateID = trans.endID
		self.transitionFunctions.transitionFns = trans.transitionFns

		try:
			self.transitionFunctions.entryFn = self.states[trans.endID].entryFn
		except KeyError, message:
			print "FSM.__setTransitionFns - Attempted to transition to a state", trans.endID ,"that does not exist"
			raise KeyError, message

