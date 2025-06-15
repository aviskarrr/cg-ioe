# to implement mid point circle algorithm 
import pygame
import sys
def mid_point_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    points = []

    while x <= y:
        points.append((xc + x, yc + y))
        points.append((xc - x, yc + y))
        points.append((xc + x, yc - y))
        points.append((xc - x, yc - y))
        points.append((xc + y, yc + x))
        points.append((xc - y, yc + x))
        points.append((xc + y, yc - x))
        points.append((xc - y, yc - x))

        if p < 0:
            p += 2 * x + 3
        else:
            p += 2 * (x - y) + 5
            y -= 1
        x += 1

    return points

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Circle Algorithm")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen.fill(BLACK)
xc, yc, r = WIDTH // 2, HEIGHT // 2, 100
circle_points = mid_point_circle(xc, yc, r)
for point in circle_points:
    screen.set_at(point, WHITE)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.time.delay(100)
