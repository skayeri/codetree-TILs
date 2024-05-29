n = int(input())
numbers = input().split()
s = ''

for i in numbers:
    s += i


for j in range(len(s)):
    j += 1
    if j % 5 == 0:
        print(s[j-5:j])

if (len(s) % 5) != 0:
    print(s[-(len(s) % 5):])