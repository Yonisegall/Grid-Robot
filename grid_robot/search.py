# from search_node import search_node
# from grid_robot_state import grid_robot_state
# import heapq
#
#
# def create_open_set():
#     open = []
#     heapq.heapify(open)
#     return open
#
#
# def create_closed_set():
#     return []
#
#
# def add_to_open(vn, open_set):
#     heapq.heappush(open_set, (vn.h, vn))
#
#
# def open_not_empty(open_set):
#     if open_set:
#         return True
#     return False
#
#
# def get_best(open_set):
#     return heapq.heappop(open_set)[1]
#
#
# def add_to_closed(vn, closed_set):
#     closed_set.append(vn)
#
#
# def duplicate_in_open(vn, open_set):
#     for index, (_, state) in enumerate(open_set):
#         if state.state == vn.state:
#             if state.g > vn.g:
#                 del open_set[index]  # Remove the old state
#                 heapq.heapify(open_set)  # Re-heapify after modification
#                 return False
#             return True
#     return False
#
#
# def duplicate_in_closed(vn, closed_set):
#     for index, state in enumerate(closed_set):
#         if state.state == vn.state:
#             if state.g > vn.g:
#                 del closed_set[index]  # Remove the old state
#                 return False
#             return True
#     return False
#
#
# # helps to debug sometimes..
# def print_path(path):
#     for i in range(len(path) - 1):
#         print(f"[{path[i].state.get_state_str()}]", end=", ")
#     print(path[-1].state.state_str)
#
#
# def search(start_state, heuristic):
#     open_set = create_open_set()
#     closed_set = create_closed_set()
#     start_node = search_node(start_state, 0, heuristic(start_state))
#     add_to_open(start_node, open_set)
#
#     while open_not_empty(open_set):
#
#         current = get_best(open_set)
#
#         if grid_robot_state.is_goal_state(current.state):
#             path = []
#             while current:
#                 path.append(current)
#                 current = current.prev
#             path.reverse()
#             return path
#
#
#         add_to_closed(current, closed_set)
#
#         for neighbor, edge_cost in current.get_neighbors():
#             curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
#             if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
#                 add_to_open(curr_neighbor, open_set)
#
#     return None





#
#
# from search_node import search_node
# from grid_robot_state import grid_robot_state
# import heapq
#
# # Global dictionary for faster duplicate checks
# global_state_dict = {}
#
#
# def create_open_set():
#     open_set = []
#     heapq.heapify(open_set)
#     return open_set
#
#
# def create_closed_set():
#     return []
#
#
# def add_to_open(vn, open_set):
#     global global_state_dict
#     heapq.heappush(open_set, (vn.h, vn))
#     global_state_dict[vn.state] = vn  # Add the node to the global dictionary
#
#
# def open_not_empty(open_set):
#     return bool(open_set)
#
#
# def get_best(open_set):
#     global global_state_dict
#     best_node = heapq.heappop(open_set)[1]
#     del global_state_dict[best_node.state]  # Remove the node from the global dictionary
#     return best_node
#
#
# def add_to_closed(vn, closed_set):
#     closed_set.append(vn)
#     global_state_dict[vn.state] = vn  # Add to the global dictionary
#
#
# def duplicate_in_open(vn, open_set):
#     global global_state_dict
#     # Check directly in the global dictionary
#     if vn.state in global_state_dict:
#         existing_node = global_state_dict[vn.state]
#         if existing_node.g > vn.g:
#             # Replace the existing node in the heap and dictionary
#             open_set.remove((existing_node.h, existing_node))
#             heapq.heapify(open_set)  # Re-heapify after modification
#             global_state_dict[vn.state] = vn  # Update with the better node
#             return False
#         return True
#     return False
#
#
# def duplicate_in_closed(vn, closed_set):
#     global global_state_dict
#     # Check directly in the global dictionary
#     if vn.state in global_state_dict:
#         existing_node = global_state_dict[vn.state]
#         if existing_node.g > vn.g:
#             # Replace the existing node in the closed set and dictionary
#             closed_set.remove(existing_node)
#             global_state_dict[vn.state] = vn  # Update with the better node
#             return False
#         return True
#     return False
#
#
# def print_path(path):
#     for i in range(len(path) - 1):
#         print(f"[{path[i].state.get_state_str()}]", end=", ")
#     print(path[-1].state.state_str)
#
#
# def search(start_state, heuristic):
#     open_set = create_open_set()
#     closed_set = create_closed_set()
#     start_node = search_node(start_state, 0, heuristic(start_state))
#     add_to_open(start_node, open_set)
#
#     while open_not_empty(open_set):
#         current = get_best(open_set)
#
#         if grid_robot_state.is_goal_state(current.state):
#             path = []
#             while current:
#                 path.append(current)
#                 current = current.prev
#             path.reverse()
#             return path
#
#         add_to_closed(current, closed_set)
#
#         for neighbor, edge_cost in current.get_neighbors():
#             curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
#             if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
#                 add_to_open(curr_neighbor, open_set)
#
#     return None



























