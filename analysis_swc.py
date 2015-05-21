#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import sys
from swc import Swc

argvs = sys.argv
argc  = len(argvs)
if(argc != 2):
    print 'Error : input filename.'
    quit()


def get_hist(data) :
    branch = np.zeros(len(data), np.int32)
    hist = np.zeros(20, np.int32)

    print "Total node=%d" % (len(data))

    for record in data :
        branch[record[6]]+=1

    for record in branch :
        hist[record]+=1

    for i in range(len(hist)) :
        print "%d : %d" % (i,  hist[i])


def print_branch_list(branc_list) :
    for record in branch_list :
        if len(record) != 0 :
            print record

def make_branch_list(data) :
    branch_list = [[]]

    for record in data :
        branch_list.append([int(record[0])])
        branch_list[int(record[0])].append(int(record[6]))

    for record in branch_list :
        if len(record) != 0 :
            if record[1] > 0 :
                branch_list[record[1]].append(record[0])

    return(branch_list)


def reduct1(branch_list) :
    for record in branch_list :
#        print len(record)
        if len(record) == 3 :
            branch_list[record[2]][1] = record[1]
            record[0] = 0

#    make_hist_from_branch_list(branch_list)


def make_hist_from_branch_list(branch_list) :
    hist = np.zeros(20, np.int32)

    for record in branch_list :
        if(len(record)>=2 and record[0]!=0) :
            hist[len(record)-2]+=1

    for i in range(len(hist)) :
        print "%d : %d" % (i,  hist[i])
    


data = np.loadtxt(argvs[1], comments='#')
branch_list = make_branch_list(data)
make_hist_from_branch_list(branch_list)
reduct1(branch_list)
make_hist_from_branch_list(branch_list)

swc = Swc(argvs[1])
#swc.printfile()


#get_hist(data)



