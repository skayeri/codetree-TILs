n, m = map(int, input().split())

A = [
    list(map(int, input().split()))
    for _ in range(n)
]

B = [
    list(map(int, input().split()))
    for _ in range(n)
]

new = [
    [0]*m for _ in range(n) 
]

for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            new[i][j] = 1

for row in new:
    for col in row:
        print(col, end=' ')
    print()