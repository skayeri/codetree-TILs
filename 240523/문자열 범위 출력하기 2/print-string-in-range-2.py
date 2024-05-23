word = input()
n = int(input())

for i in range(n):
    if n > len(word):
        for i in range(len(word), -1, -1):
            print(word[-(i+1)], end='')
    else:
        print(word[-(i+1)], end='')