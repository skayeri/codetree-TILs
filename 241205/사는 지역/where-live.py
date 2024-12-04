class Info:
    def __init__(self, name, zipcode, location):
        self.n = name
        self.z = zipcode
        self.l = location

num = int(input())

infos = []
names = []
for _ in range(num):
    n, z, l = tuple(input().split())
    names.append(n)
    infos.append(Info(n, z, l))

names.sort()
ans = 0
for i in range(num):
    if infos[i].n == names[-1]:
        ans = i

print(f"name {infos[ans].n}")
print(f"addr {infos[ans].z}")
print(f"city {infos[ans].l}")