from search_node import search_node
from grid_robot_state import grid_robot_state
import heapq


# def create_open_set():
#     open = []
#     heapq.heapify(open)
#     return (open, {})  # Return tuple with heap and dictionary
#
#
# def create_closed_set():
#     return []
#
#
# def add_to_open(vn, open_set):
#     heapq.heappush(open_set[0], (vn.f, vn))
#     open_set[1][vn] = vn.f  # Store g-cost for lookups
#
#
# def open_not_empty(open_set):
#     return len(open_set[0]) != 0  # Return True if the heap is not empty
#
#
# def get_best(open_set):
#     # Get the best node (lowest heuristic cost)
#     key = heapq.heappop(open_set[0])
#     del open_set[1][key]  # Remove it from the dictionary as well
#     return key
#
#
# def add_to_closed(vn, closed_set):
#     closed_set.append(vn)
#
#
# def duplicate_in_open(vn, open_set):
#     if vn in open_set[1]:
#         existing_cost = open_set[1][vn]
#         if vn.g >= existing_cost:
#             return True
#     return False
#
#
# def duplicate_in_closed(vn, closed_set):
#     for index, state in enumerate(closed_set):
#         if state.state == vn.state:
#             if vn.g >= state.g:
#                 return True
#     return False
#
#
# # Helper function to debug and print the path
# def print_path(path):
#     for i in range(len(path) - 1):
#         print(f"[{path[i].state.get_state_str()}]", end=", ")
#     print(path[-1].state.get_state_str())
#
#
#
# def search(start_state, heuristic):
#     open_set = create_open_set()
#     closed_set = create_closed_set()
#     start_node = search_node(start_state, 0, heuristic(start_state))
#     add_to_open(start_node, open_set)
#
#     while open_not_empty(open_set):
#
#         current = get_best(open_set)
#
#         if grid_robot_state.is_goal_state(current.state):
#             path = []
#             while current:
#                 path.append(current)
#                 current = current.prev
#             path.reverse()
#             return path
#
#         #print(f'Current location : {current.state.get_location()} , cost  : {current.h}')
#
#
#         add_to_closed(current, closed_set)
#
#         for neighbor, edge_cost in current.get_neighbors():
#             curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
#             if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
#                 add_to_open(curr_neighbor, open_set)
#
#     return None



def create_open_set():
    open = []
    heapq.heapify(open)
    return open  # Return tuple with heap and dictionary


def create_closed_set():
    return []


def add_to_open(vn, open_set):
    heapq.heappush(open_set, (vn.f, vn))


def open_not_empty(open_set):
    return len(open_set[0]) != 0  # Return True if the heap is not empty


def get_best(open_set):
    val, key = heapq.heappop(open_set)
    return key


def add_to_closed(vn, closed_set):
    closed_set.append(vn)


def duplicate_in_open(vn, open_set):
    for item in open_set:
        val, key = item
        if key == vn:
            if val <= vn.f:
                return True
    return False

    # if vn in open_set[1]:
    #     existing_cost = open_set[1][vn]
    #     if vn.g >= existing_cost:
    #         return True
    # return False


def duplicate_in_closed(vn, closed_set):
    for index, state in enumerate(closed_set):
        if state.state == vn.state:
            if vn.g >= state.g:
                return True
    return False


# Helper function to debug and print the path
def print_path(path):
    for i in range(len(path) - 1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")
    print(path[-1].state.get_state_str())



def search(start_state, heuristic):
    open_set = create_open_set()
    closed_set = create_closed_set()
    start_node = search_node(start_state, 0, heuristic(start_state))
    add_to_open(start_node, open_set)

    while open_not_empty(open_set):

        current = get_best(open_set)
        if grid_robot_state.is_goal_state(current.state):
            path = []
            while current:
                path.append(current)
                current = current.prev
            path.reverse()
            return path

        #print(f'Current location : {current.state.get_location()} , cost  : {current.h}')


        add_to_closed(current, closed_set)

        for neighbor, edge_cost in current.get_neighbors():
            curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)

    return None


