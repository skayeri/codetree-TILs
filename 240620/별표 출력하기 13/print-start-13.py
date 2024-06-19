n = int(input())
j = 1
k = 0
for i in range(1, 2*n+1):
    if i % 2 == 1:
        print('* ' * (n-k))
        k += 1
    else:
        print('* ' * j)
        j += 1