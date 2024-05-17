n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]

num = 1
for k in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                arr[i][j] = num
                num += 1

for row in arr:
    for el in row:
        print(el, end=' ')
    print()