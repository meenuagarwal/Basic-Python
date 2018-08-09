import sys
from multiprocessing import Process, Manager

def square(n, sq_list):
    sq_list.append(n*n)

if __name__ == "__main__":
    mp = Manager()
    sq_list = mp.list()
    proc = []
    for i in range(4):
        p = Process(target=square, args=(i,sq_list,))
        proc.append(p)
        p.start()

    for p in proc:
        p.join()

    print (sq_list)
