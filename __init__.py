import os, sys
from vcd import VCDWriter
# from bundle import Bundle
from datetime import datetime
# import numpy
# import pandas as pd
import csv

DUMP = """
date Mon Jun 4 12:04:42.117 pm 2018
base dec  timestamps absolute
internal events logged
// version 11.0.0
//1344.432809 previous log file: Logging.asc
1344.432878 5  469744131x      Rx   d 8 135 129  24  62 177   0 240   1  Length = 273726 BitCount = 141 ID = 469744131x
1344.433001 CANFD   2 Rx         fc  ESC_51                           1 0 e 48 67 ce ff 00 7e 00 40 06 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   299015  524   323000 c81a7d76 50a00150 46280150 20001f7e 20000b1a
1344.433013 3  1003            Rx   d 8 225 254   0  76   0   0   7   0  Length = 235988 BitCount = 122 ID = 1003
1344.433111 CANFD   2 Rx         a8  Motor_12                         1 0 8  8 ad 69 1e cf 95 64 fe 0f   102031  130   323000 b0011297 50a00150 46280150 20001f7e 20000b1a
1344.433112 5  168             Rx   d 8 173 105  30 207 149 100 254  15  Length = 225972 BitCount = 117 ID = 168
1344.433139 6  263             Rx   d 8   0   0   0  86   1  20 157 235  Length = 231910 BitCount = 120 ID = 263
1344.433224 CANFD   2 Rx         fd  ESP_21                           1 0 8  8 5b dd 1f 00 00 00 04 00   104531  135   323000 c8007911 50a00150 46280150 20001f7e 20000b1a
1344.433253 3  263             Rx   d 8   0   0   0  86   1  20 157 235  Length = 231988 BitCount = 120 ID = 263
1344.433361 5  178             Rx   d 8   0   0   0   0   0   0   0   0  Length = 240093 BitCount = 124 ID = 178
1344.433380 CANFD   1 Rx         fc  ESC_51                           1 0 e 48 67 ce ff 00 7e 00 40 06 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   299265  524   303000 c81a7d76 46500250 4b280150 20011736 2000091c
1344.433387 6  327             Rx   d 8   0   0   0   0 240   3   0   0  Length = 239910 BitCount = 124 ID = 327
1344.433388 CANFD   4 Rx         fc  ESC_51                           1 0 e 48 67 ce ff 00 7e 00 40 06 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   299265  524   303000 c81a7d76 46500250 4b280150 20011736 2000091c
1344.433493 CANFD   1 Rx         fd  ESP_21                           1 0 8  8 5b dd 1f 00 00 00 04 00   104750  135   323000 c8007911 46500250 4b280150 20011736 2000091c
1344.433499 3  305             Rx   d 8   0   0   0 254   0 254 223 255  Length = 237988 BitCount = 123 ID = 305
1344.433501 CANFD   4 Rx         fd  ESP_21                           1 0 8  8 5b dd 1f 00 00 00 04 00   104765  135   323000 c8007911 46500250 4b280150 20011736 2000091c
1344.433532 CANFD   2 Rx        102  ESC_50                           1 0 e 48 73 5d ff 03 02 ff 3f 00 00 00 64 00 00 00 00 00 00 00 00 00 00 e0 0f 00 00 00 00 00 00 f0 ff 00 00 20 00 00 e6 00 00 00 01 00 00 00 00 00 00 00   293531  513   303000 a80442d5 50a00150 46280150 20001f7e 20000b1a
1344.433603 5  253             Rx   d 8  91 221  31   0   0   0   4   0  Length = 233972 BitCount = 121 ID = 253
1344.433629 6  253             Rx   d 8  91 221  31   0   0   0   4   0  Length = 233910 BitCount = 121 ID = 253
1344.433642 CANFD   2 Rx         ec  EBKV_02                          1 0 8  8 a8 1a 00 00 7e 40 a1 0f   101531  132   323000 a80042eb 50a00150 46280150 20001f7e 20000b1a
1344.433741 3  253             Rx   d 8  91 221  31   0   0   0   4   0  Length = 233972 BitCount = 121 ID = 253
1344.433753 CANFD   2 Rx        105  VMM_01                           1 0 8  8 eb 0d 10 00 31 02 00 00   103531  133   323000 e00113e4 50a00150 46280150 20001f7e 20000b1a
1344.433843 5  263             Rx   d 8   0   0   0  86   1  20 157 235  Length = 232093 BitCount = 120 ID = 263
1344.433873 6  257             Rx   d 8 115  93 255   3   2 255  63   0  Length = 227910 BitCount = 118 ID = 257
1344.433910 CANFD   2 Rx   17f0003bx KN_EBKV                          1 0 8  8 20 00 00 00 00 14 00 80   148531  160   323000 e001463d 50a00150 46280150 20001f7e 20000b1a
1344.433925 CANFD   1 Rx        102  ESC_50                           1 0 e 48 73 5d ff 03 02 ff 3f 00 00 00 64 00 00 00 00 00 00 00 00 00 00 e0 0f 00 00 00 00 00 00 f0 ff 00 00 20 00 00 e6 00 00 00 01 00 00 00 00 00 00 00   293765  513   303000 a80442d5 46500250 4b280150 20011736 2000091c
1344.433932 CANFD   4 Rx        102  ESC_50                           1 0 e 48 73 5d ff 03 02 ff 3f 00 00 00 64 00 00 00 00 00 00 00 00 00 00 e0 0f 00 00 00 00 00 00 f0 ff 00 00 20 00 00 e6 00 00 00 01 00 00 00 00 00 00 00   293765  513   303000 a80442d5 46500250 4b280150 20011736 2000091c
1344.433978 3  257             Rx   d 8 115  93 255   3   2 255  63   0  Length = 227972 BitCount = 118 ID = 257
"""



