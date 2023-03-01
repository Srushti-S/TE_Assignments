g=0

def display(ele):
    for i in range(9):
        if i%3 == 0:
            print()
        if ele[i]==-1:
            print("_", end = " ")
        else:
            print(ele[i], end = " ")
    print()

def solvable(start):
    inv=0
    for i in range(9):
        if start[i] <= 1:
            continue
        for j in range(i+1,9):
            if start[j]==-1:
                continue
            if start[i]>start[j]:
                inv+=1
    if inv%2==0:
        return True
    return False

def heuristic(start,goal):
    global g
    h = 0
    for i in range(9):
        for j in range(9):
            if start[i] == goal[j] and start[i] != -1:
                h += (abs(j-i))//3 + (abs(j-i))%3
    return h + g

def left(start,pos):
    start[pos],start[pos-1]= start[pos-1],start[pos]

def right(start,pos):
    start[pos],start[pos+1]= start[pos+1],start[pos]

def up(start,pos):
    start[pos],start[pos-3]= start[pos-3],start[pos]

def down(start,pos):
    start[pos],start[pos+3]= start[pos+3],start[pos]

def move(start,goal):
    emptyat= start.index(-1)
    row = emptyat//3
    col = emptyat%3
    t1,t2,t3,t4 = start[:],start[:],start[:],start[:]
    f1,f2,f3,f4 = 100,100,100,100

    if col -1 >=0:
        left(t1, emptyat)
        f1 = heuristic(t1, goal)
    if col+1<3:
        right(t2, emptyat)
        f2 = heuristic(t2, goal)
    if row + 1 <3:
        down(t3, emptyat)
        f3 = heuristic(t3, goal)
    if row-1>=0:
        up(t4, emptyat)
        f4 = heuristic(t4, goal)

    min_heuristic = min(f1, f2,f3,f4)

    if f1==min_heuristic:
        left(start, emptyat)
    elif f2==min_heuristic:
        right(start, emptyat)
    elif f3==min_heuristic:
        down(start, emptyat)
    elif f4 == min_heuristic:
        up(start, emptyat)     
        
def solvePuzzle(start,goal):
    global g
    g+=1
    move(start,goal)
    display(start)
    f = heuristic(start,goal)
    if f == g:
        print("Puzzle solved in {} moves".format(f))
        return
    solvePuzzle(start,goal)

def main():
    global g
    start = list()
    goal = list()
    print("Enter the start state:(-1 for empty):")
    for i in range(9):
        start.append(int(input()))

    print("Enter the goal state:(-1 for empty):")
    for i in range(9):
        goal.append(int(input()))
    display(start)

    try:
        if solvable(start):
            solvePuzzle(start,goal)
            #print("Puzzle solved in {} moves".format(g))
        else:
            print("It's not possible to solve this puzzle")
    except:
        print("It's not possible to solve this puzzle")

if __name__ == '__main__':
    main()
