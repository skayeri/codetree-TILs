def cal(x, y):
    X = min(x, y) + 10
    Y = max(x, y) * 2
    print(X, Y)

a, b = map(int, input().split())

cal(a, b)