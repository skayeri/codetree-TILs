a = input()
b = input()

A = ''
B = ''

for i in a:
    if i.isdigit():
        A += i
for j in b:
    if j.isdigit():
        B += j

print(int(A) + int(B))