import pygame as pg
import sys


WHITE = (222,255,255)
BLACK = (0,0,0)
WIDTH = 800
HEIGHT = 600

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("hello")



# def circ(xc,yc,r):
#     x = 0
#     y = r
#     p = 1-r
#     points = []
#     while(x<=y):
#         points.append(((xc+x), (yc+y)))
#         points.append(((xc+x), (yc-y)))
#         points.append(((xc-x), (yc+y)))
#         points.append(((xc-x), (yc-y)))
        
#         points.append(((xc+y), (yc+x)))
#         points.append(((xc+y), (yc-x)))
#         points.append(((xc-y), (yc+x)))
#         points.append(((xc-y), (yc-x)))
        
#         if(p<0):
#             p = p+2*x+3
#         else:
#             p = p+2*(x-y)+5
#             y = y-1
#         x = x+1
    
#     return points





# def circ(x,y,r):
#     x = 0
#     y = r
#     p = 1-r
#     points=[]
#     while(x<=y):
#         points.append((xc+x,yc+y))
#         points.append((xc+x,yc-y))
#         points.append((xc-x,yc+y))
#         points.append((xc-x,yc-y))
        
        
#         points.append((xc+y,yc+x))
#         points.append((xc+y,yc-x))
#         points.append((xc-y,yc+x))
#         points.append((xc-y,yc-x))
        
#         if(p<0):
#             p = p+2*x+3
#         else:
#             p = p+2*(x-y)+5
#             y-=1
#         x+=1
#     return points





def circ(xx,yy,r):
    x= 0
    y = r
    p = 1-r
    points =[]
    while(x<=y):
        points.append((xx+x,yy+y))
        points.append((xx+x,yy-y))
        points.append((xx-x,yy+y))
        points.append((xx-x,yy-y))


        points.append((xx+y,yy+x))
        points.append((xx+y,yy-x))
        points.append((xx-y,yy+x))
        points.append((xx-y,yy-x))
        
        if(p<0):
            p = p+2*x+3
        else:
            p = p+2*(x-y)+5
            y = y-1
        x = x+1
        
    return points

xc = WIDTH//2
yc = HEIGHT//2
r = 100
cc = circ(xc,yc,r)
print(cc)
screen.fill(WHITE)
for point in cc:
    screen.set_at(point, BLACK)
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