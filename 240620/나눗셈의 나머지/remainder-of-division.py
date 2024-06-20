a, b = map(int, input().split())
l = [0] * 10
m = a
answer = 0

while m > 1:
    l[int(m % b)] += 1
    m //= b

for j in l:
    answer += j**2

print(answer)