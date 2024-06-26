def function(x, y):
    l = []
    k = []
    for i in range(1, y + 1):
        l.append(x * i)
    for j in range(1, x + 1):
        k.append(y * j)
    for q in l:
        if q in k:
            print(q)
            break

n, m = map(int, input().split())

function(n, m)