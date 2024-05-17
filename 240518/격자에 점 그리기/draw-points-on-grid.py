n, m = map(int, input().split())

arr = [[0]*n for _ in range(n)]

cnt = 1
for i in range(m):
    r, c = tuple(map(int, input().split()))
    arr[r-1][c-1] = cnt
    cnt += 1

for row in arr:
    for el in row:
        print(el, end=' ')
    print()