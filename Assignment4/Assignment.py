import copy
import itertools
import sys


class CSP:
    def __init__(self):
        # self.variables is a list of the variable names in the CSP
        self.variables = []

        # self.domains[i] is a list of legal values for variable i
        self.domains = {}

        # self.constraints[i][j] is a list of legal value pairs for
        # the variable pair (i, j)
        self.constraints = {}

        # Variable to keep track of how many times backtrack function is called
        self.called_backtrack = 0

        # Variable to keep track of how many times backtrack fails.
        self.backtrack_fail = 0

    def add_variable(self, name, domain):
        """Add a new variable to the CSP. 'name' is the variable name
        and 'domain' is a list of the legal values for the variable.
        """
        self.variables.append(name)
        self.domains[name] = list(domain)
        self.constraints[name] = {}

    def get_all_possible_pairs(self, a, b):
        """Get a list of all possible pairs (as tuples) of the values in
        the lists 'a' and 'b', where the first component comes from list
        'a' and the second component comes from list 'b'.
        """
        return itertools.product(a, b)

    def get_all_arcs(self):
        """Get a list of all arcs/constraints that have been defined in
        the CSP. The arcs/constraints are represented as tuples (i, j),
        indicating a constraint between variable 'i' and 'j'.
        """
        return [(i, j) for i in self.constraints for j in self.constraints[i]]

    def get_all_neighboring_arcs(self, var):
        """Get a list of all arcs/constraints going to/from variable
        'var'. The arcs/constraints are represented as in get_all_arcs().
        """
        return [(i, var) for i in self.constraints[var]]

    def add_constraint_one_way(self, i, j, filter_function):
        """Add a new constraint between variables 'i' and 'j'. The legal
        values are specified by supplying a function 'filter_function',
        that returns True for legal value pairs and False for illegal
        value pairs. This function only adds the constraint one way,
        from i -> j. You must ensure that the function also gets called
        to add the constraint the other way, j -> i, as all constraints
        are supposed to be two-way connections!
        """
        if not j in self.constraints[i]:
            # First, get a list of all possible pairs of values between variables i and j
            self.constraints[i][j] = self.get_all_possible_pairs(self.domains[i], self.domains[j])

        # Next, filter this list of value pairs through the function
        # 'filter_function', so that only the legal value pairs remain
        self.constraints[i][j] = filter(lambda value_pair: filter_function(*value_pair), self.constraints[i][j])

    def add_all_different_constraint(self, variables):
        """Add an Alldiff constraint between all of the variables in the
        list 'variables'.
        """
        for (i, j) in self.get_all_possible_pairs(variables, variables):
            if i != j:
                self.add_constraint_one_way(i, j, lambda x, y: x != y)

    def backtracking_search(self):
        """This functions starts the CSP solver and returns the found
        solution.
        """
        # Make a so-called "deep copy" of the dictionary containing the
        # domains of the CSP variables. The deep copy is required to
        # ensure that any changes made to 'assignment' does not have any
        # side effects elsewhere.
        assignment = copy.deepcopy(self.domains)

        # Run AC-3 on all constraints in the CSP, to weed out all of the
        # values that are not arc-consistent to begin with
        self.inference(assignment, self.get_all_arcs())

        # Call backtrack with the partial assignment 'assignment'
        return self.backtrack(assignment)

    def backtrack(self, assignment):
        """The function 'Backtrack' from the pseudocode in the
        textbook.

        The function is called recursively, with a partial assignment of
        values 'assignment'. 'assignment' is a dictionary that contains
        a list of all legal values for the variables that have *not* yet
        been decided, and a list of only a single value for the
        variables that *have* been decided.

        When all of the variables in 'assignment' have lists of length
        one, i.e. when all variables have been assigned a value, the
        function should return 'assignment'. Otherwise, the search
        should continue. When the function 'inference' is called to run
        the AC-3 algorithm, the lists of legal values in 'assignment'
        should get reduced as AC-3 discovers illegal values.

        IMPORTANT: For every iteration of the for-loop in the
        pseudocode, you need to make a deep copy of 'assignment' into a
        new variable before changing it. Every iteration of the for-loop
        should have a clean slate and not see any traces of the old
        assignments and inferences that took place in previous
        iterations of the loop.
        """
        # TODO: IMPLEMENT THIS
        # ******************************  Change  ******************************

        # Every time backtrack is called it should be recorded.
        self.called_backtrack += 1

        # If the assignment has only one value in the domain of each variable, the result should be returned.
        if self.assignment_complete(assignment):
            return assignment
        
        # Uses a variable that has more than one value in its domain.
        var = self.select_unassigned_variable(assignment)

        # Every value in the variables domain is tested out. This is equivalent to making a guess and see if it can work.
        # No reason to order the domain values in any particular order.
        for value in assignment[var]:
            # In order to see if the guess is right without chaning the starting point, a copy is made.
            assignment_copy = copy.deepcopy(assignment)

            # The chosen value is used as a guess in the copy.
            if value in assignment_copy[var]:
                assignment_copy[var] = [value]

                # The assignment containg the guess is then checked for all constraints.
                inferences = self.inference(assignment_copy, self.get_all_neighboring_arcs(var))

                # If the guess holds for all constraints, backtrack is recursively called, to guess on new values wihtin the same guess.
                if inferences:
                    result = self.backtrack(assignment_copy)
                    # Base case, returns solution to the initial call.
                    if result:
                        return result
        
        # Tracks the amount of times back track fails. This signifies how many wrong guesses was made to find the solution.
        self.backtrack_fail += 1
        return False

    # Checks if every value has only one value in its domain.
    def assignment_complete(self, assignment):

        for variable in assignment:
            if len(assignment[variable]) != 1:
                return False
        return True


        # ****************************  Change over ****************************

    def select_unassigned_variable(self, assignment):
        """The function 'Select-Unassigned-Variable' from the pseudocode
        in the textbook. Should return the name of one of the variables
        in 'assignment' that have not yet been decided, i.e. whose list
        of legal values has a length greater than one.
        """
        # TODO: IMPLEMENT THIS
        # ******************************  Change  ******************************

        # Returns a variable that has more than one value in its domain, meaning that it is not decided on yet.
        for variable in assignment:
            if len(assignment[variable]) > 1:
                return variable

        # ****************************  Change over ****************************

    def inference(self, assignment, queue):
        """The function 'AC-3' from the pseudocode in the textbook.
        'assignment' is the current partial assignment, that contains
        the lists of legal values for each undecided variable. 'queue'
        is the initial queue of arcs that should be visited.
        """
        # TODO: IMPLEMENT THIS
        # ******************************  Change  ******************************

        # Goes through all constraints it is given.
        while queue:
            (xi, xj) = queue.pop()

            # Checks if the whole domain holds for constraints. If it does not, all affected variables are added to the queue,
            # so they are checked again to make shure they are consistent.
            if self.revise(assignment, xi, xj):
                if len(assignment[xi]) == 0:
                    return False
                for neighbor_arc in self.get_all_neighboring_arcs(xi):
                    if neighbor_arc[0] != xj:
                        queue.append(neighbor_arc)
        # Returns true if the assignment is consistent and has at least one value in every domain.
        return True

        # ****************************  Change over ****************************

    def revise(self, assignment, i, j):
        """The function 'Revise' from the pseudocode in the textbook.
        'assignment' is the current partial assignment, that contains
        the lists of legal values for each undecided variable. 'i' and
        'j' specifies the arc that should be visited. If a value is
        found in variable i's domain that doesn't satisfy the constraint
        between i and j, the value should be deleted from i's list of
        legal values in 'assignment'.
        """
        # TODO: IMPLEMENT THIS
        # ******************************  Change  ******************************

        revised = False

        for x in assignment[i]:

            # The goal is to find out if the x value is valid, and this is keept track of by this boolean.
            x_valid = False

            for y in assignment[j]:

                # Loop through all constraints to see if any y value can give the x value in question.
                for constraint in self.constraints[i][j]:
                    if constraint[1] ==  y and constraint[0] == x:

                        # If a constraint allowing current x value is found, this should update x_valid.
                        x_valid = True
                        break
            
            # If x is found not to be valid the value should be removed from the list and the method should return True.
            if not x_valid:
                assignment[i].remove(x)
                revised = True
                break

        return revised
        

        # ****************************  Change over ****************************



