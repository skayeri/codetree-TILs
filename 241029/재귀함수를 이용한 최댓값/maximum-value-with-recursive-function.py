m = int(input()) - 1
n_list = list(map(int, input().split()))

def max_num(n_list, n):
    if n == 0:
        return n_list[0]
    
    if n_list[n] >= max(n_list[:n]):
        return n_list[n]
    else:
        return max_num(n_list, n - 1)

print(max_num(n_list, m))