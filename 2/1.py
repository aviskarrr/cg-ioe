import pygame as pg
import sys

WHITE = (222,255,255)
BLACK = (0,0,0)
WIDTH = 800
HEIGHT = 600

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("hello")

# def dda(x1,y1,x2,y2):
#     dx = abs(x2-x1)
#     dy = abs(y2-y1)

#     if(dx>dy):
#         steps = dx
#     else:
#         steps = dy
        
#     xinc = dx/steps
#     yinc = dy/steps

#     x =x1
#     y = y1
    
#     for i in range(int(steps)+1):
#         screen.set_at((round(x),round(y)), BLACK)
#         x = x+xinc
#         y = y + yinc



# def dda(x1,y1,x2,y2):
#     dx = abs(x2-x1)
#     dy = abs(y2-y1)
#     x = x1
#     y = y1
#     if(dx>dy):
#         step = dx
#     else:
#         step = dy
#     xinc = dx/step
#     yinc = dy/step
    
#     for i in range(int(step)+1):
#         screen.set_at((round(x),round(y)), BLACK)
#         x = x+xinc
#         y = y+yinc




def dda(x1,y1,x2,y2):
    
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    
    if(dx>dy):
        steps = dx
    else:
        steps = dy
    
    xinc = dx/steps
    yinc = dy/steps
    
    x = x1 
    y = y1
    
    for i in range(int(steps)+1):
        screen.set_at((round(x),round(y)), BLACK)
        x = x+xinc
        y = y+yinc

def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        screen.fill(WHITE)
        # screen.fill(BLACK)
        dda(12,12,112,112)
        pg.display.flip()
        pg.time.delay(100)
    



main()