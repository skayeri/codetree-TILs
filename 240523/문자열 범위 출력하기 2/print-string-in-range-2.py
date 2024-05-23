word = input()
n = int(input())

for i in range(n):
    print(word[-(i+1)], end='')