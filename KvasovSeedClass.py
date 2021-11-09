class Seed:
    def __init__(self, image, big_image):
        self.posx = 9
        self.posy = 0
        self.pos = [self.posx, self.posy]
        self.size = 0
        self.image = image
        self.big_image = big_image
        self.count = 0
        is_active = True

    def draw(self, big_image, image, count):
        # Прорисовка зерна
        raise NotImplemented
    def remove(self):
        raise NotImplemented