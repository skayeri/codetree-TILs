n = int(input())
arr = []

for i in range(n):
    (height, weight) = map(int, input().split())
    arr.append((height, weight, i + 1))

arr.sort(key=lambda x: (x[0], -x[1]))

for a in arr:
    print(*a)