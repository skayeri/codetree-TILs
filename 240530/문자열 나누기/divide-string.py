n = int(input())
numbers = input().split()
s = ''

for i in numbers:
    s += i

curr = 1
target = 5

for j in range(len(s)):
    curr += 1
    if curr % target == 0:
        print(s[curr-5:curr])
if (len(s) % 5) != 0:
    print(s[-(len(s) % 5):])