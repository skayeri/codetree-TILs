info = []

for _ in range(5):
    name, height, weight = input().split()
    info.append((name, int(height), float(weight)))

sort_name = sorted(info, key=lambda x: x[0])
sort_height = sorted(info, key=lambda x: -x[1])

print('name')
for n in sort_name:
    print(*n)

print('\nheight')
for h in sort_height:
    print(*h)