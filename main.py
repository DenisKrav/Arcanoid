import pygame
import sys

pygame.init()

back = (171, 209, 181)
screenWidth = 600
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
screen.fill(back)

clock = pygame.time.Clock()

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=(156, 37, 134)):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def change_color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(screen, self.fill_color, self.rect)

class Picture(Area):
    def __init__(self, fileName, x=0, y=0, width=10, height=10, color=(156, 37, 134)):
        Area.__init__(self, x, y, width, height, color)
        self.image = pygame.transform.scale(pygame.image.load(fileName), (width, height))

    def draw_picture(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Label(Area):
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        super().__init__(x, y, width, height, color)

    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.text = text
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw_text(self, shift_x=0, shift_y=0):
        self.fill()
        screen.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

platform = Picture("images/platform.png", int(screenWidth * 0.35), int(screenHeight * 0.8), 200, 50, (209, 161, 209))
platform_speed = 10

enemies = []
num_rows = 6
num_columns = 15
enemy_width = 30
enemy_height = 30
enemy_padding = 9
start_x = 10
start_y = 10
for row in range(num_rows):
    for column in range(num_columns):
        x = start_x + column * (enemy_width + enemy_padding)
        y = start_y + row * (enemy_height + enemy_padding)
        new_enemy = Picture("images/enemy.png", x, y, enemy_width, enemy_height, (209, 161, 209))
        enemies.append(new_enemy)
enemy_count = enemy_width * enemy_height #################################3

ball = Picture("images/ball.png", screenWidth * 0.5, screenHeight * 0.5, enemy_width, enemy_height, (209, 161, 209))
ball_speed_x = 5
ball_speed_y = -5

while True:
    screen.fill(back)
    platform.draw_picture()

    for enemy in enemies:
        enemy.draw_picture()

    ball.draw_picture()

    ball.rect.x += ball_speed_x
    ball.rect.y += ball_speed_y

    if ball.rect.left <= 0 or ball.rect.right >= screenWidth:
        ball_speed_x = -ball_speed_x
    if ball.rect.top <= 0:
        ball_speed_y = -ball_speed_y

    if ball.rect.colliderect(platform.rect):
        ball_speed_y = -ball_speed_y

    for enemy in enemies:
        if ball.rect.colliderect(enemy.rect):
            enemies.remove(enemy)
            ball_speed_y = -ball_speed_y
            break

    if ball.rect.bottom >= screenHeight or len(enemies) == 0:
        pygame.quit()
        sys.exit()

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and platform.rect.x + platform.rect.width != screenWidth:
        platform.rect.x += platform_speed
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and platform.rect.x != 0:
        platform.rect.x -= platform_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(40)
    pygame.display.update()