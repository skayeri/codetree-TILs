s, q = input().split()
q = int(q)
l = [int(input()) for _ in range(q)]

for i in l:
    if i == 1:
        s = s[1:] + s[0]
        print(s)
    elif i == 2:
        s = s[-1] + s[:-1]
        print(s)
    else:
        s = list(s)
        s.reverse()
        s = ''.join(s)
        print(s)