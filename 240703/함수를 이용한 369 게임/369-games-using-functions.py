a, b = map(int, input().split())

def is_369(n):
    while n > 0:
        if n % 10 in (3, 6, 9):
            return True
        n //= 10
    return False

def is_target(x):
    return x % 3 == 0 or is_369(x)

cnt = 0
for i in range(a, b+1):
    if is_target(i):
        cnt += 1

print(cnt)