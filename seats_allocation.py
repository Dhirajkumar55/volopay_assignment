# to get the coordinates of the window seats, T = O(n)
def getWindowSeats(n,m,position,key):
    ans = []
    if position == "starting" :
        for i in range(n):
            ans.append((key, i, 0))
    elif position == "ending" :
        for i in range(n):
            ans.append((key, i, m-1))
            
    return ans


# to get the coordinates of the aisle seats, T = O(n)
def getAisleSeats(n,m,position,key):  
    ans = []
    if position == "starting":
        for i in range(n):
            ans.append((key, i, m-1))
    elif position == "ending":
        for i in range(n):
            ans.append((key, i, 0))
    else:
        for i in range(n):
            ans.append((key, i, 0))
            
        for i in range(n):
            ans.append((key, i, m-1))
    
    return ans


# to get the coordinates of the middle seats, T = O(n*m)
def getMiddleSeats(n,m,key):   
    ans = []
    
    if m<=2:
        return ans
    
    for i in range(n):
        for j in range(1,m-1):
            ans.append((key, i, j))

    return ans


# function to order the coordinates from left -> right, top -> bottom , T = O(n*m)
def transform(arr, rows): 
    temp = [[] for _ in range(rows)]
   
    for i in arr:
        temp[i[1]].append(i)
    
    arr = []
    
    for i in temp:
        for j in i:
            arr.append(j)
            
    return arr
    

# function to print the seating order
def printSeats(seats):
    print("Allocation: \n")
    for i in seats:
        for j in i:
            for k in j:
                print(k, end = " ")
            print()
        print()
        
    

# main function
def main():
    n = int(input()) # input -> no of columns in aeroplane 

    seats = [None for i in range(n)]
    maxR = 0
    maxSeats = 0
    
    for i in range(n):
        cols, rows = 0, 0
        temp = input() # input -> for each column -> no of cols, no of rows
        cols = int(temp[0])
        rows = int(temp[2])
        maxSeats += cols*rows
        maxR = max(maxR, rows)
        seats[i] = [[-1 for k in range(cols)]for j in range(rows)]
    
    passengers = int(input())
        
    aisleSeats = [] #list to store aisleSeats
    windowSeats = [] #list to store windowSeats
    middleSeats = [] #list to store middleSeats
    
    
    for i in range(n): # T = O(n^2*m)
        rows = len(seats[i])
        cols = len(seats[i][0])
      
        s = ""
        
        if i == 0 : 
            s = "starting"  # this string is for window seats and aisle seats
        if i == n-1 :
            s = "ending"
            
        aS = getAisleSeats(rows, cols, s, i)
        aisleSeats.extend(aS)
        
        wS = getWindowSeats(rows, cols, s, i)
        windowSeats.extend(wS)
        
        mS = getMiddleSeats(rows, cols, i)
        middleSeats.extend(mS)
        

    aisleSeats = transform(aisleSeats, maxR)
    windowSeats = transform(windowSeats, maxR)
    middleSeats = transform(middleSeats, maxR)
    
    myQueue = [] #queue to hold the coordinated in left -> right, top -> bottom order
    
    for i in aisleSeats:  # fill aisle seats first
        myQueue.append(i)
        
    for i in windowSeats: # fill window seats after completely filling aisle seats
        myQueue.append(i)
    
    for i in middleSeats: # fill middle seats after completely filling window seats
        myQueue.append(i)
    
    
    if passengers > maxSeats: # check if passengers exceeds the max no of seats available
        print('Unable to allocate passengers starting from: ' + str(maxSeats+1), " to "+ str(passengers));
        print()
        passengers = maxSeats
    
    for x in range(passengers):
        topE = myQueue.pop(0)
        pos = topE[0]
        i = topE[1]
        j = topE[2]

        seats[pos][i][j] = x+1 # assigning the passenger to their corresponding seats
        
    printSeats(seats) # finally printing seats
    
    
    
#calling main function    
main()