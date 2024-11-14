n = int(input())
_list = list(map(int, input().split()))
sub = []

_list.sort()

for i in range(n):
    sub.append([_list[i], _list[-(i+1)]])

ans = 0
for a, b in sub:
    if ans <= a + b:
        ans = a + b

print(ans)