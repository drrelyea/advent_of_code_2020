import numpy as np
import pandas as pd
import re
import os
import urllib
from copy import deepcopy
with open('/Users/relyea/data/input_day13.txt') as aoc_fp:
    zz = [theline.rstrip() for theline in aoc_fp.readlines()]

# start = int(zz[0])
# times = sorted([int(aa) for aa in zz[1].split(',') if aa!='x'])

# mindiff = 104304320432
# for time in times:
#     nextone = (start//time + 1)*time - start
#     if nextone < mindiff:
#         mindiff = nextone
#         besttime = time


# part 2

def modInverse(a, m): 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1): 
        return 0
  
    while (a > 1): 
  
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
    # Make x positive 
    if (x < 0): 
        x = x + m0 
  
    return x 
  

alltimes = zz[1].split(',')
times = {}
for itime, time in enumerate(alltimes):
    if time!='x':
        times[int(time)] = itime

# times = {aa:bb for bb,aa in enumerate([67,7,59,61])}

numsum = 0
fullprod = np.prod(list(times.keys()))
for time, delay in times.items():
    prod = 1
    for tt, dd in times.items():
        if tt != time:
            prod *= tt
    inv = modInverse(prod, time)
    numsum += (time - delay)*prod*inv
print(((numsum % fullprod) + fullprod) % fullprod)

# 67,7,59,61 is 754018

# 67,7,x,59,61 is 1261476
