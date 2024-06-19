l = [int(input()) for _ in range(5)]
ans = 0
for i in l:
    if i % 2 == 0:
        ans += 1
print(ans)