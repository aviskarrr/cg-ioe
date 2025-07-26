import pygame as pg
import sys

WHITE = (222,255,255)
BLACK = (0,0,0)
WIDTH = 800
HEIGHT = 600

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("hello")


# def bla(x1,y1,x2,y2):
#     dx = abs(x2-x1)
#     dy = abs(y2-y1)
    
#     if(x2>x1):
#         lx = 1
#     else:
#         lx = -1
#     if(y2>y1):
#         ly = 1
#     else:
#         ly =-1
    
#     x = x1
#     y = y1

    
#     if(dx>dy):
#         p = 2*dy-dx
#         for i in range (dx+1):

#             if(p<0):
#                 x = x+lx
#                 y = y
#                 p = p + 2*dy
#             else: 
#                 x=x+lx
#                 y = y+ly
#                 p = p+2*(dy-dx)
#             screen.set_at((x,y), BLACK)
        
#     else:
#         p = 2*dx-dy
#         for i in range (dy+1):

#             if(p<0):
#                 x = x
#                 y = y+ly
#                 p = p + 2*dx
#             else: 
#                 x=x+lx
#                 y = y+ly
#                 p = p+2*(dx-dy)
#             screen.set_at((x,y), BLACK)










# def bla(x1,y1,x2,y2):
#     dx = abs(x2-x1)
#     dy = abs(y2-y1)
    
#     if(x2>x1):
#         lx=1
#     else:
#         lx = -1
        
#     if(y2>y1):
#         ly = 1
#     else:
#         ly = -1
#     x = x1
#     y = y1
#     if(dx>dy):
#         p = 2*dy-dx
#         for i in range (dx+1):
#             if(p<0):
#                 x = x+lx
#                 y = y
#                 p = p+2*dy
#             else:
                
#                 x = x+lx
#                 y=y+ly
#                 p = p+2*(dy-dx)
#             screen.set_at((x,y), BLACK)
            
#     else:
#         p = 2*dx-dy
#         for i in range (dy+1):
#             if(p<0):
#                 x = x
#                 y = y+ly
#                 p = p+2*dx
#             else:
                
#                 x = x+lx
#                 y=y+ly
#                 p = p+2*(dx-dy)
#             screen.set_at((x,y), BLACK)






def bla(x1,y1,x2,y2):
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    
    if(x2>x1):
        lx = 1
    else:
        lx = -1
    if(y2>y1):
        ly = 1
    else:
        ly = -1
    
    x = x1
    y= y1
    
    if(dx>dy):
        p = 2*dy-dx
        for i in range (dx+1):
            if(p<0):
                x = x+lx
                y = y
                p = p+2*dy
            else:
                x = x+lx
                y = y+ly
                p=p+2*(dy-dx)
            screen.set_at((x,y), BLACK)
    else:
        p = 2*dx-dy
        for i in range (dy+1):
            if(p<0):
                x = x
                y = y+ly
                p = p+2*dx
            else:
                x = x+lx
                y = y+ly
                p=p+2*(dx-dy)
            screen.set_at((x,y), BLACK)

def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        screen.fill(WHITE)
        # screen.fill(BLACK)
        # dda(12,12,112,112)
        bla(12,12,122,122)
        pg.display.flip()
        pg.time.delay(100)
    



main()