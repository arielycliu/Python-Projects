import pygame
pygame.init()
import random

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Egg Game")

CircleColor = (195, 253, 255)
CircleX, CircleY = 250, 425
CircleRadius = 30
CircleMove = 1.5
CircleMoveY = 0.5

class Eggs():
    def __init__(self, x):
        self.color = (255, 255, 255)
        self.x = x
        self.y = 0
        self.r = 25
        self.m = 1

    def drop(self):
        self.y += self.m

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def check(self):
        return (self.y > 535)


circles = []
start_ticks = pygame.time.get_ticks() #start timer

def redraw_game_window():
    screen.fill(000)
    # Main circle
    pygame.draw.circle(screen, CircleColor, (CircleX, CircleY), CircleRadius)
    pygame.display.flip()

    # Redraw circles
    global circles
    for c in circles:
        c.draw()
        c.drop()
        if c.check() == True:  # check if fallen below the screen
            circles.index(c)
            del circles[circles.index(c)]  # find index and remove circle
            print("Missed")

    pygame.display.update()

run = True
while run:
   
    # Check for window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Control main circle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and CircleX > 35:
        CircleX -= CircleMove
    if keys[pygame.K_RIGHT] and CircleX < 465:
        CircleX += CircleMove
    if keys[pygame.K_UP] and CircleY > 35:
        CircleY -= CircleMoveY
    if keys[pygame.K_DOWN] and CircleY < 465:
        CircleY += CircleMoveY

    sec = (pygame.time.get_ticks()-start_ticks)/1000 # Find seconds
    if sec > 9:
        start_ticks = pygame.time.get_ticks()  # start timer
        circles.append(Eggs(random.randint(35, 465)))

    redraw_game_window()

    pygame.time.delay(25)

pygame.quit()