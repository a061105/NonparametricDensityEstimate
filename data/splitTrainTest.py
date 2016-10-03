import sys
import random
from math import floor, ceil

try:
    data_fpath = sys.argv[1]
    data_contr_fpath = sys.argv[2]
    test_ratio = float(sys.argv[3])
except IndexError:
    print('python splitTrainTest.py [data] [data.contrast] [test_ratio]')
    exit(0)
except ValueError:
    print('[test_ratio] should between 0 and 1')
    exit(0)
if test_ratio > 1 or test_ratio < 0:
    print('[test_ratio] should between 0 and 1')
    exit(0)

train_ratio = 1.0 - test_ratio

for dpath in [data_fpath, data_contr_fpath]:
    data = list()
    with open(data_fpath) as fpr:
        for line in fpr:
            data.append(line)
    
    N = len(data)
    Ntrain = int(ceil(N*train_ratio))
    Ntest = int(floor(N*test_ratio))
    
    random.shuffle(data)
    with open(dpath+'.tr','w') as fpw:
        for i in range(Ntrain):
            fpw.write(data[i])
    with open(dpath+'.ts','w') as fpw:
        for i in range(Ntrain, Ntrain+Ntest):
            fpw.write(data[i])

