class Spy:
    def __init__(self, codename, score):
        self.c = codename
        self.s = score

spys = []
for _ in range(5):
    codename, score = tuple(input().split())
    spys.append(Spy(codename, score))

scores = []
for i in range(5):
    scores.append(int(spys[i].s))

m = min(scores)

for j in range(5):
    if int(spys[j].s) == m:
        print(spys[j].c, spys[j].s)

