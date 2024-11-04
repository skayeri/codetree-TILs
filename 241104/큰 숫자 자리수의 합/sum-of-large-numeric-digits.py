def sol(a):
    if a == 0:
        return 0

    return sol(a // 10) + a % 10

_list = list(map(int, input().split()))
val = 1
for i in range(3):
     val *= _list[i]

print(sol(val))