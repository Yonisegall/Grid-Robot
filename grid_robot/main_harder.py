import time
from heuristics import *
from search import *

if __name__ == '__main__':


    bitch_map = [
        [0,  0,  0,  0,  0, 0, 0, 0],
        [0,  0,  0,  4,  0, 0, 0, 0],
        [0,  0,  0,  0, -1, 0, 0, 0],
        [0,  0,  0,  0, -1, 0, 3, 0],
        [0,  0,  0,  0, -1, 0, 0, 0],
        [0, -1, -1, -1, -1, 0, 0, 0],
        [0,  0,  0,  0,  0, 0, 0, 0]
    ]
    robot_start_location = (2, 1)
    lamp_h = 7
    lamp_location = (4, 2)

    start_state = grid_robot_state(board= bitch_map, robot_location=robot_start_location, lamp_height=lamp_h,
                                   lamp_location=lamp_location)
    start_time = time.time()
    search_result = search(start_state, advanced_heuristic)
    end_time = time.time() - start_time
    # runtime
    print(end_time)
    # solution cost
    print(search_result[-1].g)

    for elem in search_result:
        print(f'location {elem.state.get_location()} , cost = {elem.g}\n')









    # # Big test case
    # map = [            #
    #     [0,  0, 0,  0, 0,  0,  0,  0],
    #     [1,  4, 2, -1, 0,  0,  0,  0],
    #     [0, -1, 0, -1, 1, -1, -1, -1],
    #     [0,  0, 0,  0, 0,  0,  0,  0],
    #     [1,  4, 2, -1, 0,  0,  0,  0],
    #     [0, -1, 0, -1, 1,  1,  1,  1],
    #     [0,  0, 0,  0, 0,  0,  0,  0],
    #     [1,  4, 2, -1, 0,  0,  0,  0],
    #     [0, -1, 0, -1, 1,  1,  1,  1],
    #     [0,  0, 0,  0, 0,  0,  0,  0],
    #     [1,  4, 2, -1, 0,  0,  0,  0],
    #     [0, -1, 0, -1, 1,  1,  1,  1]
    # ]
    # robot_start_location = (5, 5)
    # lamp_h = 10
    # lamp_location = (0, 4)
    #
    # start_state = grid_robot_state(board=map, robot_location=robot_start_location, lamp_height=lamp_h,
    #                                lamp_location=lamp_location)
    # start_time = time.time()
    # search_result = search(start_state, advanced_heuristic)
    # end_time = time.time() - start_time
    # # runtime
    # print(end_time)
    # # solution cost
    # print(search_result[-1].g)
    #
    # for elem in search_result:
    #     print(f'location {elem.state.get_location()} , cost = {elem.state.get_stairs()}\n')




