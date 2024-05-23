arr = [input() for _ in range(10)]
letter = input()

for i in arr:
    if i[-1] == letter:
        print(i)