_date = 'today'
_base = ''

# for _ln in DUMP.split("\n"):


BUSES = dict()

trace = None
dump = None


_b_vcd = None
try:
    _b_vcd = sys.argv.index('/vcd')
    sys.argv.pop(_b_vcd)
except:
    print("-- No vcd created")

_csv_file = sys.argv[2] + ".csv"
_in_file = sys.argv[1]

#"  91.330607 6  ErrorFrame	Flags = 65534	CodeExt = 8306	Code = 129	ID = 958	DLC = 8	Position = 106	Length = 230125	Data = 125  15  231  5  66  64  12  128"
with open(_csv_file, 'w+') as _fo:
    # dump = csv.writer(_fo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    dump = csv.DictWriter(_fo, fieldnames=["ts", "fb", "busID", "id", "dlc", ] + ["i%d" % _i for _i in xrange(64)] + ["e_flags", "e_code", "e_codeext", "e_pos"], delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    dump.writeheader()

    for _I in range(2 if _b_vcd else 1):
        print("_I:", _I)
        if _I == 0:
            print("Write csv: " + _csv_file)

        with open(_in_file, 'r') as _fi:
            for _ln in _fi:
                _ln = _ln.strip()
                if not _ln:
                    continue
                if _ln.startswith('//'):
                    continue

                _ll = _ln.split()

                if _ln.startswith('date'):
                    if _I == 0:
                        _date = _ln[len('date '):]

                        _tm = ' '.join(_ll[1:])
                        _trig_date = datetime.strptime(_tm, "%a %b %d %H:%M:%S.%f %p %Y")

                        _fn = "{pref}_{ts}.vcd".format(pref=sys.argv[2], ts=int((_trig_date - datetime(1970, 1, 1)).total_seconds()))
                        trace = VCDWriter(open(_fn, 'w+'), timescale='1 us', date=_tm)

                        print ("Write vcd:", _fn)


                        print (_trig_date)
                    continue

                if _ln.startswith('base'):
                    _base = _ln[len('base '):]
                    continue
                if _ln.startswith('internal'):
                    _internal = _ln[len('internal '):]
                    continue
                if _ln.startswith('Begin'):
                    # _tm = ' '.join(_ll[2:])
                    # _trig_date = datetime.strptime(_tm, "%a %b %d %H:%M:%S.%f %p %Y")
                    #
                    #
                    # if trace:
                    #     pass
                    # _fn = "{pref}_{ts}.vcd".format(pref=sys.argv[2], ts=(_trig_date - datetime(1970, 1,1)).total_seconds())
                    # trace = VCDWriter(open(_fn, 'w+'), timescale='1 us', date=_tm)
                    # print _trig_date
                    continue
                if _ln.startswith('End'):
                    print (_ln)
                    continue


                # print _ll
                r = None
                _ts = int(float(_ll[0]) * 1000000)

                if _ll[1].startswith('Start'):
                    _start_ts = _ts
                    continue

                _rxtx = _ll[3]
                # _errfrm = _ll[4] == 'ErrorFrame'
                # if _errfrm:
                #     continue

                if _ll[1] == 'CANFD':
                    if _ln[38] == ' ':
                        _ll.insert(5, '---')
