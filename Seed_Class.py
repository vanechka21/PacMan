global image=None #считать изображение
global big_image=None #считать большое изображение
class Seed:
    def __init__(self, image, big_image):
        self.posx = 9
        self.posy = 0
        self.pos = [self.posx, self.posy]
        self.size = 0
        self.count = 0
        self.is_active = True
        self.is_big=True


    def draw(self, big_image, image, count):
        # Прорисовка зерна
        raise NotImplemented
    def remove(self):
        raise NotImplemented