n = int(input())

Info = [tuple(input().split()) for _ in range(n)]

Info.sort(key=lambda x: x[1])

for i in Info:
    print(*i)