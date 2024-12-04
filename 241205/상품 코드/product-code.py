class Product:
    def __init__(self, name = "", code = ""):
        self.n = name
        self.c = code

p1 = Product()
p2 = Product()

p1.n = "codetree"
p1.c = "50"

p2_name, p2_code = tuple(input().split())
p2.n = p2_name
p2.c = p2_code

print(f"product {p1.c} is {p1.n}")
print(f"product {p2.c} is {p2.n}")