def create_map_coloring_csp():
    """Instantiate a CSP representing the map coloring problem from the
    textbook. This can be useful for testing your CSP solver as you
    develop your code.
    """
    csp = CSP()
    states = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
    edges = {'SA': ['WA', 'NT', 'Q', 'NSW', 'V'], 'NT': ['WA', 'Q'], 'NSW': ['Q', 'V']}
    colors = ['red', 'green', 'blue']
    for state in states:
        csp.add_variable(state, colors)
    for state, other_states in edges.items():
        for other_state in other_states:
            csp.add_constraint_one_way(state, other_state, lambda i, j: i != j)
            csp.add_constraint_one_way(other_state, state, lambda i, j: i != j)

    for constraint in csp.constraints:
        for entry in csp.constraints[constraint]:
            csp.constraints[constraint][entry] = list(csp.constraints[constraint][entry])
    return csp


def create_sudoku_csp(filename):
    """Instantiate a CSP representing the Sudoku board found in the text
    file named 'filename' in the current directory.
    """
    csp = CSP()
    board = list(map(lambda x: x.strip(), open(filename, 'r')))

    for row in range(9):
        for col in range(9):
            if board[row][col] == '0':
                csp.add_variable('%d-%d' % (row, col), list(map(str, range(1, 10))))
            else:
                csp.add_variable('%d-%d' % (row, col), [board[row][col]])

    for row in range(9):
        csp.add_all_different_constraint(['%d-%d' % (row, col) for col in range(9)])
    for col in range(9):
        csp.add_all_different_constraint(['%d-%d' % (row, col) for row in range(9)])
    for box_row in range(3):
        for box_col in range(3):
            cells = []
            for row in range(box_row * 3, (box_row + 1) * 3):
                for col in range(box_col * 3, (box_col + 1) * 3):
                    cells.append('%d-%d' % (row, col))
            csp.add_all_different_constraint(cells)

    for constraint in csp.constraints:
        for entry in csp.constraints[constraint]:
            csp.constraints[constraint][entry] = list(csp.constraints[constraint][entry])
    return csp


def print_sudoku_solution(solution):
    """Convert the representation of a Sudoku solution as returned from
    the method CSP.backtracking_search(), into a human readable
    representation.
    """
    for row in range(9):
        for col in range(9):
            print(solution['%d-%d' % (row, col)][0], end=" "),
            if col == 2 or col == 5:
                print('|', end=" "),
        print("")
        if row == 2 or row == 5:
            print('------+-------+------')

# ******************************  Change  ******************************


def solve_print_sudoku(filename):
    sudoku = create_sudoku_csp(filename)
    solution = sudoku.backtracking_search()

    print('\n\nThe following is the result of the program solving: ', filename)
    print('The backtrack method was called ', sudoku.called_backtrack, ' times\n')
    print('The backtrack method failed ', sudoku.backtrack_fail, ' times.\n')

    print_sudoku_solution(solution)



if __name__ == '__main__':


    sys.stdout = open('output.txt', 'w')

    solve_print_sudoku('easy.txt')
    solve_print_sudoku('medium.txt')
    solve_print_sudoku('hard.txt')
    solve_print_sudoku('veryhard.txt')
    solve_print_sudoku('worldshardest.txt')



# ****************************  Change over ****************************