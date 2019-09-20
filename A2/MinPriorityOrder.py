"""
Contains a standard implementation of a min order.
This implementation is not runtime efficient, but fast to program.

Input:
meth_soring_value:      Method invoked on elements to be sorted, returning the value they should be sorted by.

Behaviour:
push(element):          Pushes an element in the order in the right placement
pop():                  Returns the first element in the order and deletes it internally.
update():               Reorders the order.
size():                 Returns the amount of elements in the order.
"""

#*************************
#         Class
#*************************
class MinPriorityOrder():

# Constructor
    def __init__(self, meth_sorting_value, *elements):

        self.meth_sorting_value = meth_sorting_value

        # Initiate the order and add all elements to the order
        self.__order = []
        for element in elements:
            self.push(element)

    # Method for adding an element
    def push(self, push_element):
        counter = 0
        for order_element in self.__order:
            if self.meth_sorting_value(order_element) > self.meth_sorting_value(push_element):
                self.__order.insert(counter, push_element)
                return True
            counter += 1
        self.__order.append(push_element)
        return True

    # Method for returning and removing the first element in the order
    def pop(self):
        element = self.__order[0]
        self.__order.remove(element)
        return element

    # Method for restacking the priority order.
    def update(self):
        old_order = self.__order
        self.__order = []
        for i in range(len(old_order), 0, -1): # Start in the back for better runtime.
            self.push(old_order[i])

    # Method for returning amount of elements in order
    def size(self):
        return len(self.__order) + 1
