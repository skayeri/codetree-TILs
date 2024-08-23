arr = input()
target = input()

def pindex(arr, target):
    for i in range(len(arr)):
        if arr[i] == target[0]:
            if arr[i : i + len(target)] == target:
                print(i)
                break
    if target not in arr:
        print(-1)

pindex(arr, target)