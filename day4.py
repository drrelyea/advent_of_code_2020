import numpy as np
import pandas as pd
import re

with open('/Users/relyea/data/input_day4.txt') as aoc_fp:
    input_data = [theline.rstrip() for theline in aoc_fp.readlines()]

input_data = [qq for qq in ' '.join(input_data).split('  ')]

new_passport = True
req_fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]

def field_value_does_not_conform(field, passport_value):
    if field == 'byr':
        return len(passport_value) !=4 or int(passport_value) < 1920 or int(passport_value) > 2002
    if field == 'iyr':
        return len(passport_value) !=4 or int(passport_value) < 2010 or int(passport_value) > 2020
    if field == 'eyr':
        return len(passport_value) !=4 or int(passport_value) < 2020 or int(passport_value) > 2030
    if field == 'hgt':
        return (
            passport_value[-2:] != 'cm' and passport_value[-2:] != 'in'
        ) or (
            passport_value[-2:] == 'cm' and (int(passport_value[:-2]) < 150 or int(passport_value[:-2]) > 193)
        ) or (
            passport_value[-2:] == 'in' and (int(passport_value[:-2]) < 59 or int(passport_value[:-2]) > 76)
        )
    if field == 'hcl':
        return len(passport_value) != 7 or re.search('\#[a-f0-9]{6}', passport_value) is None
    if field == 'ecl':
        return not any([qq in passport_value for qq in ['amb','blu','brn','gry','grn','hzl','oth']])
    if field == 'pid':
        return len(passport_value) != 9 or re.search('[0-9]{9}', passport_value) is None

def check_valid(passport):
    passport_valid = True
    for field in req_fields:
        if field not in passport or field_value_does_not_conform(field, passport[field]):
            passport_valid = False
    return passport_valid

passport = {}
n_valid =0 
for line in input_data:
    if check_valid({aa.split(':')[0]: aa.split(':')[1] for aa in line.split(' ')}):
        n_valid += 1
