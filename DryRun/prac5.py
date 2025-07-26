import pygame as pg
import sys
import math


PURPLE = (222,55,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
WIDTH = 800
HEIGHT = 600


def translation(x,y,tx,ty):
    return(x+tx,y+ty)

def scaling(x,y,sx,sy):
    return(x*sx,y*sy)

def rot(x,y,ang):
    rad = math.radians(ang)
    xn=x*math.cos(rad)-y*math.sin(rad)
    yn = x*math.sin(rad)+y*math.cos(rad)
    return (xn,yn)



pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('2dtras')

def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        screen.fill(BLACK)
        
        x1 = 10
        y1 = 10
        x2 = 300
        y2 = 300
        pg.draw.line(screen, WHITE, (x1,y1), (x2,y2))
        # t1,t2 = translation(x1,y1,10,10)
        # t3,t4 = translation(x2,y2,10,10)
        # pg.draw.line(screen, PURPLE,(t1,t2), (t3,t4))
        
        
        
        s1,s2 = scaling(x1,y1,2,2)
        s3,s4 = scaling(x2,y2,2,2)
        # pg.draw.line(screen, PURPLE,(s1,s2), (s3,s4))
        
        r1,r2 = rot(x1,y1,21)
        r3,r4 = rot(x2,y2,21)
        pg.draw.line(screen, PURPLE,(r1,r2), (r3,r4))

        pg.display.flip()
        pg.time.delay(100)
        
main()

