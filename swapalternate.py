def swapAlternate(arr, n) :
    for i in range(0, (n - 1), 2) :
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")
    print()

n = int(input())
arr = list(map(int,input().split()))
swapAlternate (arr, n) 
printList(arr,n)
