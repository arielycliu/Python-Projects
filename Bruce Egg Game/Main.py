import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Egg Game")

CircleColor = (255, 255, 255)
CircleX, CircleY = 250, 425
CircleRadius = 30
CircleMove = 0.7
CircleMoveY = 0.3

class Eggs():
    def __init__(self, x, y, r, m):
        self.color = (255, 255, 255)
        self.x = x
        self.y = y
        self.r = r
        self.m = m

    def Drop(self):
        self.y += self.m



run = True
while run:

    # Check for window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and CircleX > 35:
        CircleX -= CircleMove
    if keys[pygame.K_RIGHT] and CircleX < 465:
        CircleX += CircleMove
    if keys[pygame.K_UP] and CircleY > 35:
        CircleY -= CircleMoveY
    if keys[pygame.K_DOWN] and CircleY < 465:
        CircleY += CircleMoveY

    screen.fill((0,0,0))
    pygame.draw.circle(screen, CircleColor, (CircleX, CircleY) , CircleRadius)
    pygame.display.update()
pygame.quit()