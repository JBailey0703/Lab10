import random
import pygame

#first commit
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        x, y = 0, 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click_x, click_y = event.pos
                    if click_x // 32 * 32 == x and click_y // 32 * 32 == y:
                        x, y = random.randrange(1, 20)*32, random.randrange(1, 16)*32
            screen.fill("light blue")
            for i in range(1, 20):
                pygame.draw.line(screen, "black", (i*32, 0), (i*32, 512))
            for i in range(1, 16):
                pygame.draw.line(screen, "black", (0, i*32), (640, i*32))
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
