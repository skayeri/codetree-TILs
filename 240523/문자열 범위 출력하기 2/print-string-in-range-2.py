word = input()
n = int(input())


if n > len(word):
    for i in range(len(word)-1, -1, -1):
        print(word[i], end='')
else:
    for i in range(n):
        print(word[-(i+1)], end='')