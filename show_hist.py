#!/usr/bin/env python

import sys
from swc import Swc

argvs = sys.argv
argc  = len(argvs)

if(argc != 2):
    print 'Usage : ./%s (input_swc)' % (argvs[0])
    quit()

swc = Swc(filename=argvs[1])
swc.show_filename()
swc.show_hist()


