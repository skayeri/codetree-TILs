def cal(x, y):
    if x < y:
        X = x + 10
        Y = y * 2
    else:
        X = x * 2
        Y = y + 10
    return X, Y

a, b = map(int, input().split())

X, Y = cal(a, b)
print(X, Y)