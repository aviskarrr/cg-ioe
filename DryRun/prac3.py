# import pygame as pg
# import sys
WHITE = (222,55,255)
BLACK = (0,0,0)
WIDTH = 800
HEIGHT = 600

# pg.init()
# screen = pg.display.set_mode((WIDTH,HEIGHT))
# pg.display.set_caption("MPC")


# def mpc(xc,yc,r):
#     points = []
    
#     x = 0
#     y = r
#     p = 1-r
    
#     while x<=y:
#         points.append((xc+x,yc+y))
#         points.append((xc+x,yc-y))
#         points.append((xc-x,yc+y))        
#         points.append((xc-x,yc-y))
        
#         points.append((xc+y,yc+x))
#         points.append((xc+y,yc-x))
#         points.append((xc-y,yc+x))        
#         points.append((xc-y,yc-x))
        
        
#         if p <0:
#             p = p+2*x+3

#         else:
#             p = p + 2*(x-y)+5
#             y = y-1
#         x = x+1
#     return points
    
    
    
# xc =WIDTH//2
# yc = HEIGHT//2
# r = 100
# circ_points = mpc(xc,yc,r)
# for point in circ_points:
#     screen.set_at(point,WHITE )
# pg.display.flip()

# def main():
#     while True:
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 pg.quit()
#                 sys.exit()
#         pg.display.flip()
#         pg.time.delay(100)
        
# screen.fill(BLACK)
# xc =WIDTH//2
# yc = HEIGHT//2
# r = 100
# circ_points = mpc(xc,yc,r)
# for point in circ_points:
#     screen.set_at(point,WHITE )
# # pg.display.flip()
        
        
# main()



import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("MPC")


def mpc(xc,yc,r):
    x = 0
    y = r
    p = 1-r
    points = []
    
    while x<=y:
        points.append((xc+x,yc+y))
        points.append((xc+x,yc-y))
        points.append((xc-x,yc+y))
        points.append((xc-x,yc-y))
        
        points.append((xc+y,yc+x))
        points.append((xc+y,yc-x))
        points.append((xc-y,yc+x))
        points.append((xc-y,yc-x))
        
        if (p<0):
            p = p + 2*x + 3
        else:
            p = p + 2* (x-y)+5
            y-=1
        x+=1
    return points    

screen.fill(BLACK)
xc = WIDTH//2
yc = HEIGHT//2
r = 100
circp = mpc(xc,yc,r)
for point in circp:
    screen.set_at(point,WHITE)
pg.display.flip()

def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pg.display.flip()
        pg.time.delay(100)


main()
