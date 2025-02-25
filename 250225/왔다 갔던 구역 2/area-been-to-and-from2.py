n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Write your code here!

arr = [0] * 1001

cur = 500
for i in range(n):
    if dir[i] == "R":
        for _ in range(x[i]):
            arr[cur] += 1
            cur += 1

    else:
        for _ in range(x[i]):
            cur -= 1
            arr[cur] += 1
            
ans = 0
for a in arr:
    if a >= 2:
        ans += 1

print(ans)