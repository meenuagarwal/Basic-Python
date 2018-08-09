#python 2.7

import sys
from multiprocessing import Pool
from functools import partial

def mul(num,multiplier):
    return (num*multiplier)

if __name__ == "__main__":
    multiplier = [2,4,6,8]
    nof_proc = 4

    #create a pool of 4 sub-processes
    p = Pool(nof_proc)

    """ Maps the multiplier to the mul function. Pool.map takes only one iterable
     variable which is multiplier here. Partial is used to pass constant arguments
     to the function """
    res = p.map(partial(mul, 4), multiplier)
    print (res)
