def printJobScheduling():
    jobs = []
    
    n = int(input("Enter the number of jobs: "))

    for i in range(n):
        jobName = input("Enter the job name: ")
        deadline = int(input("Enter the job deadline: "))
        profit = int(input("Enter the job profit: "))
        jobs.append([jobName, deadline, profit])

    jobs.sort(key=lambda x: x[2], reverse=True)

    maxDeadline = max(jobs, key=lambda x: x[1])[1]

    result = ['-1'] * maxDeadline           # Initialize result and slot arrays
    slot = [False] * maxDeadline

    maxProfit = 0
    for i in range(len(jobs)):
        for j in range(min(maxDeadline - 1, jobs[i][1] - 1), -1, -1):       # Find a free slot for this job
            if slot[j] is False:
                slot[j] = True
                result[j] = jobs[i][0]
                maxProfit += jobs[i][2]
                break

    print("Job Sequence:", result)
    print("Maximum Profit:", maxProfit)

printJobScheduling()
