import sys
from multiprocessing import Process, Queue

def square(n,q):
    q.put(['sqaured', n*n])

if __name__ == "__main__":
    q = Queue()
    proc = []
    for i in range(5):
        p = Process(target=square, args=(i,q,))
        proc.append(p)
        p.start()
    for p in proc:
        p.join()

    #qsize() gives size og the queue. The output might not be in order.
    for i in range(q.qsize()):
        print (q.get())
