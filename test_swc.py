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

swc = Swc(argvs[1])
#swc.show()
swc.show_hist()


