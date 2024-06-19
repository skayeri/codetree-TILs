a, b = map(int, input().split())
l = [2, 4, 6, 8]

for i in l:
    for j in range(b, a-1, -1):
        print(j, '*', i, '=', j * i, end='')
        if j != a:
            print(' / ', end='')
    print()