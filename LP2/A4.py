def issafe(arr,x,y,n):
    for row in range(x):
        if arr[row][y] ==1:
            return False            # Checking column 
    row = x
    col = y
     
    while row>=0 and col>=0:        #Checking Diagonal 
        if arr[row][col]==1:
            return False
        row-=1
        col-=1
    row = x
    col = y
    
    while row>=0 and col<n:         #Checking Anti Diagonal 
        if arr[row][col]==1:
            return False
        row-=1
        col+=1
    return True

def nQueen(arr,x,n):
    if x>=n:                        #Terminating condition
        return True
    for col in range(n):
        if issafe(arr,x,col,n):
            arr[x][col]=1
            if nQueen(arr,x+1,n):   #checking terminating condition
                return True
            arr[x][col] = 0
    return False

def main():
    flag=1
    while(flag==1):       
        n = int(input("Enter number of squares : "))
        if n<4:
            print("Error! Please enter value greater than 3!!!")  
        else:
            arr = [[0]*n for i in range(0,n)]
        
            if nQueen(arr,0,n):
                for i in range(n):
                    for j in range(n):
                        print(arr[i][j],end=" ")
                    print()
        flag=int(input("Do you want to continue(1/0)?: "))

main()
