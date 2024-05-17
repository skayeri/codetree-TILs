n = int(input())

arr = []

for i in range(n):
    arr.append([0]*(i+1))

arr[0][0] = 1

for i in range(n):
    for j in range(len(arr[i])):
        if j == 0 or j == len(arr[i]) - 1:
            arr[i][j] = 1            
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for row in arr:
    for el in row:
        print(el, end=' ')
    print()