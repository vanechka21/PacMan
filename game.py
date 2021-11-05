screen_size = [720, 980]

def main():
    global points, max_points, x_pos_p, y_pos_p, seeds, life_count
    player = Pacman() #Нужен класс пакмана
    life_count=3 # Количество жизней. Как измененять количество я пока не знаю, т.к. нет класса пакмана и призрака
    points=0
    font = pygame.font.Font('freesansbold.ttf', 20)
    run = True
    def __init__(self):
        self.screen = pygame.display.set_mode(Game.screen_size)

    def score():
        global points
        points += 1

        text = font.render("Points: " + str(points), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (600, 40)
        screen_size.blit(text, textRect)

    def pre_start_loop(self):
         raise NotImplemented #Нет смысла отрисовывать игру до момента нажатия пробела. Всё отрисовывается моментально.

    while run: # Это game_loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((0, 0, 0))
        userInput = pygame.key.get_pressed() #Ввод с клавиатуры

        player.update(userInput) #При нажатие клавиши изменить направление

        score()
        pygame.display.flip()
        pygame.time.delay(80)

def menu(life_count):
    global points, max_points
    run = True
    while run:
        SCREEN.fill((0, 0, 0))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if life_count == 3:
            text = font.render("Press any Key to Start", True, (255, 255, 0))
        elif life_count == 0:
            text = font.render("Press any Key to Restart", True, (255, 255, 0))
            if points>max_points:
                max_points = points
            max_score = font.render("Maximum Score: " + str(max_points), True, (255, 255, 0))
            score = font.render("Your Score: " + str(points), True, (255, 255, 0))
            scoreRect = max_score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
            SCREEN.blit(max_score, scoreRect)
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()

