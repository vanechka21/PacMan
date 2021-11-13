class Ghost:
    def image_choice(self):
        #выбирает нужные файлы для изображений
        pass
    def __init__(self, image1, image2, image3):
        self.posx = 0
        self.posy = 0
        self.pos = (self.posx, self.posy)
        self.image = [image1, image2, image3]
        self.direction = (0, 0)

    def move(self, pos):
        # Движение привидения
        raise NotImplemented

    def draw(self, image):
        # отрисовка привидения
        raise NotImplemented

    def change_direction(self, direction):
        # смена направления
        raise NotImplemented

    def collision_action(self):
        raise NotImplemented