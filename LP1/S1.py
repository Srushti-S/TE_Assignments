print("FIRST COME FIRST SERVE SCHEDULLING")
n= int(input("Enter number of processes : "))
d = dict()

for i in range(n):
    key = "P"+str(i+1)
    a = int(input("Enter arrival time of process"+str(i+1)+": "))
    b = int(input("Enter burst time of process"+str(i+1)+": "))
    l = []
    l.append(a)
    l.append(b)
    d[key] = l

d = sorted(d.items(), key=lambda item: item[1][0])

CT = []
for i in range(len(d)):
    if(i==0):
        CT.append(d[i][1][1])
    else:
        CT.append(CT[i-1] + d[i][1][1])     # get prevCT + newBT
WT = []
TAT = []
for i in range(len(d)):
    TAT.append(CT[i] - d[i][1][0])
    WT.append(TAT[i] - d[i][1][1])
    
avg_WT = 0
for i in WT:
    avg_WT +=i

avg_TAT=0
for i in TAT:
    avg_TAT+=i

print("Process | Arrival | Burst | Complete | Turn Around | Wait |")
for i in range(n):
      print("  ",d[i][0],"   |   ",d[i][1][0]," |    ",d[i][1][1]," |    ",CT[i],"  |    ",TAT[i],"  |   ",WT[i],"   |  ")
print("Average Waiting Time: ",avg_WT/n)
print("Average TurnAround Time: ",avg_TAT/n)

class RR:
    def fun(self, n):
        process_data = []
        for i in range(n):
            t = []
            pid = int(input("Enter Process ID: "))
            at = int(input(f"Enter Arrival Time for Process {pid}: "))
            bt = int(input(f"Enter Burst Time for Process {pid}: "))
            t.extend([pid, at, bt, 0, bt])
#            '0' is the state of the process. 0 means not executed and 1 means execution complete
            process_data.append(t)
        quant = int(input("Enter Time quantam: "))
        RR.schedulingProcess(self, process_data, quant)

    def schedulingProcess(self, process_data, quant):
        start_time = []
        ct = []
        executed_process = []
        ready_queue = []
        s_time = 0
        process_data.sort(key=lambda x: x[1])   #        Sort processes according to the Arrival Time
        while 1:
            queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][3] == 0:
                    present = 0
                    if len(ready_queue) != 0:
                        for k in range(len(ready_queue)):
                            if process_data[i][0] == ready_queue[k][0]:
                                present = 1
#                    The above if loop checks that the next process is not a part of ready_queue
                    if present == 0:
                        temp.extend([process_data[i][0], process_data[i]
                                     [1], process_data[i][2], process_data[i][4]])
                        ready_queue.append(temp)
                        temp = []
#                    The above if loop adds a process to the ready_queue only if it is not already present in it
                    if len(ready_queue) != 0 and len(executed_process) != 0:
                        for k in range(len(ready_queue)):
                            if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                                ready_queue.insert(
                                    (len(ready_queue) - 1), ready_queue.pop(k))
#                    The above if loop makes sure that the recently executed process is appended at the end of ready_queue
                elif process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i]
                                 [1], process_data[i][2], process_data[i][4]])
                    queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(queue) == 0:
                break
            if len(ready_queue) != 0:
                if ready_queue[0][2] > quant:
#                    If process has remaining burst time greater than the time slice, it will execute for a time period equal to time slice and then switch
                    start_time.append(s_time)
                    s_time = s_time + quant
                    e_time = s_time
                    ct.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = process_data[j][2] - quant
                    ready_queue.pop(0)
                elif ready_queue[0][2] <= quant:
#                    If a process has a remaining burst time less than or equal to time slice, it will complete its execution
                    start_time.append(s_time)
                    s_time = s_time + ready_queue[0][2]
                    e_time = s_time
                    ct.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)
                    ready_queue.pop(0)
            elif len(ready_queue) == 0:
                if s_time < queue[0][1]:
                    s_time = queue[0][1]
                if queue[0][2] > quant:
#                    If process has remaining burst time greater than the time slice, it will execute for a time period equal to time slice and then switch
                    start_time.append(s_time)
                    s_time = s_time + quant
                    e_time = s_time
                    ct.append(e_time)
                    executed_process.append(queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == queue[0][0]:
                            break
                    process_data[j][2] = process_data[j][2] - quant
                elif queue[0][2] <= quant:
#                    If a process has a remaining burst time less than or equal to time slice, it will complete its execution
                    start_time.append(s_time)
                    s_time = s_time + queue[0][2]
                    e_time = s_time
                    ct.append(e_time)
                    executed_process.append(queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == queue[0][0]:
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)
        t_time = RR.calculateTurnaroundTime(self, process_data)
        w_time = RR.calculateWaitingTime(self, process_data)
        RR.printData(self, process_data, t_time,w_time, executed_process)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        avg_tat = total_turnaround_time / len(process_data)
        return avg_tat

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        avg_wt = total_waiting_time / len(process_data)
        return avg_wt

    def printData(self, process_data, avg_tat, avg_wt, executed_process):
        process_data.sort(key=lambda x: x[0])
#        Sort processes according to the Process ID
        print("PID  AT   Rem_bt   Completed  Original_bt  Completion_Time  Turnaround_Time  Waiting_Time")
        for i in range(len(process_data)):
            # print('---')
            for j in range(len(process_data[i])):
                print(process_data[i][j], end="	")
            print()
        print(f'Average Turnaround Time: {avg_tat}')
        print(f'Average Waiting Time: {avg_wt}')
        print(f'Sequence of Processes: {executed_process}')

if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    rr = RR()
    rr.fun(n)
