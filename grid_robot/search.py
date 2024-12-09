# from search_node import search_node
# from grid_robot_state import grid_robot_state
# import heapq
#
#
# # --------------------- The faster ---------------------
#
# def create_open_set():  # Try with HashMap
#     open_new = []
#     heapq.heapify(open_new)
#     return open_new, {}  # Return tuple with heap and dictionary
#
#
# def create_closed_set():
#     return {}
#
#
# def add_to_open(vn, open_set):
#     heapq.heappush(open_set[0], (vn.f, vn))
#     open_set[1][vn.unique] = vn.g
#
#
# def open_not_empty(open_set):
#     return len(open_set[0]) != 0  # Return True if the heap is not empty
#
#
# def get_best(open_set):
#     while open_not_empty(open_set):
#         val, key = heapq.heappop(open_set[0])
#         key_str = key.unique
#
#         if key_str in open_set[1]:
#             del open_set[1][key_str]
#             return key
#     return None
#
#
# def add_to_closed(vn, closed_set):
#     closed_set[vn.state.unique] = vn.f
#
#
# def duplicate_in_open(vn, open_set):
#     key_str = vn.state.unique
#     if key_str in open_set[1]:
#         val = open_set[1][key_str]
#         return val >= vn.g
#     return False
#
#
# def duplicate_in_closed(vn, closed_set):
#     key_str = vn.state.unique
#     if key_str in closed_set:
#         val = closed_set[key_str]
#         return val >= vn.g
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
# def search(start_state, heuristic):
#     open_set = create_open_set()
#     closed_set = create_closed_set()
#     start_node = search_node(start_state, 0, heuristic(start_state))
#     add_to_open(start_node, open_set)
#
#     while open_not_empty(open_set):
#
#         current = get_best(open_set)
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





































import heapq
from search_node import search_node
from grid_robot_state import grid_robot_state

def create_open_set():
    open_new = []
    heapq.heapify(open_new)
    return open_new, {}  # Tuple with heap and dictionary

def create_closed_set():
    return {}

def add_to_open(vn, open_set):
    if vn.unique in open_set[1]:
        open_set[1][vn.unique] = vn.g
        heapq.heappush(open_set[0], (vn.f, vn))
    else:
        open_set[1][vn.unique] = vn.g
        heapq.heappush(open_set[0], (vn.f, vn))

def open_not_empty(open_set):
    return len(open_set[0]) != 0

def get_best(open_set):
    while open_not_empty(open_set):
        val, key = heapq.heappop(open_set[0])
        if key.unique in open_set[1]:
            del open_set[1][key.unique]
            return key
    return None

def add_to_closed(vn, closed_set):
    closed_set[vn.state.unique] = vn.f

def duplicate_in_open(vn, open_set):
    if vn.unique in open_set[1]:
        return open_set[1][vn.unique] >= vn.g
    return False

def duplicate_in_closed(vn, closed_set):
    if vn.state.unique in closed_set:
        return closed_set[vn.state.unique] >= vn.g
    return False

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

        add_to_closed(current, closed_set)

        for neighbor in current.get_neighbors():
            neighbor_state, edge_cost = neighbor
            curr_neighbor = search_node(neighbor_state, current.g + edge_cost, heuristic(neighbor_state), current)
            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)

    return None










# import heapq
# from search_node import search_node
# from grid_robot_state import grid_robot_state
#
# def create_open_set():
#     open_new = []
#     heapq.heapify(open_new) # Tuple with heap and dictionary
#     return open_new
#
# def create_closed_set():
#     return {}
#
# def add_to_open(vn, open_set):
#     heapq.heappush(open_set, (vn.f, vn))
#
# def open_not_empty(open_set):
#     return len(open_set[0]) != 0
#
# def get_best(open_set):
#     return heapq.heappop(open_set)[1]
#
# def add_to_closed(vn, closed_set):
#     closed_set[vn.state.unique] = vn.f
#
# def duplicate_in_open(vn, open_set):
#     # if vn.unique in open_set[1]:
#     #     return open_set[1][vn.unique] >= vn.g
#     # return False
#     for _, elem in open_set:
#         if elem == vn:
#             return elem.g <= vn.g
#         if elem.f > vn.f:
#             break
#     return False
#
# def duplicate_in_closed(vn, closed_set):
#     if vn.state.unique in closed_set:
#         return closed_set[vn.state.unique] >= vn.g
#     return False
#
# def search(start_state, heuristic):
#     open_set = create_open_set()
#     closed_set = create_closed_set()
#     start_node = search_node(start_state, 0, heuristic(start_state))
#     add_to_open(start_node, open_set)
#
#     while open_not_empty(open_set):
#         current = get_best(open_set)
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
#         for neighbor in current.get_neighbors():
#             neighbor_state, edge_cost = neighbor
#             curr_neighbor = search_node(neighbor_state, current.g + edge_cost, heuristic(neighbor_state), current)
#             if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
#                 add_to_open(curr_neighbor, open_set)
#
#     return None
