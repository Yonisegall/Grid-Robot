from grid_robot_state import grid_robot_state


def base_heuristic(_grid_robot_state):
    loc_x, loc_y = _grid_robot_state.location
    loc_lamp_x, loc_lamp_y = _grid_robot_state.lamp_location
    return abs(loc_x - loc_lamp_x) + abs(loc_y - loc_lamp_y)



def advanced_heuristic(_grid_robot_state):
    if grid_robot_state.is_goal_state(_grid_robot_state):
        return 0
    lamp_height = _grid_robot_state.lamp_height
    stairs_held = _grid_robot_state.stairs
    if stairs_held == 0:
        return base_heuristic(_grid_robot_state) + lamp_height
    else:
        return (base_heuristic(_grid_robot_state) * stairs_held) + (lamp_height - stairs_held)


# def advanced_heuristic(_grid_robot_state):
#     robot_loc_x, robot_loc_y = _grid_robot_state.location
#     lamp_height = _grid_robot_state.lamp_height
#     stairs_held = _grid_robot_state.stairs
#
#     # 1. Base heuristic: Manhattan distance to lamp
#     manhattan_dist = base_heuristic(_grid_robot_state)
#
#     # 2. Height mismatch
#     # height_mismatch = max(0, lamp_height - stairs_held)
#     height_mismatch = lamp_height - stairs_held if lamp_height - stairs_held > 0 else 0
#
#     # 3. Estimated cost to collect additional stairs (if needed)
#     board = _grid_robot_state.map
#     min_stairs_cost = 0
#
#     if height_mismatch != 0:
#         # Need more stairs
#         for i, row in enumerate(board):
#             for j, cell in enumerate(row):
#                 if cell > 0:  # There are stairs here
#                     distance_to_stairs = abs(robot_loc_x - i) + abs(robot_loc_y - j)
#                     min_stairs_cost = distance_to_stairs if distance_to_stairs > min_stairs_cost else min_stairs_cost
#
#     stairs_cost = min_stairs_cost if stairs_held < lamp_height else 0
#
#     return manhattan_dist + height_mismatch + stairs_cost
#