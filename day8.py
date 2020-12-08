import numpy as np
import pandas as pd
import re

with open('/Users/relyea/data/input_day8.txt') as aoc_fp:
    input_data = [theline.rstrip() for theline in aoc_fp.readlines()]


thelist = np.zeros(len(input_data))

stillzero = True
ind = 0
accum = 0
while stillzero:
    theop = input_data[ind][0:3]
    if thelist[ind] != 0:
        break
    else:
        thelist[ind] = 1
    if theop == 'jmp':
        ind += int(input_data[ind].split(' ')[1])
    elif theop == 'nop':
        ind += 1
    elif theop == 'acc':
        accum += int(input_data[ind].split(' ')[1])
        ind += 1


ido = input_data.copy()
for instruction in range(len(input_data)):
    input_data = ido.copy()
    if input_data[instruction][0:3] == 'jmp':
        input_data[instruction] = 'nop' + input_data[instruction][3:]
    elif input_data[instruction][0:3] == 'nop':
        input_data[instruction] = 'jmp' + input_data[instruction][3:]
    else:
        continue
    thelist = np.zeros(len(input_data))
    stillzero = True
    ind = 0
    accum = 0
    while stillzero:
        theop = input_data[ind][0:3]
        if thelist[ind] != 0:
            break
        else:
            thelist[ind] = 1
        if theop == 'jmp':
            ind += int(input_data[ind].split(' ')[1])
        elif theop == 'nop':
            ind += 1
        elif theop == 'acc':
            accum += int(input_data[ind].split(' ')[1])
            ind += 1
        if ind >= len(input_data):
            print(accum)
            assert(False)