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

def count_trees(themap, dx, dy):
    ix = dx
    iy = dy
    ntrees = 0
    while iy < len(themap):
        ntrees += int(themap[iy][ix % len(themap[0])] == '#')
        ix += dx
        iy += dy
    return ntrees

themult = 1
for (dx,dy) in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
    ntrees = count_trees(input_data, dx, dy)
    print(ntrees)
    themult *= ntrees
print(themult)

