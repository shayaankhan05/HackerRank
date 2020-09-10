from array import *
n = int(input().strip())
arr = []
p = 0
s = 0
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            p += arr[i][j]
        if (i+j) == (n-1):
            s += arr[i][j]
res = abs(p-s)
print(res)
