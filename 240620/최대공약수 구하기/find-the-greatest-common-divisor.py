a, b = map(int, input().split())

def max_comm(n, m):
    for i in range(1, n):
        if n % i == 0 and m % i == 0:
            ans = i
    print(ans)
    
max_comm(a, b)