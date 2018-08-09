Python doesn't quite support multithreading due to [GIL](https://realpython.com/python-gil/). So multithreading is not going to improve performance especially for CPU bound programs.
[Multiprocessing](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing) is a good solution in such cases (keeping the overhead of creating processes in mind). 
It runs the sub-processes on the free cores available in CPU. But ofcourse it comes with its problems i.e. shared variables. Since processes have their own independent memory, passing variables is a tricky part unlike in threading which uses shared memory.
The multiprocessing module provides some workaround for this difficulty such as -
- Manager: A manager object returned by Manager() can be used to create Python object types such as list, dict, Queue etc and allows other processes to manipulate them.
- Queue: A queue(First-In-First-Out data structure) can also be used for sharing data between processes. They are passed as a parameter for target function and can be consumed accordingly using put() method and for extracting the data by using get() method.
- Pooling: Pool is used to create a pool of 'n' number of processes to which jobs can be submitted. It has many useful methids such as apply(), map() and many more. It can be used to get output values from target function as shown in the example script.
