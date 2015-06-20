#!/usr/bin/env python

import sys
from swc import Swc

argvs = sys.argv
argc  = len(argvs)
if(argc != 3):
    print 'Usage : ./%s (cmp number) (gen swc name)' % (argvs[0])
    quit()

swc = Swc()
swc.genswc(int(argvs[1]))
swc.write(argvs[2])
