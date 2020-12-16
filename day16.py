with open('/Users/relyea/data/input_day16.txt') as aoc_fp:
    zz = [theline.rstrip() for theline in aoc_fp.readlines()]

# zz = [
#     'class: 1-3 or 5-7',
#     'row: 6-11 or 33-44',
#     'seat: 13-40 or 45-50',
#     '',
#     'your ticket:',
#     '7,1,14',
#     '',
#     'nearby tickets:',
#     '7,3,47',
#     '40,4,50',
#     '55,2,20',
#     '38,6,12'
# ]


# zz = [
#     'class: 0-1 or 4-19',
#     'row: 0-5 or 8-19',
#     'seat: 0-13 or 16-19',
#     '',
#     'your ticket:',
#     '11,12,13',
#     '',
#     'nearby tickets:',
#     '3,9,18',
#     '15,1,5',
#     '5,14,9',
# ]

rules = {}
for line in zz:
    if 'or' in line:
        key = line.split(": ")[0]
        ranges = line.split(": ")[1].split(" or ")
        rangelist = []
        for therange in ranges:
            rangelist.append((int(therange.split('-')[0]),int(therange.split('-')[1])))
        rules[key] = rangelist

def get_possible_rules(num):
    possiblelist = []
    # print(icol, numstr)
    num = int(numstr)
    for key in rules:
        for subrule in rules[key]:
            if subrule[0] <= num <= subrule[1]:
                # print(key, rules[key])
                possiblelist.append(key)
    return possiblelist

grabnext = False
possiblerules = {}
extendedpossiblerules = {}
graballfollowing = False
invalidsum = 0
validlines = []
for iline,line in enumerate(zz):
    if grabnext:
        validlines.append(line)
        myticket = line
        for icol, numstr in enumerate(line.split(',')):
            possiblerules[icol] = get_possible_rules(numstr)
        grabnext = False
    if graballfollowing:
        # print('newline')
        lineisvalid = True
        for icol, numstr in enumerate(line.split(',')):
            possiblelist = []
            # print('newsplit', icol, numstr)
            num = int(numstr)
            isvalid = False
            for key in possiblerules[icol]:
                # print(num, rules[key])
                for subrule in rules[key]:
                    if subrule[0] <= num <= subrule[1]:
                        # print(key, rules[key], 'passed')
                        isvalid = True
            if not isvalid:
                invalidsum += num
                lineisvalid = False
        if lineisvalid:
            validlines.append(line)
        else:
            print(line)


    if 'your ticket' in line:
        grabnext = True
        continue
    if 'nearby' in line:
        graballfollowing = True
print(invalidsum)

goodrules = {}
for icol in range(len(possiblerules)):
    goodrules[icol] = []
    for rulestr,rulelist in rules.items():
        rulegood = True
        for line in validlines:
            num = int(line.split(',')[icol])
            linegood = False
            for subrule in rulelist:
                if subrule[0] <= num <= subrule[1]:
                    linegood = True
            if not linegood:
                rulegood = False
                break
        if rulegood:
            goodrules[icol].append(rulestr)

popthese = []
finalrules = {}
while True:
    allsorted = True
    for icol,rulelist in goodrules.items():
        if len(rulelist) == 1:
            finalrules[icol] = rulelist[0]
            popthese.append(rulelist[0])
    if len(popthese) == 0:
        break
    print(popthese)
    for poprule in popthese:
        for icol,rulelist in goodrules.items():
            if poprule in rulelist:
                # print('b4',goodrules[icol])
                rulelist.remove(poprule)
                # print('f2',goodrules[icol])
    print(finalrules)
    popthese = []

theprod = 1
myticketlist = [int(aa) for aa in myticket.split(',')]
for icol,rule in finalrules.items():
    if rule.startswith('departure'):
        theprod *= myticketlist[icol]
print(theprod)
