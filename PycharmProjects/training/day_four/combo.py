class Repeater:
    def __init__(self, v):
        self.value = v
    def __iter__(self):
        return self
    def __next__(self):
        return self.value

r1 = Repeater({121,14})
for var in r1:
    print(var)

