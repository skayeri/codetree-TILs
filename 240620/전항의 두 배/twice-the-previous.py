arr = list(map(int, input().split()))

for i in range(8):
    arr.append(arr[i] * 2 + arr[i + 1])

print(*arr)