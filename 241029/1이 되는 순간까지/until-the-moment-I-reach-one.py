n = int(input())
ans = 0

def sol(n, ans):
    if n == 1:
        return ans

    if n % 2 == 0:
        ans += 1
        return sol(n // 2, ans)
    else:
        ans += 1
        return sol(n // 3, ans)

print(sol(n, ans))