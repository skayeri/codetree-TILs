n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Write your code here!

area = [0] * n

for (a, b) in commands:
    for i in range(a-1, b):
        area[i] += 1

print(max(area))