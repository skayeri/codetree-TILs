K, N = map(int, input().split())

answer = []

def print_answer(answer):
    print(*answer)

cur = 0
def select(cur):
    if cur == N:
        print_answer(answer)
        return
    for i in range(1, K + 1):
        answer.append(i)
        select(cur + 1)
        answer.pop()

select(cur)