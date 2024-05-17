n, m = map(int, input().split())
num = 0

arr = [
    [0] * m for _ in range(n)
]

for i in range(m):
    for j in range(n):
        if i % 2 ==0:
            arr[j][i] = num
        else:
            arr[n-j-1][i] = num
        num += 1

for row in arr:
    for el in row:
        print(el, end=' ')
    print()