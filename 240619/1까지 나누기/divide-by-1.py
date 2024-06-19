n = int(input())
ans = 0

for i in range(1, n+1):
    n /= i
    ans += 1
    if n / i <= 1:
        ans += 1
        break

print(ans)