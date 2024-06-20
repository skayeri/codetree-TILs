arr = list(map(int, input().split()))

for j in arr:
    if j % 3 == 0:
        print(arr[arr.index(j)-1])
        break