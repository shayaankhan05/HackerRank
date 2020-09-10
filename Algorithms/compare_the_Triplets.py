a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(3):
    if a[i] > b[i]:
        a[i], b[i] = 1, 0
    elif a[i] == b[i]:
        a[i], b[i] = 0, 0
    else:
        a[i], b[i] = 0, 1

r = sum(a)
s = sum(b)

print(r, s, end="")
