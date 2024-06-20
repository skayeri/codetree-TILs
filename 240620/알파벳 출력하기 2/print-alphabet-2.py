n = int(input())
cnt = 0
for i in range(n):
    print('  ' * i, end='')
    for j in range(n-i):
        print(chr(65 + cnt), end=' ')
        cnt += 1
        if cnt == 26:
            cnt = 0
    print()