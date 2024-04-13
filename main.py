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

while True:
    platform.draw_picture()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()