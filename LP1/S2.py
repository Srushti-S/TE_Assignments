import copy

def srtf():
    p_info = []
    process_order = []
    n = int(input('ENTER THE NUMBER OF PROCESSES: '))
    print('ENTER THE PROCESS ID, ARRIVAL TIME AND BURST TIME RESPECTIVELY: ')
    for _ in range(n):
        temp_list = list(map(int, input().split()))
        temp_list.append(0)
        p_info.append(temp_list)
    original_p_info = copy.deepcopy(p_info)
    # p_info contains all the information of a process
    # each list(process) of p_info has [processid, arrival time, burst time, completion time]
    # sorting on the basis of arrival time
    p_info.sort(key=lambda k: k[1])
    original_p_info.sort(key=lambda p: p[1])

    cur_time = 0
    tot_time_req = 0
    for i in range(n):
        tot_time_req += p_info[i][2]
    counter = 0
    j = 0

    while (counter < tot_time_req):
        min_bt = 99999999
        p_no = None
        for j in range(n):      # for the first process
            if p_info[j][2] != 0:
                if p_info[j][1] <= cur_time:
                    if p_info[j][2] < min_bt:
                        min_bt = p_info[j][2]
                        p_no = p_info[j][0]             
        if p_no is None:
            process_order.append(-1)
            cur_time += 1
        else:
            process_order.append(p_no)
            cur_time += 1
            counter += 1
            for k in range(n):
                if p_no == p_info[k][0]:
                    p_info[k][2] -= 1
                    p_info[k][3] = cur_time

    gantt_chart = []
    i = 0
    ct = 0
    while i < len(process_order):
        x = 1
        for j in range(i + 1, len(process_order)):
            if process_order[i] == process_order[j]:
                x += 1
                if j == len(process_order) - 1:
                    ct += x
                    break
            else:
                ct += x
                break
        gantt_chart.append([process_order[i], ct])
        i += x
    print('\nGANTT CHART: ')
    for p in range(len(gantt_chart)):
        if gantt_chart[p][0] == -1:
            print('IDLE\t|', end='')
        else:
            print('P{}\t|'.format(gantt_chart[p][0]), end='')
    print()
    print('0', '\t', end='')
    for p in range(len(gantt_chart)):
        print(gantt_chart[p][1], '\t', end='')
    print()
    p_info.sort(key=lambda k: k[0]) # sorting on the basis of process time
    original_p_info.sort(key=lambda p: p[0])
    
    print("\nTABLE:\n")
    print('PROCESS NO.\tARRIVAL TIME\tBURST TIME\tCOMPLETION TIME\t\tTURN AROUND TIME\tWAITING TIME\t')
    for i in range(n):
        print(original_p_info[i][0], '\t\t', original_p_info[i][1], '\t\t', original_p_info[i][2],
              '\t\t', p_info[i][3], '\t\t\t', p_info[i][3] -
              p_info[i][1], '\t\t\t\t',
              p_info[i][3] - p_info[i][1] - original_p_info[i][2])
    tot_tat = 0
    tot_wt = 0
    for i in range(n):
        tot_tat += p_info[i][3] - p_info[i][1]
        tot_wt += p_info[i][3] - p_info[i][1] - original_p_info[i][2]
    print('\nAVERAGE TURN AROUND TIME: ', tot_tat/n)
    print('AVERAGE WAITING TIME: ', tot_wt/n)
srtf()

totalprocess = 5
proc = []
for i in range(totalprocess):
	l = []
	for j in range(4):
		l.append(0)
	proc.append(l)

def get_wt_time( wt):
	# declaring service array that stores cumulative burst time
	service = [0] * 5
	service[0] = 0
	wt[0] = 0
	for i in range(1, totalprocess):
		service[i] = proc[i - 1][1] + service[i - 1]
		wt[i] = service[i] - proc[i][0] + 1
		# If waiting time is negative, change it o zero
		if(wt[i] < 0) :	
			wt[i] = 0
		
def get_tat_time(tat, wt):

	# Filling turnaroundtime array
	for i in range(totalprocess):
		tat[i] = proc[i][1] + wt[i]

def display():
	
	# Declare waiting time and turnaround time array
	wt = [0] * 5
	tat = [0] * 5
	wavg = 0
	tavg = 0

	get_wt_time(wt)
	get_tat_time(tat, wt)

	stime = [0] * 5
	ctime = [0] * 5
	stime[0] = 1
	ctime[0] = stime[0] + tat[0]
	# calculating starting and ending time
	for i in range(1, totalprocess):
		stime[i] = ctime[i - 1]
		ctime[i] = stime[i] + tat[i] - wt[i]

	print("Process_no\tStart_time\tComplete_time","\tTurn_Around_Time\tWaiting_Time")

	# display the process details
	for i in range(totalprocess):
		wavg += wt[i]
		tavg += tat[i]
		
		print(proc[i][3], "\t\t", stime[i], "\t\t", end = " ")
		print(ctime[i], "\t\t", tat[i], "\t\t\t", wt[i])
	print("Average waiting time is : ",wavg / totalprocess)
	print("average turnaround time : " ,tavg / totalprocess)
	
# Driver code
if __name__ =="__main__":
    print("\nEnter the number of processes :", end=" ")
    n = int(input())

    arrivaltime = [0]*n
    bursttime = [0]*n
    priority = [0]*n
    
    print("\nEnter the arrival time of the processes :", end=" ")
    for i in range(n):
        arrivaltime[i] = int(input())

    print("\nEnter the burst time of the processes :", end=" ")
    for i in range(n):
        bursttime[i] = int(input())
    
    print("\nEnter the priority of the processes :", end=" ")
    for i in range(n):
        priority[i] = int(input())

    for i in range(n):

        proc[i][0] = arrivaltime[i]
        proc[i][1] = bursttime[i]
        proc[i][2] = priority[i]
        proc[i][3] = i + 1

    proc = sorted (proc, key = lambda x:x[2])   # Using inbuilt sort function
    proc = sorted (proc)

    display()
