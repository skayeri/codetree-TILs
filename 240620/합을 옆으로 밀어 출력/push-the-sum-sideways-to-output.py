n = int(input())
l = [int(input()) for _ in range(n)]
s = str(sum(l))

print(s[1:] + s[0])