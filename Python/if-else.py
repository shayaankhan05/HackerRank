n = int(input())

if n % 2 != 0 or n in range(6, 20):
    print("Weird")
elif(n % 2 == 0 and(n > 20 or n in range(2, 6))):
    print("Not Weird")
