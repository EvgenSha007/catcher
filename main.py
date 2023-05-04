from pygame import *
import random

font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, image1, player_x, player_y, player_speed, w=50, h=50):
        super().__init__()
        self.image = transform.scale(image.load(image1), (w, h)) 
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

# Рабочее пространство
screen_width = 400
screen_height = 400
screen = display.set_mode((screen_width, screen_height))
display.set_caption("Ловец яблок")
background = transform.scale(image.load("tree_bg.png"), (screen_width, screen_height))

# Настройка часов
clock = time.Clock()
FPS = 60

# Ввод цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Ввод игрока
player_width = 50
player_height = 50
player_x = screen_width / 2 - player_width / 2
player_y = screen_height - player_height
player_speed = 5
player = GameSprite("basket.png", player_x, player_y, player_speed)


# Рандомно падающее яблоко и его размеры
egg_width = 30
egg_height = 30
egg_x = random.randint(0, screen_width - egg_width)
egg_y = 0
egg_speed = 3


# Счет
score = 0
font_main = font.SysFont("Arial", 30)
font_fin = font.SysFont("Arial", 50)

# Победа проигрыш
lose = font_fin.render("Проигрыш!", True, (255, 0, 0))
win = font_fin.render("Победа!", True, (0, 255, 0))


# Основное игровой цикл
running = True
game = True
while running:
    # Обработка события
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                running = False


    screen.blit(background, (0, 0))
    
    if game:
        # Движение игрока
        keys = key.get_pressed()
        if keys[K_LEFT] and player.rect.x > 0:
            player.rect.x -= player_speed
        if keys[K_RIGHT] and player.rect.x < screen_width - player_width:
            player.rect.x += player_speed



        # Движение яблока
        egg_y += egg_speed



        # Поймано ли яблоко?
        if egg_y + egg_height > player.rect.y and egg_x + egg_width > player.rect.x and egg_x < player.rect.x + player_width:
            egg_x = random.randint(0, screen_width - egg_width)
            egg_y = 0
            score += 1
            egg_speed += 0.1



        # Не пропущено ли яблоко?
        if egg_y > screen_height:
            egg_x = random.randint(0, screen_width - egg_width)
            egg_y = 0
            score -= 1
            egg_speed -= 0.1

        # Победа \ проигрыш
        if score >= 50:
            screen.blit(win, (120, 200))
            display.update()
            game = False
            
        if score <= -5:
            screen.blit(lose, (100, 200))
            display.update()
            game = False

        # Изображение
        player.reset()
        draw.ellipse(screen, red, (egg_x, egg_y, egg_width, egg_height))
        score_text = font_main.render("Счёт: " + str(score), True, blue)
        screen.blit(score_text, (10, 10))
        
        
        display.update()
        clock.tick(FPS)

