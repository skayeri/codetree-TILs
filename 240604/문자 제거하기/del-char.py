s = list(input())
n = len(s)
l = [int(input()) for _ in range(n-1)]

for i in l:
    if i >= len(s) - 1:
        s.pop(-1)
        print(''.join(s))
    else:  
        s.pop(i)
        print(''.join(s))