a, b = map(int, input().split())

def jud_num(n):
    if n == 1:
         return False
    for i in range(2, n):
        if n % i == 0:
            return False
    if n != 100 and (n // 10 + n % 10) % 2 == 0:
        return True

cnt = 0
for i in range(a, b + 1):
    if jud_num(i):
        cnt += 1

print(cnt)