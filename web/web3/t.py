class A:
    def __init__(self):
        self.a = 10
        self.b = 20


key = "a"
a = A()
print(getattr(a, key))  # -> a.a
