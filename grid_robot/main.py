import time
from heuristics import *
from search import *

if __name__ == '__main__':



    # map = [
    #     [0, 0, 0, 0],
    #     [1, 4, 2, -1],
    #     [0, -1, 0, -1]
    # ]
    #
    # robot_start_location = (0, 0)
    # lamp_h = 6
    # lamp_location = (2, 2)
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
    #






    # map_2 = [
    #     [0,  0,  0,  0,  0, 0, 0, 0],
    #     [0,  0,  0,  4,  0, 0, 0, 0],
    #     [0,  0,  0,  0, -1, 0, 0, 0],
    #     [0,  0,  0,  0, -1, 0, 3, 0],
    #     [0,  0,  0,  0, -1, 0, 0, 0],
    #     [0, -1, -1, -1, -1, 0, 0, 0],
    #     [0,  0,  0,  0,  0, 0, 0, 0]
    # ]
    # robot_start_location = (2, 1)
    # lamp_h = 7
    # lamp_location = (4, 2)
    #
    # start_state = grid_robot_state(board=map_2, robot_location=robot_start_location, lamp_height=lamp_h,
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







    # map_3 = [
    #     [0,  0,  2, 0],
    #     [0, -1, -1, 0],
    #     [0, -1,  0, 0],
    #     [0,  0,  2, 0]
    # ]
    #
    # robot_start_location = (0, 0)  # מיקום ההתחלה של הרובוט
    # lamp_h = 4  # גובה המנורה
    # lamp_location = (2, 2)  # מיקום המנורה
    #
    # start_state = grid_robot_state(board=map_3, robot_location=robot_start_location, lamp_height=lamp_h,
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






                                    #
    map = [[0, 0, 0,  0, 0, 1,  0,  0],
           [0, 0, 0, -1, 0, 0,  0,  0],
           [0, 0, 2,  0, 0, 0, -1,  0],
           [0, 0, 0,  0, 0, 0,  0,  0],
           [0, 0, 0, -1, 0, 1,  0,  0],
           [0, 0, 0,  0, 0, 0,  0,  0],
           [0, 0, 0,  0, 0, 2,  0,  0],
           [0, 0, 0,  0, 0, 0,  0,  3]]

    robot_start_location = (7, 0)
    lamp_h = 3
    lamp_location = (0, 7)
    # # expected Heuristic is: [14, 13, 12, 11, 10, 9, 8, 7, 7, 6, 5, 4, 3, 2, 2, 1, 0, 0]



                            #
    # map = [[0,  0,  0,  0,  0,  0,  0,  0], # Us cost 28
    #        [2,  0, -1,  0,  0,  1,  0,  0],
    #        [0, -1,  1,  0,  2,  0, -1,  0],
    #        [0,  0,  2,  0, -1,  1,  0,  0],
    #        [0,  0,  2,  1,  0,  3,  0,  0],
    #        [-1, 1,  0, -1,  0, -1,  0,  0],
    #        [-1, 0, -1,  0,  0,  1,  0, -1],
    #        [0,  0,  0,  0,  0,  0,  0,  0]]
    #
    # robot_start_location = (7, 0)
    # lamp_h = 4
    # lamp_location = (0, 4)
    # expected Heuristic is: [11,10,9,8,7,6,5,5,4,3,2,2,1,1 ,0]

    start_state = grid_robot_state(board=map, robot_location=robot_start_location, lamp_height=lamp_h,
                                   lamp_location=lamp_location)
    start_time = time.time()
    search_result = search(start_state, advanced_heuristic)
    end_time = time.time() - start_time
    # runtime
    print(end_time)
    # solution cost
    print(search_result[-1].g)

    for elem in search_result:
        print(f'location {elem.state.get_location()} , cost = {elem.state.get_stairs()}\n')


    print("fuck BGU")
