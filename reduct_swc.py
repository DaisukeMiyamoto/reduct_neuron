#!/usr/bin/env python

import sys
from swc import Swc

argvs = sys.argv
argc  = len(argvs)
if(argc != 2):
    print 'Usage : ./%s (input_swc)' % (argvs[0])
    quit()


filename = argvs[1]
swc = Swc(filename=argvs[1])
org = swc.size_of_data()

filename1 = filename.replace('.', '-1.', 1)
print 'Generating %s' % filename1
swc.reduct1()
swc.write(filename1)

filename2 = filename1.replace('.', '-2.', 1)
print 'Generating %s' % filename2
swc.reduct2()
swc.write(filename2)

filename3 = filename2.replace('.', '-1.', 1)
print 'Generating %s' % filename3
swc.reduct1()
swc.write(filename3)

filename4 = filename3.replace('.', '-2.', 1)
print 'Generating %s' % filename4
swc.reduct2()
swc.write(filename4)

swc.show_hist()
final = swc.size_of_data()

print "%d -> %d" % (org, final)
