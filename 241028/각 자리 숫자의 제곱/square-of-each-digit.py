def sol(n):
    if n < 10:
        return n**2

    return sol(n // 10) + (n % 10)**2

n = int(input())

print(sol(n))