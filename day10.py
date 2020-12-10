# first half - literally top 100
# second half - I miscounted the permutations (oof)

import numpy as np
import pandas as pd
import re
import os
import urllib

with open('/Users/relyea/data/input_day10.txt') as aoc_fp:
    zz = [int(theline.rstrip()) for theline in aoc_fp.readlines()]

zz = [int(theline) for theline in zz]

zz = np.array(sorted(zz))

(sum(zz[1:]-zz[0:-1]==1)+1)*(sum(zz[1:]-zz[0:-1]==3)+1)

diffsa = zz[1:]-zz[0:-1]
diffs = np.zeros(len(diffsa)+2)
diffs[1:-1] = diffsa
diffs[0] = 1
diffs[-1] = 3

permutations = {
    0: 1,
    1: 1,
    2: 2,
    3: 4,
    4: 7
}
nperms = 1
therange = 0
for idiff, thediff in enumerate(diffs):
    if thediff == 3:
        nperms *= permutations[therange]
        therange = 0
    else:
        therange+=1

print(nperms)
