import pacman

pos = (0, 0)
direction = (1, 0)
image = None #удет добавлено позже
score = 0
lives = 3



def move():
    raise NotImplementedError      #  reqest to field (dir, pos) - next_pos


def check_ghost(self):
    # роверка на привидение
    # lifes -here
    #lifes - 0 games.run = false
    raise NotImplementedError


def check_seed():
    raise NotImplementedError

def step():
    move()
    check_ghost()
    check_seed()

def draw():
    # Отрисовка пакмана.
    pass

def change_direction(button):
    global pos
    pos = (9, 0)
    # считывает нажатие кнопки и меняет направление пакмана
    pass






