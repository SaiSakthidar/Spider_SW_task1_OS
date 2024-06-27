def calculate_times(processes):
    time = 0
    waiting_times = []
    turnaround_times = []
    
    for process in processes:
        arrival_time, burst_time = process[1], process[2]
        waiting_time = time - arrival_time
        waiting_times.append(waiting_time)
        
        time += burst_time
        turnaround_time = waiting_time + burst_time
        turnaround_times.append(turnaround_time)
    
    avg_waiting_time = sum(waiting_times) / len(waiting_times)
    avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)
    
    return avg_waiting_time, avg_turnaround_time

processes = [(1, 0, 5), (2, 2, 3), (3, 4, 8)]
avg_waiting_time, avg_turnaround_time = calculate_times(processes)
print(f"Average Waiting Time: {avg_waiting_time}")
print(f"Average Turnaround Time: {avg_turnaround_time}")

'''
Waiting Time: The amount of time a process has been in the ready queue waiting to get executed. 
              It does not include the time the process actually spends executing or being idle.
Turnaround Time: The total time taken between the submission of a process and its completion.
                  It includes waiting time and execution time.
'''