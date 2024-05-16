arr = [list(map(int, input().split())) for _ in range(2)]

for i in arr:
    print(f"{sum(i)/4:.1f}", end=' ')
print()

for j in range(4):
    temp = []
    for k in arr:
        temp.append(k[j])
    print(f"{sum(temp)/2:.1f}", end=' ')
print()

s = 0
for a in arr:
    s += sum(a)
print(f"{s/8:.1f}")