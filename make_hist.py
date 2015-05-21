#!/bin/python

import numpy as np
import matplotlib.pyplot as plt
import sys

argvs = sys.argv
argc  = len(argvs)

if(argc != 2):
    print 'Error : input filename.'
    quit()


data = np.loadtxt(argvs[1], comments='#')

branch = np.zeros(len(data), np.int32)

print "Total node=%d" % (len(data))

for record in data :
#    print record[6]
    branch[record[6]]+=1

hist = np.zeros(20, np.int32)

for record in branch :
#    print record
    hist[record]+=1

for i in range(len(hist)) :
    print "%d : %d" % (i,  hist[i])

