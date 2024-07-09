def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

a, b = map(int, input().split())
ans = 0

for j in range(a, b + 1):
    if is_prime(j):
        ans += j

print(ans)