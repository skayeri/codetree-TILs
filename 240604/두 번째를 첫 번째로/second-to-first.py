s = list(input())
t = s[1]
change = s[0]

for idx, j in enumerate(s):
    if j == t:
        s[idx] = change

print(''.join(s))