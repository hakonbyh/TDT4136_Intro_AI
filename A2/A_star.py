"""
Contains the standard A* algorithm and the specializations needed for this case.
"""
#*************************
#         Imports
#*************************
from Node import Node
from Priority_order import Priority_order

#*************************
#         Class
#*************************
class A_star():

# Constructor
    def __init__(self, start_state):
        
        # Make the open nodes as a min priority order
        self.open = self.intitate_priority_order(start_state)

        # The closed once does not need a specific order.
        self.closed = []

# Methods
    # Method for running the algoritm.
    def run(self):

        # Loop to be executed until all nodes are explored or a solution is found.
        while True:
            current_node = self.open.pop()
            self.closed.append(current_node)

            # Create all the leaf nodes and add them to the open order.
            leaf_nodes = create_leaf_nodes(current_node)
            self.open.push(leaf_nodes)

            break






#*************************
#   Special functions
#*************************

# Initiates the min priority order with the first node.
def initiate_priority_order(Node: node):
    return Priority_order(node)

# Creates all nodes that can be reached directly from the given state.
def create_leaf_nodes(Node: node):
    pass
