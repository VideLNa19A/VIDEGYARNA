from GameField import GameField

class Food:
    foods = []

    def __init__(self):
        self.color = (214, 8, 8)
        self.radius = 4

        self.pos = GameField.random_point(0.75)
        self.x = self.pos[0]
        self.y = self.pos[1]

        self.foods.append(self)
        