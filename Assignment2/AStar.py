"""
Contains the standard A* algorithm implementation.

AStar takes the following input:
start_state:                        The state of the first node.
func_heuristic(state):              Function for estimating the remainding cost for a path from the given state to the goal.
func_adjacent_states(state):         Function for generating the successing nodes for a given state.
func_goal_evaluate(state):          Function returns True if the state is the goal, else False.
func_cost(state, next_state):       Function returning the cost of going from one state to another. Set to 1 by default.

Behavour:
Only run() should be called. It returns a path of nodes.
"""
#*************************
# Global static variables
#*************************
verbose = False  # Should be used during debugging.

#*************************
#        Imports
#*************************
from MinPriorityOrder import MinPriorityOrder


#*************************
#    Class for nodes
#*************************
class Node():

# Constructor
    def __init__(self, state, g_cost=None, h_cost=None, f_cost=None, parent=None, successors=None):

        self.state = state
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = f_cost
        self.parent = parent
        self.successors = successors if successors else []


#*************************
# A* algorithm as a class
#*************************

# Method for running the algoritm.
class AStar():

# Constructor to take in all functions and states.
    def __init__(self, start_state, func_heuristic, func_adjacent_states, func_goal_evaluate, func_cost=lambda x, y: 1):

        # Functions to be saved and used during the algorithm.
        self.func_heuristic = func_heuristic
        self.func_adjacent_states = func_adjacent_states
        self.func_goal_evaluate = func_goal_evaluate
        self.func_cost = func_cost

        # Make the open nodes as a min priority order
        self.open = self.initiate_priority_order(start_state)

        # The closed once does not need a specific order.
        self.closed = []

        # Map every state to its corresponding node. This gives a overview of what nodes exists.
        self.state_node_map = {}

    # Method for runing the actual algorithm
    def run(self):

        # Loop to be executed until all nodes are explored or a solution is found.
        while self.open.size():

            # Takes the first node in open, and puts it in close.
            current_node = self.open.pop()
            if verbose: print('pop id: ', current_node.state)
            self.closed.append(current_node)

            # If this node is the answer, it should return all the parents as well as it self.
            if self.func_goal_evaluate(current_node.state):
                print("Path found!")
                return  self.find_path(current_node)

            # Make a list of all possible successor states, make them into nodes, and loop through them.
            adjacent_states = self.func_adjacent_states(current_node.state)
            adjacent_nodes = self.create_nodes(adjacent_states)

            for adjacent_node in adjacent_nodes:

                # If a node with the same state has been made before we should use the old one.
                if adjacent_node.state in self.state_node_map.keys():
                    adjacent_node = self.state_node_map[adjacent_node.state]
                
                # Add the adjacent node to the current nodes successors.
                current_node.successors.append(adjacent_node)

                # If the node is new it needs to get its costs and parent initiated. In addition it should be added to the mapping.
                if adjacent_node.state not in self.state_node_map.keys():
                    self.attach_and_eval(adjacent_node, current_node)
                    if verbose: print('push id:', adjacent_node.state)
                    self.open.push(adjacent_node)
                    self.state_node_map[adjacent_node.state] = adjacent_node
                
                # If the adjacent node existed before current node was expanded from, and the path to the adjacent node will be shorter
                # through the current node, adjacent node should be updated with new parent and costs.
                elif (current_node.g_cost + self.func_cost(current_node.state, adjacent_node.state)) < adjacent_node.g_cost:
                    self.attach_and_eval(adjacent_node, current_node)

                    # If the node has children, the children should also be updated.
                    if adjacent_node in self.closed:
                        self.propagate_path_improvements(adjacent_node)

        # If no solution was found this is printed.
        print("No solution was found.")
        if verbose:
            for node in self.closed:
                print(node.state)
            print(' The following paths were found:')
            for node in self.closed:
                #print(self.find_path(node))
                pass
        return 


# Helping methods

    # Initiates the min priority order with the first node.
    def initiate_priority_order(self, start_state):
        if verbose: print('initiate with start state:', start_state)
        return MinPriorityOrder(lambda node: node.f_cost, Node(state=start_state, g_cost=0, h_cost=self.func_heuristic(start_state)))

    # Return the desired outcome from the A* algorithm.
    def find_path(self, node):
        if node.parent is None: # Base case
            return [node]
        return self.find_path(node.parent) + [node] # Recurevly calls on it self.

    # Creates nodes for all states supplied.
    def create_nodes(self, states):
        new_nodes = []
        for state in states:
            new_nodes.append(Node(state))
        return new_nodes

    # Method for setting costs and paret for a new node.
    def attach_and_eval(self, node, parent):
        node.parent = parent
        node.g_cost = parent.g_cost + self.func_cost(node.state, parent.state)
        node.h_cost = self.func_heuristic(node.state)
        node.f_cost = node.g_cost + node.h_cost

    # Mehtod for updating path of successors after its parent got its cost updated.
    def propagate_path_improvements(self, parent_node):
        for successor in parent_node.successors:
            if successor.g_cost > (parent_node.g_cost + self.func_cost(parent_node.state, successor.state)):
                self.attach_and_eval(successor, parent_node)
                self.propagate_path_improvements(successor)



#*************************
#         Test
#*************************
    
# Heuristic funcion.
def level(id):
    if id == 1:
        return 4
    if id in range(2, 5):
        return 3
    if id in range(5, 8):
        return 2
    if id in range(8, 12):
        return 1
    else:
        return 0

# The graph cosists of five levels, giving the heuristic function. Only one node at the bottom, and this is the target.
# The dictionaly denotes the adjacent nodes
def func_test():
    dic_graph = {}
    dic_graph[1] = [2, 3, 4]
    dic_graph[2] = [1, 5]
    dic_graph[3] = [1, 5]
    dic_graph[4] = [1, 6, 7]
    dic_graph[5] = [2, 3, 8, 9]
    dic_graph[6] = [4, 9, 10]
    dic_graph[7] = [4, 10, 11]
    dic_graph[8] = [5]
    dic_graph[9] = [5, 6]
    dic_graph[10] = [6, 7]
    dic_graph[11] = [12]
    dic_graph[12] = [11]

    a_star = AStar(1, level, lambda x: dic_graph[x], lambda x: True if x == 12 else False )
    node_path = a_star.run()
    
    print('Expect: 1, 4, 7, 11, 12')

    id_path = []
    for node in node_path:
        id_path.append(node.state)
    print('Got:', id_path)

if __name__ == "__main__":
    func_test()