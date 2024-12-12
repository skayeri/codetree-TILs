n = int(input())

info = []

for _ in range(n):
    name, height, weight = input().split()
    info.append((name, int(height), int(weight)))

info.sort(key=lambda x: (x[1], -x[2]))

for i in info:
    print(*i)