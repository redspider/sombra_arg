# openssl enc -rc4 -d -pass pass:rasomb <./ct.dat
import subprocess

import itertools


def check(password):
    result = subprocess.check_output('openssl enc -rc4 -d -pass pass:%s <./ct.dat' % password, shell=True)
    #if any([r for r in result if r > 127]):
    #    return
    print(password, result)



check('1337111765289947')
check('1337111799476528')

#for s in range(0,99999999):
#    check('13371117%08d' % s)
