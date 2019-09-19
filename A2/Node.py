"""
A* is the algoritm required to use in assignment 2.

Made to work on nodes denoted by a position in a map of NxM size.
"""
    


class Node():

    def __init__(self, state, g_cost=None, h_cost=None, f_cost=None, parent=None, successors=None,): 
        # State is the following tupple [Map_Obj, x, y]

        # Save the map and positions. They shal not be changed.
        self.__x = state[1]
        self.__y = state[2]

        # Every node needs current cost (g), estimated remaining cost (h), and full cost (f).
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = f_cost

        # For keeping track of the optimal route.
        self.parent = parent
        self.successors = successors if successors else []