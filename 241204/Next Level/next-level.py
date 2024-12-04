class Info:
    def __init__(self, ID = "", level = 0):
        self.id = ID
        self.level = level

cha1 = Info("codetree", 10)
cha2 = Info(*input().split())

print(f"user {cha1.id} lv {cha1.level}")
print(f"user {cha2.id} lv {cha2.level}")