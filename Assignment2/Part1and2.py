"""
First task is to find the shortes way in Samfundet_map_1.csv.
To do this I need to use the A* algorithm that is implemented in AStar.py. The following functions has to be implemnted to do so:

AStar takes the following input:
start_state:                        The state of the first node.
func_heuristic(state):              Function for estimating the remainding cost for a path from the given state to the goal.
func_adjacent_states(state):         Function for generating the successing nodes for a given state.
func_goal_evaluate(state):          Function returns True if the state is the goal, else False.
func_cost(state, next_state):       Function returning the cost of going from one state to another. Set to 1 by default.
"""

#*************************
#       Imports
#*************************
from Map import Map_Obj
from AStar import AStar, Node


#*************************
#       Functions
#*************************

# A heuristic function
def walking_distance(state):
    x_current, y_current = state[1], state[2]
    x_goal, y_goal = state[0].get_goal_pos()[0], state[0].get_goal_pos()[1]
    return abs(x_current - x_goal) + abs(y_current - y_goal)

# Returns all nodes adjacent to the given node.
def generate_adjacent_states_dagonal(state):
    states = []
    for x,y in [(state[1] + i, state[2] + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]:
        
        # Should not return the states that are impassable.
        if state[0].get_cell_value([x, y]) != -1:
            states.append((state[0], x, y)) # The state has to be given as a tuple, because A* uses the states as keys in a dictionary.
    return states

# Return only horisontal and verticaly adjacent nodes, not diagonal adjacent once. Terrible function, but was tired...
def generate_adjacent_states(state):
    states = []
    states.append((state[0], state[1] - 1, state[2]))
    states.append((state[0], state[1] + 1, state[2]))
    states.append((state[0], state[1], state[2] - 1))
    states.append((state[0], state[1], state[2] + 1))
    ret_states = []
    for new_state in states:
        if state[0].get_cell_value([new_state[1], new_state[2]]) != -1:
            ret_states.append(new_state)
    return ret_states

# Checks if the given node is the goal.
def goal_evaluate(state):
    if [state[1], state[2]] == state[0].get_goal_pos():
        return True

# Returns the cost of moving to a position. Only works when moving one step.
def find_cost(state, next_state):
    for adjacent_state in generate_adjacent_states(state):
        if adjacent_state == next_state:
            return next_state[0].get_cell_value([next_state[1], next_state[2]])
    print('Can find cost. The nodes are not adjacent.')

def visualise_path_map(state_map, path):
    for position in path[1: len(path)]:
        state_map.replace_map_values(position, 5, state_map.get_goal_pos())
    state_map.show_map()

#*************************
#          Main
#*************************

# Main for part 1
def main():

    # Task 1
    map = Map_Obj(1)
    start_state = (map, map.get_start_pos()[0], map.get_start_pos()[1])
    a_star = AStar(start_state, walking_distance, generate_adjacent_states, goal_evaluate)
    node_path = a_star.run()
    
    pos_path = []
    for node in node_path:
        pos_path.append([node.state[1], node.state[2]])
    print('Positions in the path of task 1:')
    print(pos_path)

    visualise_path_map(map, pos_path)

    # Task 2
    map = Map_Obj(2)
    start_state = (map, map.get_start_pos()[0], map.get_start_pos()[1])
    a_star = AStar(start_state, walking_distance, generate_adjacent_states, goal_evaluate)
    node_path = a_star.run()
    
    pos_path = []
    for node in node_path:
        pos_path.append([node.state[1], node.state[2]])
    print('Positions in the path of task 2:')
    print(pos_path)

    visualise_path_map(map, pos_path)

# Main for Part 2
def main2():

    # Task 3

    map = Map_Obj(3)
    start_state = (map, map.get_start_pos()[0], map.get_start_pos()[1])
    a_star = AStar(start_state, walking_distance, generate_adjacent_states, goal_evaluate, find_cost)
    node_path = a_star.run()
    
    pos_path = []
    for node in node_path:
        pos_path.append([node.state[1], node.state[2]])
    print('Positions in the path of task 3:')
    print(pos_path)

    visualise_path_map(map, pos_path)

    # Task 4

    map = Map_Obj(4)
    start_state = (map, map.get_start_pos()[0], map.get_start_pos()[1])
    a_star = AStar(start_state, walking_distance, generate_adjacent_states, goal_evaluate, find_cost)
    node_path = a_star.run()
    
    pos_path = []
    for node in node_path:
        pos_path.append([node.state[1], node.state[2]])
    print('Positions in the path of task 3:')
    print(pos_path)

    visualise_path_map(map, pos_path)

if __name__ == "__main__":
    main()
    main2()