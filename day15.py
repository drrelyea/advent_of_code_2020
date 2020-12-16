zzlist = [0, 3, 6]
zzlist = [5,2,8,16,18,0,1]

key_orated_val_round = {zz: izz for izz,zz in enumerate(zzlist)}
has_been_spoken = set([zz for zz in zzlist[:-1]])
prevspoken = zzlist[-1]
N = 30000000
# N = 2020
for ii in range(len(zzlist)-1, N):
    if ii % 100000 == 0:
        print(ii)
    if prevspoken not in has_been_spoken:
        if ii == N-1:
            print('NOTspoken', prevspoken, ii, 'N', 0)
        currspoken = 0
        has_been_spoken.add(prevspoken)
        key_orated_val_round[prevspoken] = ii
    else:
        if ii == N-1:
            print('   spoken', prevspoken, ii, key_orated_val_round[prevspoken], ii - key_orated_val_round[prevspoken])
        currspoken = ii - key_orated_val_round[prevspoken]
        key_orated_val_round[prevspoken] = ii
    prevspoken = currspoken
