arr = list(input())

def sol(arr):
    arr_ = set((arr))
    if len(arr_) > 1:
        print('Yes')
    else:
        print('No')

sol(arr)