a, b = map(int, input().split())
ans = 0
l = []

for i in range(1, 1920):
    if 1920 % i == 0 and 2880 % i == 0:
        l.append(i)

for j in range(a, b+1):
    if j in l:
        ans = 1
        break
print(ans)