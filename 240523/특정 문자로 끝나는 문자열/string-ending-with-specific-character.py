arr = [input() for _ in range(10)]
letter = input()

a = 0

for i in arr:
    if i[-1] == letter:
        print(i)
        a = 1
        
if a == 0:
    print('None')