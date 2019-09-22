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
# Global static variables
#*************************
verbose = False  # Should be used during debugging.

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
        if verbose: print('push was used and gave this que:')
        if verbose: self.print_order()
        if verbose: print('--')
        return True

    # Method for returning and removing the first element in the order
    def pop(self):
        try:
            if verbose: print('Pop tried on following que:') 
            if verbose: self.print_order()
            element = self.__order[0]
            if verbose: print('Found element:', self.meth_sorting_value(element))
            self.__order.remove(element)
            if verbose: print('Removed element:')
            if verbose: self.print_order()
            if verbose: print('--')
            return element
        except IndexError as ie:
            if verbose: print('Size of que:', self.size())
            print('pop gave a IndexError')
            print(ie)


    # Method for restacking the priority order.
    def update(self):
        old_order = self.__order
        self.__order = []
        for i in range(len(old_order), 0, -1): # Start in the back for better runtime.
            self.push(old_order[i])

    # Method for returning amount of elements in order
    def size(self):
        return len(self.__order)

    # Prints the internal state of the order.
    def print_order(self):
        order = []
        for element in self.__order:
            order.append(self.meth_sorting_value(element))
        print(order)



#*************************
#         Test
#*************************
import random

class Node():
    def __init__(self, state, f_cost=None):
        self.state = state
        self.f_cost = f_cost

def func_test():
    nodes = []
    for i in range(10):
        nodes.append(Node(i, random.randrange(0,25)))
    order = MinPriorityOrder(lambda x: x.f_cost, nodes[0])
    
    for node in nodes[1:10]:
        order.print_order()
        order.push(node)
    order.print_order()
    
    poped = order.pop()

    print('New order:')
    order.print_order()

    poped = order.pop()

    print('New order:')
    order.print_order()

if __name__ == "__main__":
    func_test()
    