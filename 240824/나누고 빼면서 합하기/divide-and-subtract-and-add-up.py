n, m = map(int, input().split())
A = list(map(int, input().split()))

def sol(n, m, A):
    sum_val = A[m - 1]
    while m > 1:
        if m % 2 == 1:
            m -= 1
            sum_val += A[m - 1]
        else:
            m //= 2
            sum_val += A[m - 1]
    return sum_val

ans = sol(n, m, A)
print(ans)