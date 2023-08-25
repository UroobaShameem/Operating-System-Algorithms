# Round Robbin Algorithm
The Round Robin scheduling algorithm is a pre-emptive scheduling algorithm commonly used in computer operating systems and multitasking environments. 
It's designed to provide fair distribution of CPU time among multiple processes or tasks by assigning each process a fixed time slice or quantum before moving on to the next process. 
This prevents any single process from monopolizing the CPU for an extended period.

## RoundRobin.py
This file contains the implementation of Round Robbin algorithm where it takes no. of processes, quantum size, arrival and execution time from user and generate PCB of each process.

## Final.py
This is an extended and modified version of code where PCB of processes is displayed while added functionality of resource allocation. User can demand for resource for any process. While the intruppt call will be generated, process will be blocked for that state. 
This approach is implemented using dictionary data structure and deque functions.
