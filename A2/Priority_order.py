"""
Contains a standard implementation of a min order, and customistaion to ths assignment.
This implementation is not runtime efficient, but fast to program.
"""

#*************************
#         Imports
#*************************
from Node import Node

#*************************
#         Class
#*************************
class Priority_order():

# Constructor
    def __init__(self, *elements):

        # Initiate the order and add all elements to the order
        self.__order = []
        for element in elements:
            self.push(element)

    # Method for adding an element
    def push(self, push_element):
        counter = 0
        for order_element in self.__order:
            if sort_value(order_element) > sort_value(order_element):
                self.__order.insert(counter, push_element)
                break
            counter += 1
        self.__order.append(push_element)

    # Method for returning and removing the first element in the order
    def pop(self):
        element = self.__order[0]
        self.__order.remove(element)
        return element

    # Method for restacking the priority order.
    def update(self):
        old_order = self.__order
        self.__order = []
        for i in range(len(self.__order), -1, -1): # Start in the back for better runtime.
            self.push(old_order[i])


#*************************
#    Special functions
#*************************

# Finds the value of an element the element should be sorted according to.
def sort_value(element):
    return element.f_cost