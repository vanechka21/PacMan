"""Это по большей степени ПсевдоКод - поэтому он грубый, даже очень"""


class Ghost:
    def __init__(self, image, map, coords_x, coords_y):
        self.coords = (coords_x, coords_y)
        self.size = [15, 15]
        self.speed = 5
        self.map = map
        self.image = image
        self.state = 0
        self.direction = (0, 0)
        self.ways = ((0, 0), (0, 0))  # - параметры путей при развилке (лево, право) и (вверх, вниз)

    def moving_scared(self, speed, image):
        self.image = image  # Либо Наш массив с имиджими загружаем позицию 2 с набором картинок
        self.state = 1
        self.speed = int(speed / 1.5)
        self.I_AM_Scared()
        self.moving()
        self.draw()
        raise NotImplemented
        # //Меняется картинка

    # //Скорость уменьшается примерно в полтора раза
    # //Приведение теперь должно двигаться от пакмена, и по возможности избегать других призраков
    # Пока что не избегает других призраков !!!!

    def I_AM_Scared(self):
        ### Мы наоборот берём наибольшее расстояние и пытаемся его увеличить (если это возможно)
        # Можно потом объеденить с приследованием с помощью статуса
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        px, py = GetPlayersCoordinates()
        if (abs(self.coords[1] - px) > abs(self.coords[2] - py)):
            if (self.coords[2] - py < 0):
                self.direction = dirs[2]
            else:
                self.direction = dirs[3]
        else:
            if self.coords[1] - px < 0:
                self.direction = dirs[0]
            else:
                self.direction = dirs[1]

    def back_to_normal(self):
        # после окончания зерна Энерджайзера меняет состояние на обычное
        self.status = 0
        self.speed = self.speed * 2

    def moving_persecution(self):
        # Мы берём наибольшее расстояние до пакмана и пытаемся его уменьшить если это возможно
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        px, py = GetPlayersCoordinates()
        if (abs(self.coords[1] - px) < abs(self.coords[2] - py)):
            if (self.coords[2] - py < 0):
                self.direction = dirs[3]
            else:
                self.direction = dirs[2]
        else:
            if self.coords[1] - px < 0:
                self.direction = dirs[1]
            else:
                self.direction = dirs[0]
        self.moving()
        raise NotImplemented
        # получает координаты пакмана и выбирает плоскость(координаты пакмана - координаты призрака )

    # с наибольшим отрывом, после чего стремится к пакману

    def moving(self):
        # Просто Двигает Пакмана и всё
        for i in range(2):
            self.coords[i] = self.direction[i] * self.speed
        raise NotImplemented

    def OnTheCorner(self, map):
        # когда призрак на перекрётске должна запускаться эта функция
        # где она проверяет возможные пути изменяя параметры self.ways
        # Пока делаю ifа'mi поскольку более эффективных идей нет, которые будут рабоать не благодаря костылям
        if (self.coords[0] + 1 != Collision):
            self.ways[0][1] = 1
        if (self.coords[0] - 1 != Collision):
            self.ways[0][0] = 1
        if (self.coords[1] + 1 != Collision):
            self.ways[1][1] = 1
        if (self.coords[0] - 1 != Collision):
            self.ways[1][0] = 1

        raise NotImplemented

    def CheckIfOnTheCorner(self, map):
        # проверяет находимся  ли мы в на перекрёстке  или в углу или нет
        # Вариант реализации 1 - map - список координат перекрёстков мы проходимся по нему
        # И сравниваем его с нашими координатами
        # Вариант реализации 2 - Мы постоянно проверяем окружения призраков (невыгодно со
        # стороны эффективности (можно как объеденить этот вариант в одну функцию, там и заменить))
        ##1
        for i in map:
            if self.coords == i:
                OnTheCorner()

        raise NotImplemented

    def draw(self):
        if self.status:
            draw_ghost(self.imgage[1])
            return
        draw_ghost(self.image[0])

        # Просто рисуем призрака и всё по картинкам
        raise NotImplemented

    """ Модифицировал класс Стёпы, спасибо ему за наработки!!!! """
