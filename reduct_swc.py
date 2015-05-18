import numpy as np
import matplotlib.pyplot as plt
import sys

argvs = sys.argv
argc  = len(argvs)

if(argc != 2):
    print 'Error : input filename.'
    quit()


#data = np.loadtxt('./test.swc', comments='#', skiprows=3)
data = np.loadtxt(argvs[1], comments='#')

print data



