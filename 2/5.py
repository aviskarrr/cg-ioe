import pygame as pg
import sys
import math

WHITE = (222,255,255)
BLACK = (0,0,0)
WIDTH = 800
HEIGHT = 600



# def trans(x,y,tx,ty):
#     return (x+tx,y+ty)

# def scale(x,y,tx,ty):
#     return (x*tx,y*ty)

# def rot(x,y,ang):
#     ag = math.radians(ang)
#     xn = x*math.cos(ag)-y*math.sin(ag)
#     yn = x*math.sin(ag)+y*math.cos(ag)
#     return (xn,yn)
def rot(x,y,ang):
    rad = math.radians(ang)
    xnew = x*math.cos(rad)-y*math.sin(rad)
    ynew = x*math.sin(rad)+y*math.cos(rad)
    return xnew, ynew





pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("hello")






def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        screen.fill(WHITE)
        
        x1 = 30
        y1 = 30
        x2 = 300
        y2 = 300
        pg.draw.line(screen, BLACK,(x1,y1),(x2,y2))
        r1,r2 = rot(x1,y1,30)
        r3,r4 = rot(x2,y2,30)
        pg.draw.line(screen, BLACK, (r1,r2),(r3,r4) )
        # dda(12,12,112,112)
        pg.display.flip()
        pg.time.delay(100)
    



main()