with open('/Users/relyea/data/input_day14.txt') as aoc_fp:
    zz = [theline.rstrip() for theline in aoc_fp.readlines()]

# zz = [
#     'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
#     'mem[8] = 11',
#     'mem[7] = 101',
#     'mem[8] = 0'
# ]

# def to_bytes(num):
#     bytesarr = []
#     for ii in range(36):
#         bytesarr.append((num >> ii) % 2)
#     return bytesarr

# def to_int(blist):
#     outnum = 0
#     for ii, bb in enumerate(blist):
#         outnum += 2**ii * int(bb)
#     return outnum

# def applymask(blist, currmask):
#     outlist = []
#     for bb, mm in zip(blist, currmask):
#         if mm != 'X':
#             outlist.append(int(mm))
#         else:
#             outlist.append(bb)
#     return outlist

# currmask = ''
# memdict = {}
# for line in zz:
#     if line.startswith("mask = "):
#         currmask = [xx for xx in line[7:][::-1]]
#     else:
#         dictindex = int(line.split('[')[1].split(']')[0])
#         origval = int(line.split(" = ")[1])
#         memdict[dictindex] = to_int(applymask(to_bytes(origval), currmask))


# PART 2
# zz = [
#     'mask = 000000000000000000000000000000X1001X',
#     'mem[42] = 100',
#     'mask = 00000000000000000000000000000000X0XX',
#     'mem[26] = 1'
# ]

def to_bytes(num):
    bytesarr = []
    for ii in range(36):
        bytesarr.append((num >> ii) % 2)
    return bytesarr

def to_int(blist):
    outnum = 0
    for ii, bb in enumerate(blist):
        outnum += 2**ii * int(bb)
    return outnum

def applymask(blist, currmask):
    outlist = []
    for bb, mm in zip(blist, currmask):
        if mm == '0':
            outlist.append(str(bb))
        else:
            outlist.append(mm)
    return outlist

def get_indices(index):
    indices_to_modify = [ii for ii,vv in enumerate(index) if vv == 'X']
    # print("i2m", indices_to_modify)
    for qq in range(2**len(indices_to_modify)):
        new_index_bits = to_bytes(qq)
        # print("nib", new_index_bits)
        newbits = [vv for vv in index]
        for inib, i2m in enumerate(indices_to_modify):
            newbits[i2m] = new_index_bits[inib]
        yield newbits

currmask = ''
memdict = {}
for line in zz:
    if line.startswith("mask = "):
        currmask = [xx for xx in line[7:][::-1]]
    else:
        dictindex = int(line.split('[')[1].split(']')[0])
        wide_dict_index = applymask(to_bytes(dictindex), currmask)
        # print("mask", currmask)
        # print("wdi", wide_dict_index)
        origval = int(line.split(" = ")[1])
        for theindex in get_indices(wide_dict_index):
            # print(to_int(theindex))
            memdict[to_int(theindex)] = origval
