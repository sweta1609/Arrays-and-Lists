from sys import stdin

def sortZeroesAndOne(arr, n) :
    #Your code goes here 
    count = 0
 
    for i in range(0, n) :
        if (arr[i] == 0) :
            count = count + 1
    for i in range(0, count) :
        arr[i] = 0
    for i in range(count, n) :
        arr[i] = 1
         
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = ' ')
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    sortZeroesAndOne(arr, n)
    printList(arr, n)
    print()

    t -= 1
