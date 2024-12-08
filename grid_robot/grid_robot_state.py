class grid_robot_state:

    def __init__(self, robot_location, map=None, lamp_height=-1, lamp_location=(-1, -1), stairs=0):
        # you can use the init function for several purposes
        self.location = robot_location
        self.map = map
        self.lamp_height = lamp_height
        self.lamp_location = lamp_location
        self.stairs = stairs
        self.unique = f'{self.location}, {self.stairs}, {self.map}'

    @staticmethod
    def is_goal_state(_grid_robot_state):
        # return _grid_robot_state.location == _grid_robot_state.lamp_location and \
        #        _grid_robot_state.stairs == _grid_robot_state.lamp_height

        x, y = _grid_robot_state.location
        return (x, y) == _grid_robot_state.lamp_location and \
                         _grid_robot_state.stairs == 0 and \
                         _grid_robot_state.map[x][y] == _grid_robot_state.lamp_height

    def get_neighbors(self):
        loc_x, loc_y = self.location
        cur_stairs_weight = self.map[loc_x][loc_y]
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        my_neighbors = []

        # 1: all regular neighbors
        for x, y in direction:

            # if self.location == self.lamp_location and self.stairs == self.lamp_height:
            #     new_board = self.return_new_board(loc_x, loc_y, cur_stairs_weight + self.stairs)
            #     self.add_neighbor(my_neighbors, loc_x, loc_y, new_board,
            #                       (self.stairs * (-1)) + 1, (self.stairs * (-1)))
            #     return my_neighbors
            # if self.is_Valid((loc_x + x, loc_y + y)):
            #     self.add_neighbor(my_neighbors, loc_x + x, loc_y + y, self.map, 1, 0)


            if self.is_Valid((loc_x + x, loc_y + y)):
                # if self.stairs == self.lamp_height and (loc_x + x, loc_y + y) == self.lamp_location:
                #     self.add_neighbor(my_neighbors, loc_x + x, loc_y + y, self.map, 2, 0)
                # else:
                self.add_neighbor(my_neighbors, loc_x + x, loc_y + y, self.map, 1, 0)

        # 2: The cell is stairs to pick up
        if cur_stairs_weight != 0:
            new_board = self.return_new_board(loc_x, loc_y, 0)
            self.add_neighbor(my_neighbors, loc_x, loc_y, new_board,
                              (self.stairs * (-1)) + 1, cur_stairs_weight)

        # Dropped the current stairs
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
        new_board = [row[:] for row in self.map]  # Faster manual copy
        new_board[x][y] = num
        return new_board

    def is_Valid(self, other_state):
        row, col = other_state
        # Check if the row and column are within bounds of the board
        return 0 <= row < len(self.map) and 0 <= col < len(self.map[row]) and self.map[row][col] != -1
