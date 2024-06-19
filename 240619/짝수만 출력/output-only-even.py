a, b = map(int, input().split())
i = 0
while a + i <= b:
    if (a + i) % 2 == 0:
        print(a + i, end=' ')
    i += 1