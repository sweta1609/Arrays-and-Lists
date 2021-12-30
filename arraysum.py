def array_sum(n,li):
    sum = 0
    for i in li:
        sum += i
    return sum

n = int (input())
li = [int(x) for x in input().split()]
ans = array_sum(n,li)
print(ans)
