n = int(input())
arr = [input() for _ in range(n)]
lett = input()

cnt = 0
ans = []

for i in arr:
    if i[0] == lett:
        cnt += 1
        ans.append(i)

length = 0
for j in ans:
    length += len(j)

answer = length/len(ans)

print(cnt, '%.2f'%answer)