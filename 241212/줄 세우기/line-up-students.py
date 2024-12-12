n = int(input())

students = []
for i in range(n):
    height, weight = map(int, input().split())
    number = i + 1
    students.append((height, weight, number))

students.sort(key=lambda x: (-x[0], -x[1], x[2]))

for h, w, n in students:
    print(h, w, n)