import numpy as np
import pandas as pd
import re

with open('/Users/relyea/data/input_day6.txt') as aoc_fp:
    input_data = [theline.rstrip() for theline in aoc_fp.readlines()]

input_data = [qq for qq in ' '.join(input_data).split('  ')]


n_tot = 0
for ii in input_data:
    # n_tot += len(set(ii.replace(' ',"")))
    n_tot += len(set.intersection(*[set(group) for group in ii.split(" ")]))
