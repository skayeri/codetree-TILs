n = int(input())

answer = 'no'

if n >= 3000:
    answer = 'book'
elif n >= 1000:
    answer = 'mask'
elif n >= 500:
    answer = 'pen'

print(answer)