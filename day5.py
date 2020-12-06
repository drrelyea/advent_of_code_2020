import numpy as np
import pandas as pd
import re

with open('/Users/relyea/data/input_day5.txt') as aoc_fp:
    input_data = [theline.rstrip() for theline in aoc_fp.readlines()]

def find_seat(seatstr):
    # ohhh it's just binary - I'm a tool
    rangetop = 128
    rangebot = 0
    aislebot = 0
    aisletop = 8
    rowrange = 128
    aislerange = 8
    for seatchar in seatstr[0:7]:
        rowrange = rowrange/2
        if seatchar == 'F':
            rangetop = rangebot + rowrange
        elif seatchar == 'B':
            rangebot = rangetop - rowrange
    for seatchar in seatstr[7:]:
        aislerange = aislerange/2
        if seatchar == 'L':
            aisletop = aislebot + aislerange
        elif seatchar == 'R':
            aislebot = aisletop - aislerange
    return (rangetop-1)*8+ (aisletop-1)

maxseat = 0
for line in input_data:
    if find_seat(line) > maxseat:
        maxseat = find_seat(line)
print(maxseat)


seat_exist = np.zeros(int(maxseat))
for line in input_data:
    seat_exist[int(find_seat(line))-1] = 1
