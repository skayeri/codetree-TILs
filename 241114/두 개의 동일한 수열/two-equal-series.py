n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

cnt = 0
for i in range(n):
    if a[i] != b[i]:
        print('No')
        break
    else:
        cnt += 1
    if cnt == n:
        print('Yes')