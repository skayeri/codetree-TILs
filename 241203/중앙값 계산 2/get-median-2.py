n = int(input())
arr = list(map(int, input().split()))
ans = []

for i, num in enumerate(arr):
    if i % 2 == 0:
        temp = sorted(arr[:i+1])
        ans.append(temp[len(temp)//2])

print(*ans)