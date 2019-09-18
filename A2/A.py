"""
A* is the algoritm required to use in assignment 2.

Made to work on nodes denoted by a position in a map of NxM size.
The id of the position is found by counting each position in the grid in the 
following way:
1  2  3  4  5
6  7  8  9  10
11 12 13 14 15
"""


# This class will contian the A* algorithm.
class A():

# Constructor.
    def __init__(self):
        
        # Initializes closed and open lists
        open, closed = [],


# Method for calculating heudonistic
    def heu(self, position, goal):
        return
    


class Position(xCoordinate, yCoordinate, id):

    def __init__(self, id):

        # The id and posotion should not be able to change later
        self.__id = id
        self.__x = xCoordinate
        self.__y = yCoordinate

        # Every position must have a current minimum cost.
        self.cost

    def heu