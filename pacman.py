posx = 0
posy = 0
pos = [posx, posy]
image = None
score = 0
direction = (1, 0)
lives = 3


def move():
    raise NotImplemented


def step():
    move()
    check_ghost()
    check_seed()


def check_ghost():
    raise NotImplemented


def change_direction():
    raise NotImplemented


def draw(image):
    # Отрисовка пакмана.
    raise NotImplemented


def check_seed():
    raise NotImplemented