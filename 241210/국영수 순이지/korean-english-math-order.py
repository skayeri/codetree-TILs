n = int(input())

Student = [tuple(input().split()) for _ in range(n)]

Student.sort(key=lambda x: (-int(x[1]), -int(x[2]), -int(x[3])))

for s in Student:
    print(*s)