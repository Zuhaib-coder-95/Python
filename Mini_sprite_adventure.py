import pygame

def main():
    pygame.init()

    screen_width, screen_height = 700, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Crystal Quest")

    x, y = 320, 220
    sprite_width, sprite_height = 50, 50
    speed = 5

    DARK_PURPLE = (25, 10, 45)
    PURPLE = (150, 50, 255)
    PINK = (255, 70, 180)
    BLUE = (50, 180, 255)
    CYAN = (50, 255, 230)
    YELLOW = (255, 230, 50)
    WHITE = (255, 255, 255)
    GREEN = (70, 255, 120)

    current_color = PURPLE
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            x -= speed
        if pressed[pygame.K_RIGHT]:
            x += speed
        if pressed[pygame.K_UP]:
            y -= speed
        if pressed[pygame.K_DOWN]:
            y += speed

        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)

        if x == 0:
            current_color = CYAN
        elif x == screen_width - sprite_width:
            current_color = PINK
        elif y == 0:
            current_color = YELLOW
        elif y == screen_height - sprite_height:
            current_color = GREEN
        else:
            current_color = PURPLE

        screen.fill(DARK_PURPLE)

        pygame.draw.circle(screen, WHITE, (70, 70), 3)
        pygame.draw.circle(screen, WHITE, (180, 120), 3)
        pygame.draw.circle(screen, WHITE, (570, 80), 3)
        pygame.draw.circle(screen, WHITE, (630, 200), 3)
        pygame.draw.circle(screen, WHITE, (100, 400), 3)
        pygame.draw.circle(screen, WHITE, (520, 420), 3)

        pygame.draw.circle(screen, BLUE, (120, 150), 40)
        pygame.draw.circle(screen, CYAN, (580, 350), 45, 5)
        pygame.draw.circle(screen, PINK, (600, 100), 15)
        pygame.draw.circle(screen, YELLOW, (100, 330), 15)

        player_rect = pygame.Rect(x, y, sprite_width, sprite_height)
        pygame.draw.rect(screen, current_color, player_rect)

        pygame.draw.circle(screen, WHITE, (int(x + 25), int(y + 15)), 7)
        pygame.draw.circle(screen, DARK_PURPLE, (int(x + 25), int(y + 35)), 5)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()