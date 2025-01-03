# class grid_robot_state:
#
#     def __init__(self, robot_location, map=None, lamp_height=-1, lamp_location=(-1, -1), stairs=0):
#         # you can use the init function for several purposes
#         self.location = robot_location
#         self.map = map
#         self.lamp_height = lamp_height
#         self.lamp_location = lamp_location
#         self.stairs = stairs
#         self.unique = f'{self.location}, {self.stairs}, {self.map}'
#
#
#
#     # "----------The faster ----------"
#
#     @staticmethod
#     def is_goal_state(_grid_robot_state):
#         return _grid_robot_state.location == _grid_robot_state.lamp_location and \
#                _grid_robot_state.stairs == _grid_robot_state.lamp_height  # The faster
#
#     def get_neighbors(self):
#         loc_x, loc_y = self.location
#         cur_stairs_weight = self.map[loc_x][loc_y]
#         direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#         my_neighbors = []
#
#         # 1: all regular neighbors
#         for x, y in direction:
#
#             if self.is_Valid((loc_x + x, loc_y + y)):  # The faster
#                 if self.stairs == self.lamp_height and (loc_x + x, loc_y + y) == self.lamp_location:
#                     self.add_neighbor(my_neighbors, loc_x + x, loc_y + y, self.map, 2, 0)
#                 else:
#                     self.add_neighbor(my_neighbors, loc_x + x, loc_y + y, self.map, 1, 0)
#
#         # 2: The cell is stairs to pick up
#         if cur_stairs_weight != 0:
#             new_board = self.return_new_board(loc_x, loc_y, 0)
#             self.add_neighbor(my_neighbors, loc_x, loc_y, new_board,
#                               (self.stairs * (-1)) + 1, cur_stairs_weight)
#
#         # Dropped the current stairs
#         if self.stairs != 0:
#             new_board = self.return_new_board(loc_x, loc_y, cur_stairs_weight + self.stairs)
#             self.add_neighbor(my_neighbors, loc_x, loc_y, new_board,
#                               (self.stairs * (-1)) + 1, (self.stairs * (-1)))
#
#         return my_neighbors
#
#
#
#     @staticmethod
#     def is_goal_state(_grid_robot_state):
#         dx, dy = _grid_robot_state.location
#         return (dx, dy) == _grid_robot_state.lamp_location and \
#                _grid_robot_state.map[dx][dy] == _grid_robot_state.lamp_height and _grid_robot_state.stairs == 0
#
#     def get_neighbors(self):
#         loc_x, loc_y = self.location
#         cur_cell_stairs_weight = self.map[loc_x][loc_y]
#         direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#         my_neighbors = []
#
#         # 1: right, left, up and down neighbors
#         for x, y in direction:
#             if self.is_Valid((loc_x + x, loc_y + y)):
#                 self.add_neighbor(my_neighbors, loc_x + x, loc_y + y, self.map, 1, 0)
#
#         # 2: The cell is stairs , "pick up" stairs neighbor
#         if cur_cell_stairs_weight != 0:
#             new_board = self.return_new_board(loc_x, loc_y, 0)
#             self.add_neighbor(my_neighbors, loc_x, loc_y, new_board,
#                               (self.stairs * (-1)) + 1, cur_cell_stairs_weight)
#
#         # 3: already hold stairs, "dropped" stairs neighbor
#         if self.stairs != 0:
#             new_board = self.return_new_board(loc_x, loc_y, cur_cell_stairs_weight + self.stairs)
#             self.add_neighbor(my_neighbors, loc_x, loc_y, new_board,
#                               (self.stairs * (-1)) + 1, (self.stairs * (-1)))
#
#         return my_neighbors
#
#
#     def add_neighbor(self, my_neighbors, dx, dy, new_board, new_cost, cur_stairs_weight):
#         new_neighbor = grid_robot_state((dx, dy), new_board, self.lamp_height, self.lamp_location,
#                                         self.stairs + cur_stairs_weight)
#         my_neighbors.append((new_neighbor, self.stairs + new_cost))
#
#     def return_new_board(self, x, y, num):
#         new_board = [row[:] for row in self.map]  # Faster manual copy
#         new_board[x][y] = num
#         return new_board
#
#     def is_Valid(self, other_state):
#         row, col = other_state
#         # Check if the row and column are within bounds of the board
#         return 0 <= row < len(self.map) and 0 <= col < len(self.map[row]) and self.map[row][col] != -1

























































