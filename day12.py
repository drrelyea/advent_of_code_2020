# # too tired to do this quickly
# # way too many reading comprehension mistakes
# # couldn't even figure out best format for strings for processing

# import numpy as np
# import pandas as pd
# import re
# import os
# import urllib
# from copy import deepcopy
# with open('/Users/relyea/data/input_day12.txt') as aoc_fp:
#     zz = [theline.rstrip() for theline in aoc_fp.readlines()]

# # zz = [
# #     'F10',
# #     'N3',
# #     'F7',
# #     'R90',
# #     'F11',
# # ]


# facings = {
#     0: "N",
#     1: "E",
#     2: "S",
#     3: "W"
# }

# def move(location, facing):
#     print(facing)
#     if facing[0] == "N":
#         location[1] += int(facing[1:])
#     elif facing[0] == "S":
#         location[1] -= int(facing[1:])
#     elif facing[0] == "E":
#         location[0] += int(facing[1:])
#     elif facing[0] == "W":
#         location[0] -= int(facing[1:])
#     return location

# location = [0,0]
# direction = 1
# for line in zz:
#     if line[0] == "L":
#         direction = (direction - int(line[1:])/90) % 4
#         facing = facings[direction] + line[1:]
#     elif line[0] == "R":
#         direction = (direction + int(line[1:])/90) % 4
#         facing = facings[direction] + line[1:]
#     elif line[0] == "F":
#         facing = facings[direction] + line[1:]
#         location = move(location, facing)
#     else:
#         facing = line
#         location = move(location, facing)
#     print(location, direction)




with open('/Users/relyea/data/input_day12.txt') as aoc_fp:
    zz = [theline.rstrip() for theline in aoc_fp.readlines()]

# # zz = [
# #     'F10',
# #     'N3',
# #     'F7',
# #     'R90',
# #     'F11',
# # ]


location = [0,0]
waypoint = [10,1]
direction = 1

def moveway(deltax, deltay, nright):
    if nright == 1:
        outy = -1*deltax
        outx = deltay
    elif nright == 2:
        outy = -1*deltay
        outx = -1*deltax
    elif nright == 3:
        outy = deltax
        outx = -1*deltay
    else:
        outx = deltax
        outy = deltay
    return outx, outy


for line in zz:
    delta_way_loc_x = waypoint[0]-location[0]
    delta_way_loc_y = waypoint[1]-location[1]
    nn = int(line[1:])
    if line[0] == "L":
        nright = (-1*nn/90) % 4
        dx, dy = moveway(delta_way_loc_x, delta_way_loc_y, nright)
        waypoint[0] = location[0] + dx
        waypoint[1] = location[1] + dy
    elif line[0] == "R":
        nright = (nn/90) % 4
        dx, dy = moveway(delta_way_loc_x, delta_way_loc_y, nright)
        waypoint[0] = location[0] + dx
        waypoint[1] = location[1] + dy
    elif line[0] == "F":
        location[0] += nn*delta_way_loc_x
        location[1] += nn*delta_way_loc_y
        waypoint[0] += nn*delta_way_loc_x
        waypoint[1] += nn*delta_way_loc_y
    elif line[0] == "N":
        waypoint[1] += nn
    elif line[0] == "S":
        waypoint[1] -= nn
    elif line[0] == "E":
        waypoint[0] += nn
    elif line[0] == "W":
        waypoint[0] -= nn
    print(location, waypoint, line)

