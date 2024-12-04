# import copy
#
#
# class grid_robot_state:
#     # global cost
#
#     def __init__(self, robot_location, board=None, lamp_height=-1, lamp_location=(-1, -1)):
#         # you can use the init function for several purposes
#         self.location = robot_location
#         self.board = board
#         self.lamp_height = lamp_height
#         self.lamp_location = lamp_location
#         self.stairs = 0
#         self.unique = ""
#
#     @staticmethod
#     def is_goal_state(_grid_robot_state):
#         bool = _grid_robot_state.get_location() == _grid_robot_state.get_lamp_location() and \
#                _grid_robot_state.get_stairs() == _grid_robot_state.get_lamp_height()
#         return bool
#
#     def get_neighbors(self):
#         loc_x, loc_y = self.location
#         cur_stairs_weight = self.board[loc_x][loc_y]
#         direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#         my_neighbors = []
#
#         # 1: all regular neighbors
#         for x, y in direction:
#             if self.is_Valid((loc_x + x, loc_y + y)):
#
#                 if self.stairs == self.lamp_height and (loc_x + x, loc_y + y) == self.lamp_location:
#                     self.add_neighbor(my_neighbors, loc_x + x, loc_y + y, self.board, 2, 0)
#                 else:
#                     self.add_neighbor(my_neighbors, loc_x + x, loc_y + y, self.board, 1, 0)
#
#         if cur_stairs_weight != 0:
#             new_board = self.return_new_board(loc_x, loc_y, 0)
#             self.add_neighbor(my_neighbors, loc_x, loc_y, new_board,
#                               (self.stairs * (-1)) + 1, cur_stairs_weight)
#
#         if self.stairs != 0:
#             new_board = self.return_new_board(loc_x, loc_y, cur_stairs_weight + self.stairs)
#             self.add_neighbor(my_neighbors, loc_x, loc_y, new_board,
#                               (self.stairs * (-1)) + 1, (self.stairs * (-1)))
#
#         return my_neighbors
#
#     # you can change the body of the function if you want
#     # def __hash__(self):
#     #     return hash((self.location, self.lamp_location, self.lamp_height, self.flatten_board()))
#
#     def __hash__(self):
#         return hash((
#             self.location,  # Robot's location
#             self.lamp_location,  # Lamp's location
#             self.lamp_height,  # Height of the lamp
#             tuple(map(tuple, self.board)),  # Immutable representation of the board (tuple of tuples)
#             self.stairs  # Current stairs value
#         ))
#
#     def add_neighbor(self, my_neighbors, dx, dy, new_board, new_cost, cur_stairs_weight):
#         new_neighbor = grid_robot_state((dx, dy), new_board, self.lamp_height, self.lamp_location)
#         new_neighbor.set_stairs(self.stairs + cur_stairs_weight)
#         my_neighbors.append((new_neighbor, self.stairs + new_cost))
#
#     def return_new_board(self, x, y, num):
#         new_board = copy.deepcopy(self.board)
#         new_board[x][y] = num
#         return new_board
#
#     def __eq__(self, other):
#         if other is None or not isinstance(other, grid_robot_state):
#             return False
#         return self.location == other.get_location() and self.lamp_location == other.lamp_location and \
#                self.lamp_height == other.get_lamp_height() and self.board == other.get_board()
#
#     def get_location(self):
#         return self.location
#
#     def set_location(self, loc):
#         self.location = loc
#
#     def get_lamp_location(self):
#         return self.lamp_location
#
#     def get_lamp_height(self):
#         return self.lamp_height
#
#     def get_board(self):
#         return self.board
#
#     def get_stairs(self):
#         return self.stairs
#
#     def set_stairs(self, num):
#         self.stairs = num
#         self.unique = f'{self.location}, {self.stairs}, {self.board}'
#
#     def is_Valid(self, other_state):
#         row, col = other_state
#         # Check if the row and column are within bounds of the board
#         if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[row]):
#             return False
#
#         return self.board[row][col] != -1
#
#     def get_str(self):
#         return f'{self.location}, {self.stairs}, {self.board}'






import copy


class grid_robot_state:
    # global cost

    def __init__(self, robot_location, board=None, lamp_height=-1, lamp_location=(-1, -1), stairs=0):
        # you can use the init function for several purposes
        self.location = robot_location
        self.board = board
        self.lamp_height = lamp_height
        self.lamp_location = lamp_location
        self.stairs = stairs
        self.unique = f'{self.location}, {self.stairs}, {self.board}'

    @staticmethod
    def is_goal_state(_grid_robot_state):
        bool = _grid_robot_state.get_location() == _grid_robot_state.get_lamp_location() and \
               _grid_robot_state.get_stairs() == _grid_robot_state.get_lamp_height()
        return bool

    def get_neighbors(self):
        loc_x, loc_y = self.location
        cur_stairs_weight = self.board[loc_x][loc_y]
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        my_neighbors = []

        # 1: all regular neighbors
        for x, y in direction:
            if self.is_Valid((loc_x + x, loc_y + y)):

                if self.stairs == self.lamp_height and (loc_x + x, loc_y + y) == self.lamp_location:
                    self.add_neighbor(my_neighbors, loc_x + x, loc_y + y, self.board, 2, 0)
                else:
                    self.add_neighbor(my_neighbors, loc_x + x, loc_y + y, self.board, 1, 0)

        if cur_stairs_weight != 0:
            new_board = self.return_new_board(loc_x, loc_y, 0)
            self.add_neighbor(my_neighbors, loc_x, loc_y, new_board,
                              (self.stairs * (-1)) + 1, cur_stairs_weight)

        if self.stairs != 0:
            new_board = self.return_new_board(loc_x, loc_y, cur_stairs_weight + self.stairs)
            self.add_neighbor(my_neighbors, loc_x, loc_y, new_board,
                              (self.stairs * (-1)) + 1, (self.stairs * (-1)))

        return my_neighbors

    def add_neighbor(self, my_neighbors, dx, dy, new_board, new_cost, cur_stairs_weight):
        new_neighbor = grid_robot_state((dx, dy), new_board, self.lamp_height, self.lamp_location,
                                        self.stairs + cur_stairs_weight)
        my_neighbors.append((new_neighbor, self.stairs + new_cost))

    def return_new_board(self, x, y, num):
        # new_board = copy.deepcopy(self.board)
        new_board = [row[:] for row in self.board]  # Faster manual copy

        new_board[x][y] = num
        return new_board

    def __eq__(self, other):
        if other is None or not isinstance(other, grid_robot_state):
            return False
        return self.location == other.get_location() and self.lamp_location == other.lamp_location and \
               self.lamp_height == other.get_lamp_height() and self.board == other.get_board()

    def get_location(self):
        return self.location

    def set_location(self, loc):
        self.location = loc

    def get_lamp_location(self):
        return self.lamp_location

    def get_lamp_height(self):
        return self.lamp_height

    def get_board(self):
        return self.board

    def get_stairs(self):
        return self.stairs

    def is_Valid(self, other_state):
        row, col = other_state
        # Check if the row and column are within bounds of the board
        if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[row]):
            return False

        return self.board[row][col] != -1

