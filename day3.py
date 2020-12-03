import numpy as np
import pandas as pd

with open('/Users/relyea/data/input_day3.txt') as aoc_fp:
    input_data = [theline.rstrip() for theline in aoc_fp.readlines()]

# 8 minutes

# input_data = [
#     '..##.......',
#     '#...#...#..',
#     '.#....#..#.',
#     '..#.#...#.#',
#     '.#...##..#.',
#     '..#.##.....',
#     '.#.#.#....#',
#     '.#........#',
#     '#.##...#...',
#     '#...##....#',
#     '.#..#...#.#'
# ]

N = len(input_data)
bigprod = 1
ntrees = 0
for ii in range(N):
    if input_data[ii][ii*1 % len(input_data[0])] == '#':
        ntrees += 1
print(ntrees)
bigprod *= ntrees
ntrees = 0
for ii in range(N):
    if input_data[ii][ii*3 % len(input_data[0])] == '#':
        ntrees += 1
print(ntrees)
bigprod *= ntrees
ntrees = 0
for ii in range(N):
    if input_data[ii][ii*5 % len(input_data[0])] == '#':
        ntrees += 1
print(ntrees)
bigprod *= ntrees
ntrees = 0
for ii in range(N):
    if input_data[ii][ii*7 % len(input_data[0])] == '#':
        ntrees += 1
print(ntrees)
bigprod *= ntrees
ntrees = 0
for ii in range(0,N,2):
    print(ii)
    if input_data[ii][round(ii*0.5) % len(input_data[0])] == '#':
        ntrees += 1
print(ntrees)
bigprod *= ntrees
