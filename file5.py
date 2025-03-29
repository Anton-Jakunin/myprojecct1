from random import random, randint
class Potion:
    def __init__(self, name, quality):
        self.name = name
        self.quality= quality
    def __str__(self):
        return f'Зелье с названием: {self.name}'
    def __add__(self, other):
        print(random() * (0.5 + 0.5) - 0.5)
        new_quality = ((self.quality + other.quality) / 2 )- (abs(self.quality - other.quality)) * (random() * (1 + 1) - 1)
        if new_quality < 30:
            raise ValueError('Получилось некачественное зелье')
        self_len = len(self.name) //2
        other_len = len(other.name) // 2
        new_name = self.name[:self_len] + other.name[other_len:]
        return Potion(new_name, new_quality)

        
a = Potion('Veritaserum', randint(30, 80))
b = Potion('Nelirotirum',randint(30, 80))
print(a + b)