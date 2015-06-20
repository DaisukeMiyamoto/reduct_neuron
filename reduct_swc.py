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
print "%s : cmp=%d length=%.1f [um] vol=%.1f [um^3]" % (swc.get_filename(), swc.get_n_cmp(), swc.get_total_length(), swc.get_total_volume())


filename1 = filename.replace('.', '-1.', 1)
swc.reduct1()
swc.write(filename1)
print "%s : cmp=%d length=%.1f [um] vol=%.1f [um^3]" % (swc.get_filename(), swc.get_n_cmp(), swc.get_total_length(), swc.get_total_volume())

filename2 = filename1.replace('.', '-2.', 1)
swc.reduct2()
swc.write(filename2)
print "%s : cmp=%d length=%.1f [um] vol=%.1f [um^3]" % (swc.get_filename(), swc.get_n_cmp(), swc.get_total_length(), swc.get_total_volume())

filename3 = filename2.replace('.', '-1.', 1)
swc.reduct1()
swc.write(filename3)
print "%s : cmp=%d length=%.1f [um] vol=%.1f [um^3]" % (swc.get_filename(), swc.get_n_cmp(), swc.get_total_length(), swc.get_total_volume())

filename4 = filename3.replace('.', '-2.', 1)
swc.reduct2()
swc.write(filename4)
print "%s : cmp=%d length=%.1f [um] vol=%.1f [um^3]" % (swc.get_filename(), swc.get_n_cmp(), swc.get_total_length(), swc.get_total_volume())

