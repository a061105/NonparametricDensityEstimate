import sys
import random

try:
    data_fpath = sys.argv[1]
    num_points = int(sys.argv[2])
except IndexError:
    print('python objApprox.py [data] [num points]')
    exit(0)
except ValueError:
    print('[num points] must be positive integer')
    exit(0)


def parseRange(data_fpath):
    
    dim_range = dict()
    with open(data_fpath) as fpr:
        for line in fpr:
            tokens = line.strip().split()
            for r in range(1,len(tokens)):
                iv_pair = tokens[r].split(":")
                ind = int(iv_pair[0])
                val = float(iv_pair[1])
                
                if ind not in dim_range.keys():
                    dim_range[ind] = [1e300,-1e300]
                lower_upper_pair = dim_range[ind]
                
                if val < lower_upper_pair[0]:
                    lower_upper_pair[0] = val
                if val > lower_upper_pair[1]:
                    lower_upper_pair[1] = val
                
    return dim_range


def is_all_between_0_1(dim_range):
    cum = True
    for lower, upper in dim_range.values():
        cum &= (lower>=0.0 and upper<=1.0)
    return cum

def uniform(dim_range):
    x = dict()
    for k in dim_range.keys():
        l, u = dim_range[k]
        x[k] = random.uniform(l,u)
    return x

def write_x(fpw, x):
    fpw.write('0')
    for k in sorted(x.keys()):
        fpw.write(' '+str(k)+':{:.4f}'.format(x[k]))


#finding range of each dimension
dim_range = parseRange(data_fpath)
if is_all_between_0_1(dim_range):
    for ind in dim_range.keys():
        dim_range[ind] = [0.0,1.0]

#generate and write contrastive data
with open(data_fpath+'.contrast','w') as fpw:
    for i in range(0,num_points):
        x = uniform(dim_range)
        write_x(fpw, x)
        fpw.write('\n')
