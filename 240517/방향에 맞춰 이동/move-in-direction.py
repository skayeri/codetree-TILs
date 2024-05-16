N = int(input())
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
move = list(input() for _ in range(N))
nx, ny = 0, 0
for i in move:
    if i[0] == 'E':
        nx += dx[0]*int(i[2:])
    elif i[0] == 'N':
        ny += dy[1]*int(i[2:])
    elif i[0] == 'W':
        nx += dx[2]*int(i[2:])
    elif i[0] == 'S':
        ny += dy[3]*int(i[2:])

print(nx, ny)