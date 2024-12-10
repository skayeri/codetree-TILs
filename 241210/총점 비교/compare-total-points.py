n = int(input())

Students = []
for _ in range(n):
    name, kor, eng, math = tuple(input().split())
    Students.append((name, int(kor), int(eng), int(math)))

Students.sort(key=lambda x: x[1] + x[2] + x[3])

for name, kor, eng, math in Students:
    print(name, kor, eng, math)