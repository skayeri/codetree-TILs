n = int(input())

for i in range(n):
    k = n
    for j in range(i + 1):
        print(k-i, end=' ')
        k += 1
    print()