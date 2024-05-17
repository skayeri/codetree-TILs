a, b, c = list(input() for _ in range(3))

la = len(a)
lb = len(b)
lc = len(c)

temp = [la, lb, lc]

print(max(temp) - min(temp))