n = int(input())
arr = list(map(int, input().split()))
l = []

for i in range(n):
    for j in arr:
        m = abs(arr[i] - j)
        if m != 0:
            l.append(m)
print(min(l))