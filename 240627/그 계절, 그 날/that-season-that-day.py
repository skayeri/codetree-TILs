def season(y, m, d):
    if m == 2:
        if y % 4 == 0 and y % 100 == 0 and y % 400:
            last_day = 29
        elif y % 4 == 0 and y % 100 == 0:
            last_day = 28
        elif y % 4 == 0:
            last_day = 29
        else:
            last_day = 28
        ans = 'Winter'
    elif 3 <= m <= 5:
        ans = 'Spring'
    elif 6 <= m <= 8:
        ans = 'Summer'
    elif 9 <= m <= 11:
        ans = 'Fall'
    else:
        ans = 'Winter'
    
    if m in [1, 3, 5, 7, 8, 10, 12]:
        last_day = 31
    elif m in [4, 6, 9, 11]:
        last_day = 30

    if d <= last_day:
        print(ans)
    else:
        print(-1)

Y, M, D = map(int, input().split())
season(Y, M, D)