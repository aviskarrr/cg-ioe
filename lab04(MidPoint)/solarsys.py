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

xx,yy,rr = WIDTH // 2, HEIGHT // 2, 10
xc, yc, r = WIDTH // 2, HEIGHT // 2, 100
xc2, yc2, r2 = WIDTH // 2, HEIGHT // 2, 150
xc3, yc3, r3 = WIDTH // 2, HEIGHT // 2, 200
xc4, yc4, r4 = WIDTH // 2, HEIGHT // 2, 250

#planet 1 



circle_points = mid_point_circle(xc, yc, r)
for point in circle_points:
    screen.set_at(point, WHITE) #orb 1
    
for point in mid_point_circle(xc2, yc2, r2):
    screen.set_at(point, WHITE) #orb 2
    
for point in mid_point_circle(xc3, yc3, r3):
    screen.set_at(point, WHITE) #orb 3
for point in mid_point_circle(xc4, yc4, r4):
    screen.set_at(point, WHITE) #orb 4
for point in mid_point_circle(xx, yy, rr):
    screen.set_at(point, WHITE) #orb 4
    
    



pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.time.delay(100)
