a, b = map(int, input().split())
n = input()

nlist = list(map(int, n))

num = 0
for i in range(len(nlist)):
    num = num * a + nlist[i]

ans = []
while True:
    if num < b:
        ans.append(num)
        break
    
    ans.append(num % b)
    num //= b

for a in ans[::-1]:
    print(a, end='')