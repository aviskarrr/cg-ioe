import pygame as pg
import sys

WIDTH = 600
HEIGHT = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Midpoint Ellipse Drawing")

def mep(rx, ry, xc, yc):
    x = 0
    y = ry

    dx = 2*rx**2*y
    dy = 2*ry**2*x
    
    #reg1
    p1 = ry**2-rx**2*ry + (0.25*rx**2)
    while(dx<dy):
        if(p1<0):
            x = x+1
            y = y
            p1 = p1 + dx + ry**2
            dx = 2*rx**2*y
            dy = 2*ry**2*x
        else:
            x = x+1
            y = y-1
            p1 = p1+ dx-dy+ry**2
            dx = 2*rx**2*y
            dy = 2*ry**2*x
        plot_ellipse_points(xc,yc,x,y)
    #reg2
    p2 = (ry*ry * float(x+0.5)**2 + rx*rx * (y-1)**2) - rx*rx * ry*ry
    while(y>=0):
        if(p2>0):
            x = x
            y = y-1
            p2 = p2 - dy + rx**2
            dx = 2*rx**2*y
            dy = 2*ry**2*x
        else:
            x = x+1
            y = y-1
            p2 = p2+dx-dy+rx**2
            dx = 2*rx**2*y
            dy = 2*ry**2*x
        plot_ellipse_points(xc, yc, x, y)
            

def plot_ellipse_points(xc, yc, x, y):
    screen.set_at((round(xc + x), round(yc + y)), WHITE)
    screen.set_at((round(xc - x), round(yc + y)), WHITE)
    screen.set_at((round(xc + x), round(yc - y)), WHITE)
    screen.set_at((round(xc - x), round(yc - y)), WHITE)

def main():
    screen.fill(BLACK)
    mep(150, 100, WIDTH // 2, HEIGHT // 2)
    pg.display.flip()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pg.time.delay(100)

main()
