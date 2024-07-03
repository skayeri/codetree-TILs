def is_target(x):
    return x % 2 == 0 and (x // 10 + x % 10) % 5 == 0

n = int(input())
if is_target(n):
    print('Yes')
else:
    print('No')