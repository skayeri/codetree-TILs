a, b, c, d = map(int, input().split())

hour = c - a
mins = d - b

print(hour * 60 + mins)