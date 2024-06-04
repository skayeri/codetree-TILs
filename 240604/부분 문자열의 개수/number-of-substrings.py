a = input()
b = input()
cnt = 0
length = len(a)

for i in range(0, length-1):
    if a[i] == b[0] and a[i+1] == b[1]:
        cnt += 1

print(cnt)