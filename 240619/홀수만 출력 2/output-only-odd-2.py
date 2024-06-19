b, a = map(int, input().split())
l = []

for i in range(a, b+1, 2):
    l.append(i)

l.reverse()

for j in l:
    print(j, end=' ')