# """
#   82.355165 CANFD   1 Rx   ErrorFrame Stuff Error                                      fffe 82     20aa Data 104       f6  1 0 d 32 19 85 fd df ff f2 5e ff 03 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    81328       1b 98000000 46500250 4b280150 20011736 2000091c
#   ...
#   82.355417 CANFD   1 Rx         f6  Motor_55                         1 0 d 32 19 85 fd df ff f2 5e ff 03 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   218187  365   303000 98187851 46500250 4b280150 20011736 2000091c
# """
                    if _ll[4]=='ErrorFrame':
                        r = dict(rxtx=_rxtx, ts=_ts, fb=1, bus_type='CANFD',
                                 e_flags=int(_ll[7], 16), e_code=int(_ll[8], 16), e_codeext=int(_ll[9],  16), e_pos=int(_ll[11]),
                                 busID=_ll[2], id=int(_ll[12].rstrip('x'), 16), id_hex=_ll[12].rstrip('x'), id_desc=_ll[12],
                                 ctl=_ll[13:13 + 3], dlc=int(_ll[16]),
                                 data=[int(_d, 16) for _d in _ll[17:17 + int(_ll[16])]])
                        # import pprint
                        # pprint.pprint(r)
                    else:
                        r = dict(rxtx=_rxtx, ts=_ts, fb=1, bus_type='CANFD',
                                e_flags=0, e_code=0, e_codeext=0, e_pos=0,
                                busID=_ll[2], id=int(_ll[4].rstrip('x'), 16), id_hex=_ll[4].rstrip('x'), id_desc=_ll[5],
                                ctl=_ll[6:6+3], dlc=int(_ll[9]), data=[int(_d, 16) for _d in _ll[10:10 + int(_ll[9])]])

                else:
                    if _ll[3].startswith('Status'):
                        continue
                    if _ll[2].startswith('Statistic'):
                        continue
                    # "   0.520549 6  ErrorFrame	Flags = 65534	CodeExt = 8306	Code = 129	ID = 960	DLC = 4	Position = 74	Length = 164140	Data = 116  0  3  0"
                    if _ll[2].startswith("ErrorFrame"):
                        r = dict(rxtx='Rx', ts=_ts, fb=1, bus_type='CAN', busID=_ll[1],
                                 e_flags=int(_ll[5]), e_codeext=int(_ll[8]), e_code=int(_ll[11]), e_pos=int(_ll[20]),
                                 id=int(_ll[14].rstrip('x')), id_hex=hex(int(_ll[14].rstrip('x'))), id_desc=_ll[14],
                                 ctl=[0], dlc=int(_ll[17]), data=[int(_d) for _d in _ll[26:26+int(_ll[17])]])

                    else:
                        r = dict(rxtx=_rxtx, ts=_ts, fb=0, bus_type='CAN', busID=_ll[1],
                            e_flags=0, e_code=0, e_codeext=0, e_pos=0,
                            id=int(_ll[2].rstrip('x')), id_hex=hex(int(_ll[2].rstrip('x'))), id_desc=_ll[2],
                            ctl=_ll[4:4+1], dlc=int(_ll[5]), data=[int(_d) for _d in  _ll[6:6 + int(_ll[5])]])


                _i = 0
                for _r in r['data']:
                    r["i%d" % _i] = _r
                    _i +=1
                    # r["i%d" & _i] = _r

                _bName = r['bus_type'] + "_" + r['busID']
                _bID = str(r['id'])
                _name = _bName + "." + _bID

                if _I == 0:
                    # _c = COLS.setdefault(_bName, {})
                    # _v = _c.setdefault(_bID, [0])
                    # _v[0] +=1
                    # dump.writerow(["TS", "BUS", "BUS_DESC", "ID", "ID_DESC", "VAL"])
                    dump.writerow({_k:_v for _k,_v in r.iteritems() if _k in dump.fieldnames})
                    _fo.flush()

                    _l = BUSES.setdefault(_name, [])
                    if not _l:
                        trace.set_scope_type(r['busID'], 'module')
                        _l.append(trace.register_var(r['busID'], _name,'reg', (8, ) * r['dlc'], (0, ) * r['dlc']))

                elif _I == 1:
                    _val = r['data']

                    _dd = [_l[0], _ts, _val[:]]

                    try:
                        trace.change(*_dd)
                    except:
                        print(_dd)
                    trace.flush(_dd[1])
                else:
                    assert False

if trace:
    trace.close()
