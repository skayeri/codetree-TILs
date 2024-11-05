n = int(input())

def sol(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    else:
        return (sol(n-1) * sol(n-2)) % 100

print(sol(n))