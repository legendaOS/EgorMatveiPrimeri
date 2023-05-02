class ParnoKopit:
    def __init__(self, name, age, legs):
        self.name = name
        self.age = age
        self.legs = legs

    def game(self):
        print(self.name, 'умеет играть в ПК')


class Jiraf(ParnoKopit):
    def __init__(self, name, age, legs, skill):
        
        super().__init__(name, age, legs)

        self.skill = skill


    def game(self):
        print(self.name, 'умеет играть в Фортнайт', self.skill)


rafik = Jiraf('Рафик', 20, 3, 'слабо')

leva = ParnoKopit('Лева', 15, 4)

rafik.game()
leva.game()
