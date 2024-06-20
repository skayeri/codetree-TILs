def draw_rec(n):
    s = 1
    for i in range(n):
        for j in range(n):
            print(s, end=' ')
            s += 1
            if s == 10:
                s = 1
        print()

n = int(input())

draw_rec(n)