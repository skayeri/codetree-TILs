a, b = map(int, input().split())
l = []
m = a
answer = 0

while m > 1:
    l.append(int(m % b))
    m //= b

arr = [0] * len(l)

for i in l:
    arr[i] += 1

for j in arr:
    answer += j**2

print(answer)