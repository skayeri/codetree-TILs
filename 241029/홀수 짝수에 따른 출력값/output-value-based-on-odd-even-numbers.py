n = int(input())

def sol(n):
    if n <= 2:
        return n
    
    return sol(n - 2) + n

print(sol(n))