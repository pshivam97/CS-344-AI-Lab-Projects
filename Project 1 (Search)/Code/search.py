# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    startState = problem.getStartState()
    explored_nodes = set()

    my_stack = util.Stack()
    my_stack.push((startState,[]))

    while not my_stack.isEmpty() :

        popped_out_node = my_stack.pop()
        coord_of_popped_out_node = popped_out_node[0]
        list_of_actions = popped_out_node[1]

        if problem.isGoalState(coord_of_popped_out_node) :
            return list_of_actions

        if coord_of_popped_out_node not in explored_nodes :
            explored_nodes.add(coord_of_popped_out_node) # At this step, we are marking the POPPED NODE as "VISITED or EXPLORED"

            for each_neighbour_coord,direction,stepCost in problem.getSuccessors(coord_of_popped_out_node) :
                if each_neighbour_coord not in explored_nodes :
                    my_stack.push((each_neighbour_coord, list_of_actions + [direction]))

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    startState = problem.getStartState()
    explored_nodes = set()

    my_queue = util.Queue()
    my_queue.push((startState,[]))

    while not my_queue.isEmpty() :

        popped_out_node = my_queue.pop()
        coord_of_popped_out_node = popped_out_node[0]
        list_of_actions = popped_out_node[1]

        if problem.isGoalState(coord_of_popped_out_node) :
            print list_of_actions
            return list_of_actions

        if coord_of_popped_out_node not in explored_nodes :
            explored_nodes.add(coord_of_popped_out_node)

            for each_neighbour_coord,direction,stepCost in problem.getSuccessors(coord_of_popped_out_node) :
                if each_neighbour_coord not in explored_nodes :
                    my_queue.push((each_neighbour_coord, list_of_actions + [direction]))

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    startState = problem.getStartState()
    explored_nodes = set()

    my_PriorityQueue = util.PriorityQueue()
    my_PriorityQueue.push((startState,[]),problem.getCostOfActions([]))

    while not my_PriorityQueue.isEmpty() :

        popped_out_node = my_PriorityQueue.pop()
        coord_of_popped_out_node = popped_out_node[0]
        list_of_actions = popped_out_node[1]

        if problem.isGoalState(coord_of_popped_out_node) :
            return list_of_actions

        if coord_of_popped_out_node not in explored_nodes :
            explored_nodes.add(coord_of_popped_out_node)

            for each_neighbour_coord,direction,stepCost in problem.getSuccessors(coord_of_popped_out_node) :
                if each_neighbour_coord not in explored_nodes :
                    my_PriorityQueue.push((each_neighbour_coord, list_of_actions + [direction]),problem.getCostOfActions(list_of_actions + [direction]))

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    startState = problem.getStartState()
    explored_nodes = set()

    my_PriorityQueue = util.PriorityQueue()
    my_PriorityQueue.push((startState,[]),problem.getCostOfActions([]) + heuristic(startState,problem))

    while not my_PriorityQueue.isEmpty() :

        popped_out_node = my_PriorityQueue.pop()
        coord_of_popped_out_node = popped_out_node[0]
        list_of_actions = popped_out_node[1]

        if problem.isGoalState(coord_of_popped_out_node) :
            return list_of_actions

        if coord_of_popped_out_node not in explored_nodes :
            explored_nodes.add(coord_of_popped_out_node)

            for each_neighbour_coord,direction,stepCost in problem.getSuccessors(coord_of_popped_out_node) :
                if each_neighbour_coord not in explored_nodes :
                    my_PriorityQueue.push((each_neighbour_coord, list_of_actions + [direction]),problem.getCostOfActions(list_of_actions + [direction]) + heuristic(each_neighbour_coord,problem))

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
