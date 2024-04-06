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



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()