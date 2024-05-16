arr = [
    list(map(int, input().split()))
    for _ in range(4)
]

answer = 0
for index, i in enumerate(arr):
    answer += sum(i[:index+1])

print(answer)