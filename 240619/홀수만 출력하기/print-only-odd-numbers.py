N = int(input())
l = [input() for _ in range(N)]

for i in l:
    if int(i) % 2 == 1 and int(i) % 3 == 0:
        print(i)