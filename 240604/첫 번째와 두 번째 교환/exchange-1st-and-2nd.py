s = input()

a = s[0]
b = s[1]

l = list(s)
for i in range(len(l)):
    if l[i] == a:
        l[i] = b
    elif l[i] == b:
        l[i] = a

print(''.join(l))