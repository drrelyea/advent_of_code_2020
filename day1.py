import numpy as np
import pandas as pd

with open('/Users/relyea/data/input_day1.txt') as aoc_fp:
    input_data = [theline.strip() for theline in aoc_fp.readlines()]
thedata = np.array([int(theline.split(',')[0]) for theline in input_data])

N = len(thedata)
thesum = np.zeros((N,N))
for aa in range(N):
    for bb in range(aa,N):
        thesum[aa,bb] = thedata[aa]+thedata[bb]

rightsum = np.where(thesum == 2020)
theprod = thedata[rightsum[0][0]]*thedata[rightsum[1][0]]

#

thesum = np.zeros((N,N,N))
for aa in range(N):
    for bb in range(aa,N):
        for cc in range(bb,N):
            thesum[aa,bb,cc] = thedata[aa]+thedata[bb]+thedata[cc]

rightsum = np.where(thesum == 2020)
theprod = thedata[rightsum[0][0]]*thedata[rightsum[1][0]]*thedata[rightsum[2][0]]
