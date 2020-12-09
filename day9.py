# literally as good as you could have done
# you didn't read the instructions well enough - the code should have been a range of only 25
# but whatever - it was fast enough

    import numpy as np
    import pandas as pd
    import re

    with open('/Users/relyea/data/input_day9.txt') as aoc_fp:
        input_data = [int(theline.rstrip()) for theline in aoc_fp.readlines()]

    def isthesum(input_data, total):
        for ii in range(len(input_data)):
            for jj in range(ii, len(input_data)):
                if input_data[ii] + input_data[jj] == total:
                    return True
        return False
    
    for iline in range(25,len(input_data)):
        if not isthesum(input_data[0:iline], input_data[iline]):
            print(input_data[iline])
            break

    maxline = iline
    theval = input_data[maxline]
    
    def find_contiguous_range(input_data, num):
        for iline in range(maxline):
            for jline in range(iline, maxline):
                if sum(input_data[iline:jline]) == num:
                    print(iline,jline)
                    return

    find_contiguous_range(input_data[0:maxline], theval)            

