n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!

negative = [0]
for (s1, s2) in segments:
    if s1 < 0:
        negative.append(s1)
    if s2 < 0:
        negative.append(s2)

for (s1, s2) in segments:
    s1 += abs(min(negative))
    s2 += abs(min(negative))

dim = [0] * 200

for (s1, s2) in segments:
    for i in range(s1, s2):
        dim[i] += 1

print(max(dim))