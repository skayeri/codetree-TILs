n = int(input())

dots = []
for i in range(1, n + 1):
    x, y = map(int, input().split())
    dots.append((x, y, i))

dots.sort(key=lambda x: (abs(x[0]) + abs(x[1]), x[2]))

for _, _, number in dots:
    print(number)