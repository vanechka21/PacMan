class Field:
    def __init__(self):
        self.weight = 0
        self.height = 0
        self.size = [self.weight, self.height]
        self.teleport1_pos = [0, 0]
        self.teleport2_pos = [1, 1]

    def draw(self, size):
        pass

    def collision(self):
        # проверка на возможность передвижения
        pass

    def get_teleport_pos(self):
        # выводит координаты телепортов
        pass
