import pygame
import sys
import math

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Single Planet Orbit Simulation")
WHITE, BLACK = (255, 255, 255), (0, 0, 0)

clock = pygame.time.Clock()

# Orbit parameters
a = 150  # Major axis radius
b = 75   # Minor axis radius
angle = 0  # Starting angle
speed = 0.01  # Speed of revolution

# Sun position
cx, cy = WIDTH // 2, HEIGHT // 2

def draw_midpoint_ellipse(rx, ry, xc, yc):
    x = 0
    y = ry
    p1 = ry**2 - rx**2 * ry + 0.25 * rx**2
    dx = 2 * ry**2 * x
    dy = 2 * rx**2 * y

    while dx < dy:
        for sx, sy in [(1,1), (-1,1), (1,-1), (-1,-1)]:
            screen.set_at((round(xc + sx*x), round(yc + sy*y)), WHITE)
        if p1 < 0:
            x += 1
            dx = 2 * ry**2 * x
            p1 += dx + ry**2
        else:
            x += 1
            y -= 1
            dx = 2 * ry**2 * x
            dy = 2 * rx**2 * y
            p1 += dx - dy + ry**2

    p2 = ry**2 * (x + 0.5)**2 + rx**2 * (y - 1)**2 - rx**2 * ry**2
    while y >= 0:
        for sx, sy in [(1,1), (-1,1), (1,-1), (-1,-1)]:
            screen.set_at((round(xc + sx*x), round(yc + sy*y)), WHITE)
        if p2 > 0:
            y -= 1
            dy = 2 * rx**2 * y
            p2 += rx**2 - dy
        else:
            y -= 1
            x += 1
            dx = 2 * ry**2 * x
            dy = 2 * rx**2 * y
            p2 += dx - dy + rx**2

def main():
    global angle
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        pygame.draw.circle(screen, (255, 255, 0), (cx, cy), 20)

        draw_midpoint_ellipse(a, b, cx, cy)

        angle += speed
        planet_x = cx + a * math.cos(angle)
        planet_y = cy + b * math.sin(angle)

        pygame.draw.circle(screen, (0, 0, 255), (int(planet_x), int(planet_y)), 10)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
