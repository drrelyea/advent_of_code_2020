import numpy as np

with open('/Users/relyea/data/input_day17.txt') as aoc_fp:
    zz = [[int(xx) for xx in theline.rstrip().replace('#','1,').replace('.','0,')[0:15].split(',')] for theline in aoc_fp.readlines()]
zz = np.array(zz)

# zz = [
#     '.#.',
#     '..#',
#     '###'
# ]
# zz = [[int(xx) for xx in theline.rstrip().replace('#','1,').replace('.','0,')[0:5].split(',')] for theline in zz]
# zz = np.array(zz)
zz = zz[:,:,np.newaxis,np.newaxis]

for cyc in range(6):
    newzz = np.zeros((zz.shape[0]+2,zz.shape[1]+2,zz.shape[2]+2,zz.shape[3]+2))
    newzz[1:-1,1:-1,1:-1,1:-1] = zz
    newzzcopy = newzz.copy()
    for izx in range(newzz.shape[0]):
        for izy in range(newzz.shape[1]):
            for izz in range(newzz.shape[2]):
                for iza in range(newzz.shape[3]):
                    nnact = 0
                    for ii in (-1,0,1):
                        if izx + ii < 0 or izx + ii == newzz.shape[0]:
                            continue
                        for jj in (-1,0,1):
                            if izy + jj < 0 or izy + jj == newzz.shape[1]:
                                continue
                            for kk in (-1,0,1):
                                if izz + kk < 0 or izz + kk == newzz.shape[2]:
                                    continue
                                for mm in (-1,0,1):
                                    if iza + mm < 0 or iza + mm == newzz.shape[3]:
                                        continue
                                    if ii==jj==kk==mm==0:
                                        continue                            
                                    nnact += newzz[izx+ii, izy+jj, izz+kk, iza+mm]
                    # print(izx,izy,nnact)
                    if newzz[izx,izy,izz,iza] == 1:
                        newzzcopy[izx,izy,izz,iza] = int(nnact == 2 or nnact == 3)
                    else:
                        newzzcopy[izx,izy,izz,iza] = int(nnact == 3)
    zz= newzzcopy

# zz = zz[:,:,np.newaxis]
# for cyc in range(6):
#     newzz = np.zeros((zz.shape[0]+2,zz.shape[1]+2,zz.shape[2]+2))
#     newzz[1:-1,1:-1,1:-1] = zz
#     newzzcopy = newzz.copy()
#     for izx in range(newzz.shape[0]):
#         for izy in range(newzz.shape[1]):
#             for izz in range(newzz.shape[2]):
#                 nnact = 0
#                 for ii in (-1,0,1):
#                     if izx + ii < 0 or izx + ii == newzz.shape[0]:
#                         continue
#                     for jj in (-1,0,1):
#                         if izy + jj < 0 or izy + jj == newzz.shape[1]:
#                             continue
#                         for kk in (-1,0,1):
#                             if izz + kk < 0 or izz + kk == newzz.shape[2]:
#                                 continue
#                             if ii==jj==kk==0:
#                                 continue                            
#                             nnact += newzz[izx+ii, izy+jj, izz+kk]
#                 # print(izx,izy,nnact)
#                 if newzz[izx,izy,izz] == 1:
#                     newzzcopy[izx,izy,izz] = int(nnact == 2 or nnact == 3)
#                 else:
#                     newzzcopy[izx,izy,izz] = int(nnact == 3)
#     zz= newzzcopy
