# I apoarently suck at recognizing a recursion problem
# however, my code works in the cyclic case as well
# BUT I should have used recursion and recognized that the problem should terminate
# I also don't have anywhere the regex chops to do this gently
# I lost a LOT of time on the basic munging and on the logic of what was internally contained
# I cannot easily debug list comprehensions, so I should avoid them for this
# also the part boundaries are a little artificial, so I should have just done both containers from the start


import numpy as np
import pandas as pd
import re

with open('/Users/relyea/data/input_day7.txt') as aoc_fp:
    input_data = [theline.rstrip() for theline in aoc_fp.readlines()]

# input_data = [
#     'light red bags contain 1 bright white bag, 2 muted yellow bags.',
#     'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
#     'bright white bags contain 1 shiny gold bag.',
#     'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
#     'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
#     'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
#     'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
#     'faded blue bags contain no other bags.',
#     'dotted black bags contain no other bags.',
# ]

bagdict = {line.split(" contain ")[0]:line.split(" contain ")[1] for line in input_data if "no other bags" not in line.split(" contain ")[1]}

container_bags = set(["shiny gold bag"])
csize = len(container_bags)
diff = 1
while diff > 0:
    newlist = []
    for key in bagdict:
        jj = [(outbag, outbag in bagdict[key]) for outbag in container_bags]
        qq = [thebag[0] for thebag in jj if thebag[1]]
        bb = [thebag[1] for thebag in jj]
        if any(bb):
            print(key, bagdict[key], qq, container_bags)
            newlist.append(key)
    for bag in newlist:
        if bag.endswith('s'):        
            container_bags.add(bag[:-1])
        else:
            container_bags.add(bag)
    diff = len(container_bags) - csize
    csize = len(container_bags)
    # rrr = input()


def remove_trailing_s(phrase):
    if phrase.endswith('.'):
        phrase = phrase[:-1]
    if phrase.endswith('s'):
        phrase = phrase[:-1]
    return phrase

def split_bag_and_number(bagnum):
    if bagnum == "no other bag":
        return (0, "otherbags")
    print(bagnum)
    split = bagnum.split(" ")
    return (int(split[0]), " ".join(split[1:]))

bagdict = {remove_trailing_s(line.split(" contain ")[0]):line.split(" contain ")[1] for line in input_data}

bagcountdict = {key: [split_bag_and_number(remove_trailing_s(subval)) for subval in val.split(', ')] for key,val in bagdict.items()}

bagcount = {}
for key in bagcountdict:
    if len(bagcountdict[key]) == 1 and bagcountdict[key][0][0] == 0:
        bagcount[key] = 1
    else:
        bagcount[key] = -1
print("bgd", bagcount)

allpositive = all([val > 0 for val in bagcount.values()])
while not allpositive:
    for key,val in bagcountdict.items():
        contained_bags = [subval[1] for subval in val]
        print("cbb", contained_bags)
        if all([bagcount[cbag] > 0 for cbag in contained_bags if cbag != "otherbags"]):
            bagcount[key] = 1
            for num, cbag in val:
                if cbag != "otherbags" and num>0 and bagcount[cbag] > 0:
                    bagcount[key] += bagcount[cbag]*num
            print("CHANGING: ", key, val, bagcount[key])
    allpositive = all([val > 0 for val in bagcount.values()])
    print("bgd", bagcount)
