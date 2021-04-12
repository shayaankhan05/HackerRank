if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    arr = []
    final = []

    for i in range(0, x+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                arr.append([i, j, k])

    for l in range(len(arr)):
        if sum(arr[l]) != n:
            final.append(arr[l])
    print(final)
