
def FirstFit(block_Size, blocks, process_Size, proccesses):
    # code to store the block id of the block that needs to be allocated to a process
    allocate = [-1] * proccesses
    occupied = [False] * blocks

    # Any process is assigned with the memory at the initial stage
    # find a suitable block for each process; the blocks are allocated as per their size
    for i in range(proccesses):
        for j in range(blocks):
            if not occupied[j] and (block_Size[j] >= process_Size[i]):
                allocate[i] = j
                occupied[j] = True
                break

    print("Process No.\t    Process Size \t      Block No.")

    for i in range(proccesses):
        print(str(i + 1) + "\t\t\t" + str(process_Size[i]) + "\t\t\t", end=" ")

        if allocate[i] != -1:
            print(allocate[i] + 1)
        else:
            print("Not Allocated")

def NextFit(block_Size, m, process_Size, n):
    # Stores block id of the block allocated to a process
     # Initially no block is assigned to any process
    
    allocation = [-1] * n
    j = 0
    t = m-1
    
    for i in range(n):          # pick each process and find suitable blocks according to its size ad assign to it
 
        while j < m:    #no starting from beginning 
            if block_Size[j] >= process_Size[i]:
                
                allocation[i] = j       # allocate block j to p[i] process
                
                block_Size[j] -= process_Size[i]        # Reduce available memory in this block.
               
                t = (j - 1) % m         # sets a new end point
                break
            if t == j:
                t = (j - 1) % m     # sets a new end point
                break   # breaks the loop after going through all memory block
             
            j = (j + 1) % m     # mod m will help in traversing the blocks from starting block after we reach the end.
              
    print("Process No.\t    Process Size \t      Block No.")
     
    for i in range(n):
        print(i + 1, "\t\t\t", process_Size[i],end = "\t\t\t")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

def worstfit(block_Size, m, process_Size, n): 
    allocate = [-1] * n 
    #select each process and search for an empty memory block as per its memory demand
    
    for i in range(n): 
    # Find an empty memory block for the current process 
        wstIdx = -1
        for j in range(m): 
            if block_Size[j] >= process_Size[i]: 
                if wstIdx == -1:  
                    wstIdx = j  
                elif block_Size[wstIdx] < block_Size[j]:  
                    wstIdx = j 
       #code to find an empty block for the current process        
     
        if wstIdx != -1: 
            # allocating empty memory space j to p[i] process  
            allocate[i] = wstIdx  
            # Reduce available memory in this block. 
            block_Size[wstIdx] -= process_Size[i] 
  
    
    print("Process No.\t    Process Size \t      Block No.") 
    for i in range(n): 
    
        print(i + 1, "\t\t\t",process_Size[i], end = "\t\t\t")  
        if allocate[i] != -1: 
            print("",allocate[i] + 1)  
        else:
            print(" Not Allocated") 

def bestFit(block_Size, m, process_Size, n):
      
    # Stores block id of the block allocated to a process 
    allocation = [-1] * n 
      
    # pick each process and find suitable blocks according to its size ad assign to it
    for i in range(n):
          
        # Find the best fit block for current process 
        bestIdx = -1
        for j in range(m):
            if block_Size[j] >= process_Size[i]:
                if bestIdx == -1: 
                    bestIdx = j 
                elif(block_Size[bestIdx] > block_Size[j]): 
                    bestIdx = j
  
        # If we could find a block for current process 
        if bestIdx != -1:
              
            # allocate block j to p[i] process 
            allocation[i] = bestIdx 
  
            # Reduce available memory in this block. 
            block_Size[bestIdx] -= process_Size[i]
  
    print("Process No. Process Size     Block no.")
    for i in range(n):
        print(i + 1, "\t\t\t", process_Size[i], end = "\t\t\t") 
        if allocation[i] != -1: 
            print(allocation[i] + 1) 
        else:
            print("Not Allocated")

    

# Driver code
'''
block_Size=[]
process_Size=[]

m= int(input("Enter length for block size: "))
print("Enter elements for block size::")
for i in range(m):
    ele=int(input())
    block_Size.append(ele)
n= int(input("Enter length for process size: "))
print("Enter elements for process size::")
for i in range(n):
    ele=int(input())
    process_Size.append(ele)
'''
block_Size = [100, 500, 200, 300, 600]
process_Size = [212, 417, 112, 426]
m = len(block_Size)
n = len(process_Size)
print("Menu: 1.First Fit  2.Best Fit  3.Worst Fit  4.Next Fit")
ch=int(input("Which algorithm you want to perform: "))

if(ch==1):
    FirstFit(block_Size, m, process_Size, n)
elif(ch==2):
    bestFit(block_Size, m, process_Size, n)
elif(ch==3):
    worstfit(block_Size, m, process_Size, n)
elif(ch==4):
    NextFit(block_Size, m, process_Size, n)
    
