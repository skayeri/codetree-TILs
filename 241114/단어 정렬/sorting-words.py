n = int(input())
words = [input() for _ in range(n)]
sort_w = sorted(words)

for i in range(n):
    print(sort_w[i])