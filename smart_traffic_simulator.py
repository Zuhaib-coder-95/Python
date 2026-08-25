import pygame
import random

pygame.init()

CAR_EVENT = pygame.USEREVENT + 1
LIGHT_EVENT = pygame.USEREVENT + 2

ROAD = pygame.Color("gray20")
WHITE = pygame.Color("white")
BLACK = pygame.Color("black")
RED = pygame.Color("red")
GREEN = pygame.Color("limegreen")
BLUE = pygame.Color("dodgerblue")
YELLOW = pygame.Color("gold")
PURPLE = pygame.Color("purple")
ORANGE = pygame.Color("orange")

class Car(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = 4

    def update(self):
        self.rect.x += self.speed

        if self.rect.left <= 0 or self.rect.right >= 600:
            self.speed *= -1
            pygame.event.post(pygame.event.Event(CAR_EVENT))
            pygame.event.post(pygame.event.Event(LIGHT_EVENT))

    def change_color(self):
        self.image.fill(random.choice([BLUE, YELLOW, PURPLE, ORANGE]))

def switch_light():
    global light_color
    if light_color == RED:
        light_color = GREEN
    else:
        light_color = RED

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Traffic Road Simulator")

car = Car(BLUE, 65, 30)
car.rect.x = 250
car.rect.y = 285

sprites = pygame.sprite.Group()
sprites.add(car)

light_color = RED
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == CAR_EVENT:
            car.change_color()

        elif event.type == LIGHT_EVENT:
            switch_light()

    sprites.update()

    screen.fill(ROAD)

    pygame.draw.rect(screen, pygame.Color("black"), (0, 260, 600, 110))

    for x in range(0, 600, 70):
        pygame.draw.rect(screen, YELLOW, (x, 310, 35, 4))

    pygame.draw.rect(screen, BLACK, (270, 35, 60, 120))
    pygame.draw.circle(screen, RED, (300, 65), 18)
    pygame.draw.circle(screen, GREEN, (300, 115), 18)

    pygame.draw.circle(screen, light_color, (300, 65 if light_color == RED else 115), 18)

    sprites.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()

