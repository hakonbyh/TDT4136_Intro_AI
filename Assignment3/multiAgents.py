# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).



# ******************************  Change  ******************************

"""
    I have experimented with many different solutions. Below version can be specified.
    version 0 form pseudocode in textbook.
    version 1 my own implementation. Not functioning.
    version 'A' is august loennings implementation.
"""

VERSION = 0


# ****************************  Change over ****************************

from util import manhattanDistance
from game import Directions
import random, util

from game import Agent


class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):

        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
          Returns a list of legal actions for an agent
          agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
          Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
          Returns the total number of agents in the game
        """
# ******************************  Change  ******************************
        if VERSION == 0:
            return self.getActionV0(gameState)
        elif VERSION == 1:
            return self.getActionV1(gameState)
        elif VERSION == 'A':
            return self.getActionA(gameState)

    # ****************************  Version 0 ****************************
    def getActionV0(self, gameState):
        bestAction = ""
        bestValue = -100000
        depth = 0

        possibleActions = gameState.getLegalActions(0)

        for action in possibleActions:
            currentState = gameState.generateSuccessor(0, action)
            currentValue = self.minValueV0(currentState, 1, depth)
            if currentValue > bestValue:
                bestValue = currentValue
                bestAction = action
        
        return bestAction


    def minValueV0(self, gameState, ghostIndex, depth):

        minValue = 100000
        possibleActions = gameState.getLegalActions(ghostIndex)

        # If the game is over the value should be returned.
        if (gameState.isLose() or gameState.isWin()):
            return self.evaluationFunction(gameState)

        # If this is the last ghost, it is pacMans turn
        if gameState.getNumAgents() - 1 == ghostIndex:
            for action in possibleActions:
                currentState = gameState.generateSuccessor(ghostIndex, action)
                currentValue = self.maxValueV0(currentState, depth)
                if minValue > currentValue:
                    minValue = currentValue
        
        # If it is not pacMans turn, it is the next ghost.
        else:
            for action in possibleActions:
                currentState = gameState.generateSuccessor(ghostIndex, action)
                currentValue = self.minValueV0(currentState, ghostIndex + 1, depth)
                if minValue > currentValue:
                    minValue = currentValue
        return minValue

    def maxValueV0(self, gameState, depth):

        depth = depth + 1
        maxValue = -100000
        actions = [action for action in gameState.getLegalActions(0)]

        if depth == self.depth or gameState.isLose() or gameState.isWin():
            return self.evaluationFunction(gameState)

        for action in actions:
            currentState = gameState.generateSuccessor(0, action)
            currentValue = self.minValueV0(currentState,1, depth)
            if maxValue < currentValue:
                maxValue = currentValue
        
        return maxValue
    
    
    # ****************************  Version 1 ****************************

    def getActionV1(self, gameState):
        return self.nextAction(gameState, 0, self.depth)[0]

	# Returns the next action and the minmax value. This will be used recursive.
    def nextAction(self, gameState, currentAgentIndex, depth):

		# Base case.
        if depth == 0 or gameState.isWin() or gameState.isLose():
			
			# Returns a list of the action with the lowest value, and the value.
            actions = [action for action in gameState.getLegalActions(currentAgentIndex)]
            action = gameState.getLegalActions(currentAgentIndex)
            action = actions[0]
            
            actionValues = []
            for action in actions:
                value = gameState.generateSuccessor(currentAgentIndex, action).getScore()
                actionValues.append([action, value])
    # 1. Dette er foerste gang selectAction kalles paa og det skjer med actions som en liste med lister, f.eks.: [[action1, value1], [action2, value2], [action3, value3]]
            return self.selectAction(currentAgentIndex, actions)
        
        nextAgent = (currentAgentIndex + 1) % (gameState.getNumAgents())

		# Recursion case. Have to find all actions avalible and get their values.
        actions = []
        for action in gameState.getLegalActions(currentAgentIndex):
            value = self.nextAction(gameState.generateSuccessor(currentAgentIndex, action), nextAgent, depth-1 if currentAgentIndex == gameState.getNumAgents()-2 else depth)
    # 4. Feilen forplanter seg videre slik at jeg ikke kan bruke value som naa skulle veart en liste med to elementer.
            actions.append([action, value])
    # 5. Av denne grunn vet jeg ikke om value faktisk er verdien, eller en action, eller bare None. Hvordan kan jeg passe paa at en [action, value] forblir en liste gjennom hele metoden?
		
		# Depending on whether the agent making this move is max or min, the action has to be returned along with its value.
		# The code assumes agentIndex=0 is max and the rest is min.
        return self.selectAction(currentAgentIndex, actions)

    # Helping method returning the min or max of a given action set.    
    def selectAction(self, agentIndex, actions):

        test = actions[0]

        if agentIndex:
            minAction = []
            for action in actions:
                if minAction ==[]:
                    minAction = action
                if action[1] < minAction[1]:
                    minAction = action
            return minAction[0], minAction[1]
        
        else:
            maxAction = []
            for action in actions:
                if maxAction == []:
                    maxAction.append(action[0])
                    maxAction.append(action[1])
                if action[1] > maxAction[1]:
    # 2. Her kan jeg se at det har faktisk kommet inn en liste med lister i. Jeg kan aksessere andre elementet i en de indre listene.
                    maxAction = action
    # 3. Men om jeg forsoeker aa bytte ut siste linje med linjen som staar under faar jeg feilmelding. Det gir for meg ingen mening. maxActions skal jo veare en liste med to elementer.
            # return [maxAction[0], maxAction[1]]
            return maxAction


    # ****************************  Version A ****************************

    def getActionA(self, gameState):

        # Initial values
        bestAction = ""
        bestValue = -99999.9
        depth = 0

        #Find the legal moves for pacman
        pacmanLegalActions = gameState.getLegalActions(0)

        #Loop through the actions
        for a in pacmanLegalActions:
            currentState = gameState.generateSuccessor(0,a)
            currentValue = self.min_valueA(currentState,depth,1)

            # Update the best value and action if the current value of the state we are looking at is better
            if currentValue > bestValue:
                bestValue = currentValue
                bestAction = a
        return bestAction

    """
            Min_value function
            This function calls itself recursively until it's pacmans turn to move again.
            Return the lowest value of its successors
    """
    def min_valueA(self, gameState, depth, ghost_index):

        # Inital values
        lowestValue = 99999.9
        ghostActions = gameState.getLegalActions(ghost_index)

        # If we are at a terminal/leaf node we want to return the static evaluation of the node using the given evaluation-function
        if (gameState.isLose() or gameState.isWin()):
            return self.evaluationFunction(gameState)

        #If we are at the last ghost, it's pacman's turn next
        if (ghost_index == gameState.getNumAgents()-1):
            for a in ghostActions:
                currentState = gameState.generateSuccessor(ghost_index,a)
                currentValue = self.max_valueA(currentState, depth)
                if currentValue < lowestValue:
                    lowestValue = currentValue

        # Else, we give the turn to the next ghost
        else:
            for a in ghostActions:
                currentState = gameState.generateSuccessor(ghost_index, a)
                currentValue = self.min_valueA(currentState,depth,ghost_index +1)
                if currentValue < lowestValue:
                    lowestValue = currentValue
        return lowestValue

    """
            Max_value function
            This function calls min_value in order to decide on the best current action
            Return the highest value of its successors
    """
    def max_valueA(self,gameState,depth):

        # We only update the depth when its pacmans turn
        depth = depth + 1

        # Initial value
        highestValue = -99999.9

        # generate the legal moves for pacman in this state
        pacmanActions = gameState.getLegalActions(0)

        # If we are at a terminal/leaf node we want to return the static evaluation of the node using the given evaluation-function
        if (depth == self.depth or gameState.isLose() or gameState.isWin()):
            return self.evaluationFunction(gameState)

        # Loop through the actions and generate states and values. We only update the best (highest) value the current is better.
        for a in pacmanActions:
            currentState = gameState.generateSuccessor(0, a)
            currentValue = self.min_valueA(currentState,depth,1)
            if currentValue > highestValue:
                highestValue = currentValue

        return highestValue

# ****************************  Change over ****************************

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
# ******************************  Change  ******************************
        if VERSION == 0:
            return self.getActionV0(gameState)
        elif VERSION == 1:
            return self.getActionV1(gameState)
        elif VERSION == 'A':
            return self.getActionA(gameState)

# ****************************  Version 0 ****************************

    def getActionV0(self, gameState):
        
        depth = 0
        alpha = -float('inf')
        beta = float('inf')

        return self.maxValueV0(gameState, alpha, beta, depth)

    def maxValueV0(self, gameState, alpha, beta, depth):

        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        value = -float('inf')
        choosenAction = None

        for action in gameState.getLegalActions(0):
            currentValue = self.minValueV0(gameState.generateSuccessor(0, action), alpha, beta, 1, depth)
            if value < currentValue:
                value = currentValue
                choosenAction = action
                
            if currentValue > beta:
                return value
            alpha = max(alpha, value)
        
        if depth == 0:
            return choosenAction
        return value


    def minValueV0(self, gameState, alpha, beta, ghostIndex, depth):

        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
        
        value = float('inf')
        nextAgentIndex = (ghostIndex + 1) % (gameState.getNumAgents())
        for action in gameState.getLegalActions(ghostIndex):
            if nextAgentIndex == 0:
                if depth + 1 == self.depth:
                    currentValue = self.evaluationFunction(gameState.generateSuccessor(ghostIndex, action))
                else:
                    currentValue = self.maxValueV0(gameState.generateSuccessor(ghostIndex, action), alpha, beta, depth + 1)
            else:
                currentValue = self.minValueV0(gameState.generateSuccessor(ghostIndex, action), alpha, beta, nextAgentIndex, depth)
            
            value = min(value, currentValue)

            if currentValue < alpha:
                return value

            beta = min(beta, value)
        
        return value


# ****************************  Version 1 ****************************

# ****************************  Version A ****************************

    def getActionA(self, gameState):

        depth = 0      # start at depth zero (root)
        a = -99999.9   #alpha value
        b = 99999.9    #beta value
        return self.max_valueA(gameState, depth, a, b)

    """
        Max_value function
        This function calls min_value in order to decide on the best current action
    """
    def max_valueA(self, gameState, depth, a, b):

        # If we are at a terminal/leaf node we want to return the static evaluation of the node using the given evaluation-function
        if (gameState.isLose() or gameState.isWin()):
            return self.evaluationFunction(gameState)

        # initial values
        highestValue = -99999.9
        bestAction = Directions.STOP

        # Generate the legal moves for pacman
        pacmanActions = gameState.getLegalActions(0)

        # Loop through all the actions
        for action in pacmanActions:
            # The next state after executing an action
            currentState = gameState.generateSuccessor(0, action)
            # The value of the state using the min_value function
            v = self.min_valueA(currentState, depth, 1, a, b)

            # If we find a better value for the state, we update it. We also update the best action, to return at depth = 0
            if v > highestValue:
                highestValue = v
                bestAction = action

            # Update the alpha value
            a = max(a, highestValue)
            # Check to see if we can prune
            if v > b:
                return highestValue

        # If we are on the top, we must return the action, if not, we must return the score in order to choose the best action.
        if depth == 0:
            return bestAction
        else:
            return highestValue


    """
            Min_value function
            This function calls itself recursively until it's pacmans turn to move again.
    """
    def min_valueA(self, gameState, depth,player, a, b):

        # If we are at a terminal/leaf node we want to return the static evaluation of the node using the given evaluation-function
        if (gameState.isLose() or gameState.isWin()):
            return self.evaluationFunction(gameState)

        # The index of the next agent
        nextPlayer = player +1

        # Check if we are at the end of the list of players, the next player is pacman.
        if player == gameState.getNumAgents() - 1:
            nextPlayer = 0 #pacman

        # Initial values
        lowestValue = 99999.9
        v = lowestValue

        # Generate the legal moves for the agent (ghost)
        actions = gameState.getLegalActions(player)

        # Loop through all the actions
        for action in actions:
            # If the next player is pacman, we return the static evaluation of the next node using the given evaluation-function
            if nextPlayer == 0:
                if depth == self.depth-1:
                    v = self.evaluationFunction(gameState.generateSuccessor(player, action))
                else:
                    # If we are not on the second last layer, we call max_value
                    v = self.max_valueA(gameState.generateSuccessor(player,action),depth +1,a,b)

            # If the next player is a ghost, we call min_value function
            else:
                v = self.min_valueA(gameState.generateSuccessor(player, action), depth, nextPlayer, a, b)

            # If we find a better value for the state, we update it.
            if v < lowestValue:
                lowestValue = v

            # Check to see if we can prune
            if v < a:
                return lowestValue
            # Update the beta value
            b = min(b, lowestValue)

        return lowestValue


# ****************************  Change over ****************************
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """


    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

