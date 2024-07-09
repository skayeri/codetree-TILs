n1, n2 = map(int, input().split())
a = list(input().split())
b = list(input().split())

def cont(a, b):
    start = 0
    for i in range(n1):
        if a[i] == b[0]:
            start = i
            break
    temp = []
    for j in range(n2):
        try:
            temp.append(a[start + j])
        except:
            print('No')
    if temp == b:
        print('Yes')
    else:
        print('No')

cont(a, b)