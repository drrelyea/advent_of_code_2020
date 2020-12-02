import numpy as np
import pandas as pd

with open('/Users/relyea/data/input_day2.txt') as aoc_fp:
    input_data = [theline.rstrip() for theline in aoc_fp.readlines()]
thedata = np.array([theline.split(' ') for theline in input_data])

# 8 minutes

N = len(thedata)
Nvalid = 0
for idata, datum in enumerate(thedata):
    thevar = datum[1][0]
    lowend = int(datum[0].split('-')[0])
    highend = int(datum[0].split('-')[1])
    thenum = datum[2].count(thevar)
    if not (thenum < lowend or thenum > highend):
        Nvalid += 1
    # print(lowend, highend,  thenum, Nvalid)

print(Nvalid)

# 4 minutes

Nvalid = 0
for idata, datum in enumerate(thedata):
    thevar = datum[1][0]
    lowend = int(datum[0].split('-')[0]) - 1
    highend = int(datum[0].split('-')[1]) - 1
    thenum = datum[2].count(datum[1][0])
    loexists = datum[2][lowend] == thevar
    hiexists = datum[2][highend] == thevar
    if loexists != hiexists:
        if loexists or hiexists:
            Nvalid += 1
    print(thevar, lowend, highend,  thenum, loexists, hiexists)

print(Nvalid)

#

