def function(x, y):
    l = []
    for i in range(1, x + 1):
        a = x * i
        for j in range(1, x + 1):
            b = y * j
            if a == b:
                print(a)
                exit(0)

n, m = map(int, input().split())

function(n, m)