class Info:
    def __init__(self, ID = "", level = 0):
        self.id = ID
        self.level = level

cha1 = Info()
cha1.id = "codetree"
cha1.level = 10

cha2 = Info()
x, y = (input().split())
cha2.id = x
cha2.level = int(y)

print(f"user {cha1.id} lv {cha1.level}")
print(f"user {cha2.id} lv {cha2.level}")