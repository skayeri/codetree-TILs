n, k, T = input().split()
n, k = tuple(map(int, (n, k)))

arr = [input() for _ in range(n)]
arr.sort()

num = 0
for el in arr:
    if el.startswith(T):
        num += 1
        if num == k:
            print(el)