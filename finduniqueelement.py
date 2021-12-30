def findUnique(arr, n) :
    #Your code goes here
    for i in range(n):
        flag = True
        for j in range(n):
            if i == j:
                continue
            elif arr[i] == arr[j]:
                flag = False
                break
        if flag==True:
            return arr[i]
n = int(input())
arr = list(map(int,input().split()))
print(findUnique(arr, n))
