import numpy as np

def base_map(env, pick_locs, drop_locs):
    x_min = env["dimensions"]["x_min"]
    y_min = env["dimensions"]["y_min"]

    x_size = env["dimensions"]["x_max"] - x_min
    y_size = env["dimensions"]["y_max"] - y_min

    grid = [[0] * x_size]
    for _ in range(y_size):
        grid.append([0] * x_size)

    for obstacle in env["obstacles"]:
        grid[obstacle[1] - y_min][obstacle[0] - x_min] = 1
    
    for loc in pick_locs + drop_locs:
        loc_x = int(10 * loc[1][0] - x_min)
        loc_y = int(10 * loc[1][1] - y_min)

        # print((loc_x, loc_y))

        grid[loc_y][loc_x] = 1
    
    return grid

def agent_map(map, agent_locs):
    for loc in agent_locs:
        map[int(loc[1] * 10 + 9)][int(loc[0] * 10 + 9)] = 0
    
    return map