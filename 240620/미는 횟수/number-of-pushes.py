a = input()
b = input()
n = 0
ans = -1

for i in range(len(a)):
    n += 1
    a = a[-1] + a[:-1]
    if a == b:
        ans = n
        break
print(ans)