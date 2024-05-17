n, m = map(int, input().split())

grid = [[0]*n for _ in range(n)]

for _ in range(m):
    r, c = tuple(map(int, input().split()))
    grid[r-1][c-1] = 1

for row in grid:
    for el in row:
        print(el, end=' ')
    print()