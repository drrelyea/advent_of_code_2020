# too tired to do this quickly
# way too many reading comprehension mistakes
# couldn't even figure out best format for strings for processing

import numpy as np
import pandas as pd
import re
import os
import urllib
from copy import deepcopy
with open('/Users/relyea/data/input_day11.txt') as aoc_fp:
    zz = [theline.rstrip() for theline in aoc_fp.readlines()]

# zz = [
#     'L.LL.LL.LL',
#     'LLLLLLL.LL',
#     'L.L.L..L..',
#     'LLLL.LL.LL',
#     'L.LL.LL.LL',
#     'L.LLLLL.LL',
#     '..L.L.....',
#     'LLLLLLLLLL',
#     'L.LLLLLL.L',
#     'L.LLLLL.LL',
# ]

ss = []
for line in zz:
    ss.append([xx for xx in line])

def get_num_neighbors_parta(ii,jj,seats):
    nn = 0
    for di in (ii-1, ii, ii+1):
        for dj in (jj-1, jj, jj+1):
            if (0 <= di < len(seats)) and (0 <= dj < len(seats[0])) and (di != ii or dj != jj):
                nn += seats[di][dj] == '#'
    return nn


def get_num_neighbors(ii,jj,seats):
    nn = 0
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if not (di == 0 and dj == 0):
                tmpi = ii + di
                tmpj = jj + dj
                sees_a_seat = False
                while not sees_a_seat and -1 < tmpi < len(seats) and -1 < tmpj < len(seats[0]):
                    if seats[tmpi][tmpj] == '#':
                        nn += 1
                        sees_a_seat = True
                    elif seats[tmpi][tmpj] == 'L':
                        sees_a_seat = True
                    tmpi += di
                    tmpj += dj
    return nn


def newstate(seats):
    newseats = []
    for line in seats:
        newseats.append([xx for xx in line])
    for ii in range(len(seats)):
        for jj in range(len(seats[0])):
            num_neighbors = get_num_neighbors(ii,jj,seats)
            if num_neighbors == 0 and seats[ii][jj] == 'L':
                newseats[ii][jj] = '#'
            elif num_neighbors >= 5 and seats[ii][jj] == '#':
                newseats[ii][jj] = 'L'
            else:
                newseats[ii][jj] = seats[ii][jj]
    return newseats

visited_seats = set()
thenewstate = ''.join([''.join(line) for line in ss])
while thenewstate not in visited_seats:
    visited_seats.add(thenewstate)
    ss = newstate(ss)
    # for line in [''.join(line) for line in ss]:
    #     print(line)
    # print('')
    thenewstate = ''.join([''.join(line) for line in ss])
    # print(len(visited_seats))
print(thenewstate.count('#'))
