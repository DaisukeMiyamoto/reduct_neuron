#!/usr/bin/env python

#import numpy as np
#import matplotlib.pyplot as plt
import sys
from swc import Swc

argvs = sys.argv
argc  = len(argvs)
if(argc != 3):
    print 'Usage : ./%s (input_swc) (output_swc)' % (argvs[0])
    quit()

swc = Swc(argvs[1])
#swc.show_hist()
org = swc.size_of_data()
swc.reduct2()
#swc.show_hist()
swc.reduct1()
final = swc.size_of_data()
#swc.show_hist()

swc.write(argvs[2])

print "%d -> %d" % (org, final)
