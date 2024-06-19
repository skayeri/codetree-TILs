l = []

while True:
    try:
        n = int(input())
        if 20 <= n < 30:
            l.append(n)
    except:
        break
print(format(sum(l) / len(l), ".2f"))