#!/usr/bin/env python

import sys
from swc import Swc


def reduct_swc(filename):
    swc = Swc(filename=filename, set_fingerprint=1)
    print("%s : cmp=%d length=%.1f [um] vol=%.1f [um^3]" % (
    swc.get_filename(), swc.get_n_cmp(), swc.get_total_length(), swc.get_total_volume()))

    filename1 = filename.replace('.', '-1.', 1)
    swc.reduct1()
    swc.write(filename1)
    print("%s : cmp=%d length=%.1f [um] vol=%.1f [um^3]" % (
    swc.get_filename(), swc.get_n_cmp(), swc.get_total_length(), swc.get_total_volume()))

    filename2 = filename1.replace('.', '-2.', 1)
    swc.reduct2()
    swc.write(filename2)
    print("%s : cmp=%d length=%.1f [um] vol=%.1f [um^3]" % (
    swc.get_filename(), swc.get_n_cmp(), swc.get_total_length(), swc.get_total_volume()))

    filename3 = filename2.replace('.', '-1.', 1)
    swc.reduct1()
    swc.write(filename3)
    print("%s : cmp=%d length=%.1f [um] vol=%.1f [um^3]" % (
    swc.get_filename(), swc.get_n_cmp(), swc.get_total_length(), swc.get_total_volume()))

    filename4 = filename3.replace('.', '-2.', 1)
    swc.reduct2()
    swc.write(filename4)
    print("%s : cmp=%d length=%.1f [um] vol=%.1f [um^3]" % (
    swc.get_filename(), swc.get_n_cmp(), swc.get_total_length(), swc.get_total_volume()))


def process_list(filelist_name):
    with open(filelist_name, 'r') as f:
        filelist = [line.strip() for line in f.readlines()]

    for file in filelist:
        print('Processing %s', file)
        reduct_swc(file)


if __name__ == '__main__':
    # process_list('sample_list.txt')
    # process_list('flycircuit_M_list.txt')
    process_list('flycircuit_F_list_again.txt')

