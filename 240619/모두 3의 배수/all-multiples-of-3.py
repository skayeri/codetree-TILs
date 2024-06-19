l = [int(input()) for _ in range(5)]
ans = 1

for i in l:
    if i % 3 != 0:
        ans = 0
        break

print(ans)