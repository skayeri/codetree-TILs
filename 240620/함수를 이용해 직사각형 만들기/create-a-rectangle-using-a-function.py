def print_rect(n, m):
    for _ in range(n):
        print('1' * m)

r, c = map(int, input().split())
print_rect(r, c)