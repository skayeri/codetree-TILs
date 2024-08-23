n, m = map(int, input().split())
A = list(map(int, input().split()))
B = [list(map(int, input().split())) for i in range(m)]

def sol(m):
    global A
    for i in range(m):
        [a, b] = B[i]
        print(sum(A[a - 1 : b]))

sol(m)