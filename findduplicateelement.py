def duplicateNumber(arr, n) :
    for i in range (n):
        for j in range (i + 1 , n):
            if i == j:
                continue
            elif arr[i] == arr[j]:
                print (arr[i] , end= ' ')
                print ()
n = int(input())
arr = list(map(int,input().split()))
duplicateNumber(arr, n)
