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



class Node:
    def __init__(self, coord, directionsList, cost):
        self.coord = coord
        self.directionsList = directionsList
        self.cost = cost


def baseSearch(problem, method, heuristic=None):

    # method 0 = DFS
    # method 1 = BFS
    # method 2 = UCS
    # method 3 = A*

    if method == 0:
        nodeStorage = util.Stack()
    elif method == 1:
        nodeStorage = util.Queue()
    elif method == 2 or 3:
        nodeStorage = util.PriorityQueue()

    closedSet = set()
    closedSet.add(problem.getStartState())

    # add start's successors to nodeStorage
    for s in problem.getSuccessors(problem.getStartState()):
        if method == 3:
            nodeStorage.push(Node(s[0], [s[1]], s[2]), s[2] + heuristic(s[0], problem))
        elif method == 2:
            nodeStorage.push(Node(s[0], [s[1]], s[2]), s[2])
        else:
            nodeStorage.push(Node(s[0], [s[1]], s[2]))

    # loop of search
    while not nodeStorage.isEmpty():
        temp = nodeStorage.pop()
        if problem.isGoalState(temp.coord):
            return temp.directionsList
        if temp.coord not in closedSet:
            closedSet.add(temp.coord)
            for s in problem.getSuccessors(temp.coord):
                newNode = Node(s[0], temp.directionsList + [s[1]], temp.cost + s[2])
                if method == 2:
                    nodeStorage.push(newNode, temp.cost + s[2])
                elif method == 3:
                    nodeStorage.push(newNode, temp.cost + s[2] + heuristic(s[0], problem))
                else:
                    nodeStorage.push(newNode)
    return []

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
    
    return baseSearch(problem, 0)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    return baseSearch(problem, 1)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    return baseSearch(problem, 2)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    return baseSearch(problem, 3, heuristic)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch