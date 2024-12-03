from search_node import search_node
from grid_robot_state import grid_robot_state
import heapq
#
#
# def create_open_set():         # The Best That Works
#     open_new = []
#     heapq.heapify(open_new)
#     return open_new  # Return tuple with heap and dictionary
#
#
# def create_closed_set():
#     return []
#
#
# def add_to_open(vn, open_set):
#     heapq.heappush(open_set, (vn.f, vn))
#
#
# def open_not_empty(open_set):
#     return len(open_set[0]) != 0  # Return True if the heap is not empty
#
#
# def get_best(open_set):
#     val, key = heapq.heappop(open_set)
#     return key
#
#
# def add_to_closed(vn, closed_set):
#     closed_set.append(vn)
#
#
# def duplicate_in_open(vn, open_set):
#     for item in open_set:
#         val, key = item
#         if key == vn:
#             if val <= vn.g:
#                 return True
#     return False
#
#     # if vn in open_set[1]:
#     #     existing_cost = open_set[1][vn]
#     #     if vn.g >= existing_cost:
#     #         return True
#     # return False
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
#     open_set[1][vn.state.get_str()] = vn.f
#
#
# def open_not_empty(open_set):
#     return len(open_set[0]) != 0  # Return True if the heap is not empty
#
#
# def get_best(open_set):
#     val, key = heapq.heappop(open_set[0])
#     del open_set[1][key.state.get_str()]
#     return key
#
#
# def add_to_closed(vn, closed_set):
#     closed_set[vn.state.get_str()] = vn.f
#
#
# def duplicate_in_open(vn, open_set):
#     # val = open_set[1].get(vn.state.get_str())
#     # if val is None: return False
#     # return val <= vn.g
#
#     key_str = vn.state.get_str()
#     if key_str in open_set[1]:
#         val = open_set[1][key_str]
#         return val >= vn.g
#     return False
#
#     # for item in open_set:
#     #     val, key = item
#     #     if key == vn:
#     #         if val <= vn.f:
#     #             return True
#     # return False
#
#
# def duplicate_in_closed(vn, closed_set):
#
#     # for elem in closed_set:
#     #     if elem.state == vn.state:
#     #         if vn.g >= elem.g:
#     #             return True
#     # return False
#
#     key_str = vn.state.get_str()
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














def create_open_set():  # Try with HashMap
    open_new = []
    heapq.heapify(open_new)
    return open_new, {}  # Return tuple with heap and dictionary


def create_closed_set():
    return {}


def add_to_open(vn, open_set):
    heapq.heappush(open_set[0], (vn.f, vn))
    open_set[1][vn.get_str()] = vn.g


def open_not_empty(open_set):
    return len(open_set[0]) != 0  # Return True if the heap is not empty


def get_best(open_set):
    val, key = heapq.heappop(open_set[0])
    b = open_set[1].get(key.get_str())
    if b is not None: del open_set[1][key.get_str()]
    return key


def add_to_closed(vn, closed_set):
    closed_set[vn.get_str()] = vn.g


def duplicate_in_open(vn, open_set):

    key_str = vn.state.get_str()
    if key_str in open_set[1]:
        val = open_set[1][key_str]
        if val <= vn.g:
            return True
    return False

    # for item in open_set:
    #     val, key = item
    #     if key == vn:
    #         if val <= vn.f:
    #             return True
    # return False


def duplicate_in_closed(vn, closed_set):

    # for elem in closed_set:
    #     if elem.state == vn.state:
    #         if elem.g <= vn.g:
    #             return True
    # return False

    key_str = vn.get_str()
    if key_str in closed_set:
        val = closed_set[key_str]
        if val <= vn.g:
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

        add_to_closed(current, closed_set)

        for neighbor, edge_cost in current.get_neighbors():
            curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)

    return None

