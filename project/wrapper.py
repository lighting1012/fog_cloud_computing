# COMP9334 project (19-T1) -- University of New South Wales
# Fog/cloud Computing
# Written by Jiaquan Xu

# How to run this program ?
# -- Make sure that the input files, wrapper.py, proj.py are in current directory
# -- Use command : python wrapper.py
# -- Then it will generate the output files.

import proj

num_tests_file = open('num_tests.txt','r')
num_tests = int(num_tests_file.read())
for i in range(1, num_tests+1):
    proj.write_file(i)