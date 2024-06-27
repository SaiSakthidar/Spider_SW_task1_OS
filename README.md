# Spider_SW_task1_OS

## Process Management	

Waiting Time: The amount of time a process has been in the ready queue waiting to get executed. 
              It does not include the time the process actually spends executing or being idle.
              
Turnaround Time: The total time taken between the submission of a process and its completion.
                  It includes waiting time and execution time.

Run os_1.py to check the process scheduling and the average waiting and turnaround times

## Deadlock Handling

Process:
This is an implementation of bankers algorithm
Initializes a list work as a copy of avail, representing the working copy of available resources.
Initializes a list finish with boolean values, all set to 0, indicating whether each process has completed.
Enters a loop to try allocating resources to each unfinished process if possible (i.e., if every needed resource by a process is less than or equal to the corresponding available resource in work).
If resources can be allocated to a process, it updates work by adding the resources allocated to that process back into it marks the process as finished, and breaks to retry allocation from the first process again (since the state has changed).
If no allocation can be made in a full loop iteration, it breaks out of the loop.

Outcome:

If all processes can finish (i.e., finish list contains all True), there is no deadlock
Otherwise, it prints "Deadlock possible"
