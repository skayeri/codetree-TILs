class Secret:
    def __init__(self, code, location, time):
        self.c = code
        self.l = location
        self.t = time

answer = Secret(*input().split())

print("secret code : %s"%answer.c)
print("meeting point : %s"%answer.l)
print("time : %s"%answer.t)