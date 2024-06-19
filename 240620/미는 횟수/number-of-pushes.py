a = input()
b = input()
n = 0

for i in range(len(a)):
    n += 1
    a = a[-1] + a[:-1]
    if a == b:
        print(n)
        break