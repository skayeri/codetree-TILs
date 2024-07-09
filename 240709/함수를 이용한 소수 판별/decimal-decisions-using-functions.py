def is_prime(x):
    if x == 1:
        return True
    else:
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