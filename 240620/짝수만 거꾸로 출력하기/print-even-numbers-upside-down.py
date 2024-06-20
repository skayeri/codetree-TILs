n = int(input())
l = list(input().split())
x = []
for i in l:
    if int(i) % 2 == 0:
        x.append(int(i))

for j in x[::-1]:
    print(j, end=' ')