n = int(input())

def sol(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return sol(n // 2) + 1
    else:

        return sol(3 * n + 1) + 1

print(sol(n))