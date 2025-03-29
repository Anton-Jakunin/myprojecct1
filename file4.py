class Cat:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'Cat: {self.name}'
    def __add__(self, other):
        result = self.name + other.name
        return Cat(result)
fluffy = Cat('fluffy')
pushok = Cat('pushok')
print(fluffy + pushok)