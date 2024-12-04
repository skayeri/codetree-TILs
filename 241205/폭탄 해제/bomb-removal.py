class Info:
    def __init__(self, code, color, second):
        self.code = code
        self.cl = color
        self.sec = second

code, color, second = tuple(input().split())
ans = Info(code, color, second)

print(f"code : {ans.code}", f"\ncolor : {ans.cl}", f"\nsecond : {ans.sec}")
