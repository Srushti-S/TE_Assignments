# profit   = [15,27,10,100, 150]
# jobs     = ["j1", "j2", "j3", "j4", "j5"]
# deadline = [2,3,3,3,4] 

profit = list()
jobs = list()
deadline = list()

n=int(input("Enter total number of jobs: "))
print("Enter {} job ids:".format(n))
for i in range(n):
    jobs.append(input())

print("Enter deadline for {} job ids:".format(n))
for i in range(n):
    deadline.append(int(input()))

print("Enter profit for {} job ids:".format(n))
for i in range(n):
    profit.append(int(input()))

profitNJobs = list(zip(profit,jobs,deadline))
profitNJobs = sorted(profitNJobs, key = lambda x: x[0], reverse = True)
slot = []
for _ in range(len(jobs)):
    slot.append(0)

profit = 0
ans = []

for i in range(len(jobs)):
    ans.append('null')

for i in range(len(jobs)):
        job = profitNJobs[i]
        for j in range(job[2], 0, -1):      #check if slot is occupied
            if slot[j] == 0:
                ans[j] = job[1]
                profit += job[0]
                slot[j] = 1
                break
        
print("Maximum profit sequence of jobs => ",ans[1:])
print("Profit => ",profit)
