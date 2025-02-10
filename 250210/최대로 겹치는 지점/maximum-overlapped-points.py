n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!

line = [0] * 101

for s1, s2 in segments:
    for i in range(s1, s2+1):
        line[i] += 1

print(max(line))