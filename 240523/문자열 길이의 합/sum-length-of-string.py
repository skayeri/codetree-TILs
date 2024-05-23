n = int(input())
arr = [input() for _ in range(n)]

length = 0
cnt = 0

for i in arr:
    length += len(i)
    if i[0] == 'a':
        cnt += 1

print(length, cnt)