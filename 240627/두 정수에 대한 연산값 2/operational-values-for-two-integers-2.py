def cal(x, y):
    X = min(x, y) + 10
    Y = max(x, y) * 2
    return X, Y

a, b = map(int, input().split())

X, Y = cal(a, b)
print(X, Y)