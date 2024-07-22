a, b = map(int, input().split())

def op(a, b):
    if a < b:
        return a * 2, b + 25
    else:
        return a + 25, b * 2

a, b = op(a, b)

print(a, b)