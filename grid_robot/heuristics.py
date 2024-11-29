from grid_robot_state import grid_robot_state


def base_heuristic(_grid_robot_state):
    return abs(_grid_robot_state.get_location()[0] - _grid_robot_state.get_lamp_location()[0]) + \
        abs(_grid_robot_state.get_location()[1] - _grid_robot_state.get_lamp_location()[1])


# def advanced_heuristic(_grid_robot_state):
#
#     return (base_heuristic(_grid_robot_state) * (_grid_robot_state.get_stairs() + 1)) + \
#         (abs((_grid_robot_state.get_lamp_height() - _grid_robot_state.get_stairs())) * 2)


    # return (base_heuristic(_grid_robot_state) * (_grid_robot_state.get_stairs() + 1)) +\
    #     (_grid_robot_state.get_lamp_height() - _grid_robot_state.get_stairs())

# def advanced_heuristic(_grid_robot_state):
#
#     robot_loc = _grid_robot_state.get_location()
#     lamp_loc = _grid_robot_state.get_lamp_location()
#     lamp_height = _grid_robot_state.get_lamp_height()
#     stairs_held = _grid_robot_state.get_stairs()
#
#     # 1. Base heuristic: Manhattan distance to lamp
#     manhattan_dist = base_heuristic(_grid_robot_state)
#
#     # 2. Height mismatch
#     height_mismatch = max(0, lamp_height - stairs_held)
#
#     # 3. Estimated cost to collect additional stairs (if needed)
#     board = _grid_robot_state.get_board()
#     # min_stairs_cost = float('inf')
#     min_stairs_cost = 0
#     for i, row in enumerate(board):
#         for j, cell in enumerate(row):
#             if cell > 0:  # There are stairs here
#                 distance_to_stairs = abs(robot_loc[0] - i) + abs(robot_loc[1] - j)
#                 min_stairs_cost = max(min_stairs_cost, distance_to_stairs + 1)  # +1 for the pickup action
#
#     stairs_cost = min_stairs_cost if stairs_held < lamp_height else 0
#
#     # 4. Total heuristic value
#     heuristic_value = manhattan_dist + height_mismatch + stairs_cost
#
#     return heuristic_value

def advanced_heuristic(_grid_robot_state):
    robot_loc = _grid_robot_state.get_location()
    lamp_loc = _grid_robot_state.get_lamp_location()
    lamp_height = _grid_robot_state.get_lamp_height()
    stairs_held = _grid_robot_state.get_stairs()

    # 1. Base heuristic: Manhattan distance to lamp
    manhattan_dist = base_heuristic(_grid_robot_state)

    # 2. Height mismatch
    height_mismatch = max(0, lamp_height - stairs_held)

    # 3. Find the minimum cost to reach stairs (optionally pick them up)
    board = _grid_robot_state.get_board()
    min_stairs_cost = float('inf')
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell > 0:  # There are stairs here
                distance_to_stairs = abs(robot_loc[0] - i) + abs(robot_loc[1] - j)
                # Calculate the cost if stairs are picked up
                stairs_pickup_cost = max(0, lamp_height - (stairs_held + cell))
                # Total cost includes distance and optional pickup cost
                total_cost = distance_to_stairs + stairs_pickup_cost
                min_stairs_cost = min(min_stairs_cost, total_cost)

    # If no additional stairs are needed, set stairs_cost to 0
    stairs_cost = min_stairs_cost if stairs_held < lamp_height else 0

    # 4. Total heuristic value
    heuristic_value = manhattan_dist + height_mismatch + stairs_cost

    return heuristic_value