n, k, T = input().split()
n, k = tuple(map(int, (n, k)))

arr = [input() for _ in range(n)]
arr.sort()

for el in arr:
    if el[:len(T)] == T:
        continue
    else:
        arr.remove(el)

print(arr[k-1])