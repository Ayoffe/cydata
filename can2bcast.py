import pandas as pd
import numpy as np
import sys

df2 = pd.DataFrame(np.random.randint(low=0, high=10, size=(5, 5)), columns=['a', 'b', 'c', 'd', 'e'])
# train = pd.read_csv(sys.argv[1])
train = pd.read_pickle(sys.argv[1]+".pcl")



test =  10




BUSNUM=6
_BC_WND = 0.0004 * 10^9

_ID2TM = dict()
_i = test
for _indx, r in train.iterrows():
    _idT = _ID2TM.setdefault(r['id'], [0]*BUSNUM)
    ts = r['ts']
    _idT[int(r['busID'])] = (_indx, ts)
    [_ts for _i,_ts in _idT if ts - _ts < _BC_WND]
    print(_indx, r['ts'])
    if not _i:
        break
    _i -= 1

_i = test
for _indx in reversed(train.index):
    r = train.loc[_indx]
    print(_indx, r['ts'])
    if not _i:
        break
    _i -= 1

# print(train.columns)
# print(train.all(axis=))
# strain = train.sample(100)
# train
#
# print(strain)