"""
Contains the standard A* algorithm implementation.

AStar takes the following input:
start_state:                        The state of the first node.
func_heuristic(state):              Function for estimating the remainding cost for a path from the given state to the goal.
func_successor_generator(state):    Function for generating the successing nodes for a given state.
func_goal_evaluate(state):          Function returns True if the state is the goal, else False.
"""

#*************************
#    Imports
#*************************
from MinPriorityOrder import MinPriorityOrder


#*************************
#    Class for nodes
#*************************
class Node():

# Constructor
    def __init__(self, state, g_cost, h_cost, f_cost=None, parent=None, List: successors=None):

        self.state = state
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.parent = parents
        self.successors = successors if successors else []


#*************************
# A* algorithm as a class
#*************************

# Method for running the algoritm.
class AStar():

# Constructor to take in all functions and states.
    def __init__(self, start_state, func_heuristic, func_successor_generator, func_goal_evaluate):

        # Functions to be saved and used during the algorithm.
        self.func_heuristic = func_heuristic
        self.func_successor_generator = func_successor_generator
        self.func_goal_evaluate = func_goal_evaluate

        # Make the open nodes as a min priority order
        open = initiate_priority_order(start_state)

        # The closed once does not need a specific order.
        closed = []

        # Map every state to its corresponding node. This gives a overview of what nodes exists.
        state_node_map = {}

    # Method for runing the actual algorithm
    def run():

        # Loop to be executed until all nodes are explored or a solution is found.
        while self.open.size():

            # Takes the first node in open, and puts it in close.
            current_node = self.open.pop()
            self.closed.append(current_node)

            # If this node is the answer, it should return all the parents as well as it self.
            if self.func_goal_evaluate(current_node.state):
                print("Path found!")
                return [node.state[1:] for node in find_path(current_node)]

            # Make a list of all successor nodes, and loop throgh them.
            new_adjacent_nodes = self.func_successor_generator(current_node.state)
            for new_adjacent_node in new_adjacent_nodes:
                self.open.push(new_adjacent_node)
            
            # All adjacent nodes that are not new needs to get their cost reviewed.
            adjacent_nodes = 
            for old_node in
        
        # If no solution was found this is printed.
        print("No solution was found.")


# Helping methods

    # Initiates the min priority order with the first node.
    def initiate_priority_order(self, start_state):
        return MinPriorityOrder(Node(state=start_state, g_cost=0, h_cost=self.func_heuristic(start_state)))

    # Return the desired outcome from the A* algorithm.
    def find_path(Node: node):
        if node.parent == None: # Base case
            return [node]
        return a_star_return(node) + [node] # Recurevly calls on it self.


    # Checks if node exists in open or closed.
    def node_exists(self, node):

    #*************************
    #         Trash
    #*************************


    # Creates all nodes that can be reached directly from the given state.
    def create_new_adjacent_nodes(Priority_order: open_nodes, List: closed_nodes, Node: node):
        new_node_states = []
        for x,y in [(state[1] + i, state[2] + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]:

            # If a position has the value of -1 it is not possible to go there and should hence not be a node.
            if state[0].get_cell_value([x, y]) == -1:
                continue

            # Add the state first, and if it is later discovered to exist, it will be removed again.
            new_node_states.append([node.get_state[0], x, y])
            
            # If the node is found to allready exist, then the sate is removed from the list.
            for old_node in closed_nodes:
                if old_node.state == [node.get_state()[0], x ,y]:
                    new_node_states.remove([node.get_state()[0], x ,y])
            for old_node in open_nodes:
                if old_node.state == [node.get_state()[0], x, y]:
                    new_node_states.remove([node.get_state()[0], x ,y])

            # If

        # All states than remain should be made into new nodes.
        new_nodes = []
        for state in new_node_states:
            new_nodes.append(Node(state, node.g_cost + ))

        return new_nodes

    # Returns all adjacent nodes that are not new.
    def find_adjacent_nodes(Priority_order: open_nodes, List: closed_nodes, Node: node):
        adjacent_nodes = []
        state = node.get_state()
        for x,y in [(state[1] + i, state[2] + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]:

            # If a position has the value of -1 it is not possible to go there and should hence not be a node.
            if state[0].get_cell_value([x, y]) == -1:
                continue
            
            # Every adjacent node should be added.
            for adjacent_node in closed_nodes:
                if adjacent_node.state == [node.get_state()[0], x ,y]:
                    adjacent_nodes.append(adjacent_node)
            for adjacent_node in open_nodes:
                if adjacent_node.state == [node.get_state()[0], x, y]:
                    adjacent_nodes.append(adjacent_node)
        
        return adjacent_nodes
