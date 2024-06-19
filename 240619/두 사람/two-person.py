a = list(input().split())
b = list(input().split())

ans = 0

if int(a[0]) >= 19 and a[1] == 'M':
    ans = 1
if int(b[0]) >= 19 and b[1] == 'M':
    ans = 1
print(ans)