# literally as good as you could have done
# you didn't read the instructions well enough - the code should have been a range of only 25
# but whatever - it was fast enough
# I couldn't have done this faster without faster fingers
# I also lost a minute in the download

import numpy as np
import pandas as pd
import re
import os
import urllib

theday = '9'
aoc_filename = '/Users/relyea/data/input_day'+theday+'.txt'
if not os.path.exists(aoc_filename):
    urllib.request.urlretrieve('https://adventofcode.com/2020/day/'+theday+'/input', aoc_filename)
    

with open('/Users/relyea/data/input_day9.txt') as aoc_fp:
    zz = [int(theline.rstrip()) for theline in aoc_fp.readlines()]

zz = [int(theline) for theline in zz]

def isthesum(inp, total):
    for ii in range(len(inp)):
        for jj in range(ii, len(inp)):
            if inp[ii] + inp[jj] == total:
                return True
    return False

for iline in range(25,len(zz)):
    if not isthesum(zz[iline-25:iline], zz[iline]):
        print(zz[iline])
        break

maxline = iline
theval = zz[maxline]

def find_contiguous_range(inp, num):
    for iline in range(maxline):
        for jline in range(iline, maxline):
            if sum(inp[iline:jline]) == num:
                print(iline,jline)
                return

find_contiguous_range(zz[0:maxline], theval)            