# the best so far
# class grid_robot_state:
#     def __init__(self, robot_location, map=None, lamp_height=-1, lamp_location=(-1, -1), stairs=0):
#
#         """ Constructor for grid_robot_state"""
#
#         # Using immutable map representation
#         self.location = robot_location
#         self.map = tuple(tuple(row) for row in map) if map else None
#         self.lamp_height = lamp_height
#         self.lamp_location = lamp_location
#         self.stairs = stairs
#         # Optimized unique key
#         self.unique = (self.location, self.stairs, hash(self.map))
#
#
#     @staticmethod
#     def is_goal_state(_grid_robot_state):
#         """ return True if the search is over, False otherwise"""
#         dx, dy = _grid_robot_state.location
#         return (dx, dy) == _grid_robot_state.lamp_location and \
#                _grid_robot_state.map[dx][dy] == _grid_robot_state.lamp_height and _grid_robot_state.stairs == 0
#
#     def get_neighbors(self):
#         """return all the neighbors operators of current state"""
#         loc_x, loc_y = self.location
#         directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#         neighbors = []
#
#         for dx, dy in directions:
#             if self.is_Valid((loc_x + dx, loc_y + dy)):
#                 neighbors.append((grid_robot_state((loc_x + dx, loc_y + dy), self.map, self.lamp_height,
#                                                    self.lamp_location, self.stairs), 1 + self.stairs))
#
#         cur_cell_stairs_weight = self.map[loc_x][loc_y]
#
#         if cur_cell_stairs_weight != 0:  # Pick up stairs
#             new_map = self.return_new_map(loc_x, loc_y, 0)
#             neighbors.append((grid_robot_state(self.location, new_map, self.lamp_height, self.lamp_location,
#                                                self.stairs + cur_cell_stairs_weight), 1))
#
#         if self.stairs != 0 and cur_cell_stairs_weight == 0:  # Drop stairs
#             new_map = self.return_new_map(loc_x, loc_y, cur_cell_stairs_weight + self.stairs)
#             neighbors.append((grid_robot_state(self.location, new_map, self.lamp_height, self.lamp_location, 0), 1))
#
#         return neighbors
#
#     def return_new_map(self, x, y, num):
#         """ Copying the map and returns new update new one"""
#         # Faster manual copy with immutability
#         return tuple(
#             tuple(num if (i == x and j == y) else cell for j, cell in enumerate(row))for i, row in enumerate(self.map)
#         )
#
#     def is_Valid(self, other_state):
#         """ Checking if a location is valid inside the map"""
#         row, col = other_state
#         return 0 <= row < len(self.map) and 0 <= col < len(self.map[row]) and self.map[row][col] != -1



















class grid_robot_state:
    def __init__(self, robot_location, map=None, lamp_height=-1, lamp_location=(-1, -1), stairs=0):

        """ Constructor for grid_robot_state"""

        # Using immutable map representation
        self.location = robot_location
        self.map = map
        self.lamp_height = lamp_height
        self.lamp_location = lamp_location
        self.stairs = stairs
        # Optimized unique key
        self.unique = f'{self.location}, {self.stairs}, {self.map}'


    @staticmethod
    def is_goal_state(_grid_robot_state):
        """ return True if the search is over, False otherwise"""
        dx, dy = _grid_robot_state.location
        return (dx, dy) == _grid_robot_state.lamp_location and \
               _grid_robot_state.map[dx][dy] == _grid_robot_state.lamp_height and _grid_robot_state.stairs == 0

    def get_neighbors(self):
        """return all the neighbors operators of current state i the problem"""
        loc_x, loc_y = self.location
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        neighbors = []

        # 1: right, left, up and down neighbors
        for dx, dy in directions:
            if self.is_Valid((loc_x + dx, loc_y + dy)):
                neighbors.append((grid_robot_state((loc_x + dx, loc_y + dy), self.map, self.lamp_height,
                                                   self.lamp_location, self.stairs), 1 + self.stairs))

        # 2: The cell is stairs , "pick up" stairs neighbor
        cur_cell_stairs_weight = self.map[loc_x][loc_y]
        if cur_cell_stairs_weight != 0:  # Pick up stairs
            new_map = self.return_new_map(loc_x, loc_y, 0)
            neighbors.append((grid_robot_state(self.location, new_map, self.lamp_height, self.lamp_location,
                                               self.stairs + cur_cell_stairs_weight), 1))

        # 3: already holding stairs, "dropped" stairs neighbor
        if self.stairs != 0 and cur_cell_stairs_weight == 0:  # Drop stairs
            new_map = self.return_new_map(loc_x, loc_y, cur_cell_stairs_weight + self.stairs)
            neighbors.append((grid_robot_state(self.location, new_map, self.lamp_height, self.lamp_location, 0), 1))

        return neighbors

    def return_new_map(self, x, y, num):
        """ Copying the map and returns new immutable update new one"""
        # Faster manual copy with immutability
        # return tuple(
        #     tuple(num if (i == x and j == y) else cell for j, cell in enumerate(row))for i, row in enumerate(self.map)
        # )

        new_board = [row[:] for row in self.map]  # Faster manual copy
        new_board[x][y] = num
        return new_board

    def is_Valid(self, other_state):
        """ Checking if a location is valid inside the map borders"""
        row, col = other_state
        return 0 <= row < len(self.map) and 0 <= col < len(self.map[row]) and self.map[row][col] != -1
