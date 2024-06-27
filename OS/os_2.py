def check_deadlock(avail, alloc, need):
    work = avail[:]
    finish = [False] * len(alloc)
    
    while True:
        did_something = False
        for i in range(len(alloc)):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(len(avail))):
                for j in range(len(avail)):
                    work[j] += alloc[i][j]
                finish[i] = True
                did_something = True
                break
        if not did_something:
            break
    
    if all(finish):
        print("No deadlock.")
    else:
        print("Deadlock detected.")



avail_resources = [1, 1, 1] 

allocated_resources= [
    [2, 1, 1], 
    [1, 2, 1], 
    [1, 1, 2], 
]
requested_resources = [
    [2, 1, 0],  
    [1, 2, 1], 
    [1, 1, 2],  
]

print("Case 1 ")
check_deadlock(avail_resources, allocated_resources, requested_resources)

print("Case 2 ")
avail_resources = [3, 3, 2]  
allocated_resources = [
    [0, 1, 0],  
    [2, 0, 0],  
    [0, 0, 1], 
]

requested_resources = [
    [2, 0, 2], 
    [0, 2, 2],  
    [1, 1, 0],  
]

check_deadlock(avail_resources, allocated_resources, requested_resources)
