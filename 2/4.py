import pygame as pg
import sys


WHITE = (222,255,255)
BLACK = (0,0,0)
WIDTH = 800
HEIGHT = 600

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("hello")




# def ellipse(xc,yc,rx,ry):
#     x = 0
#     y = ry
#     dx = 2*ry*ry*x
#     dy = 2*rx*rx*y
#     p1 = ry*ry-rx*rx*ry+rx*rx*0.25
#     while(dx<dy):

#         if(p1<0):
#             x = x+1
#             y = y
#             p1 = p1+ dx+ry*ry
#             dx = 2*ry*ry*x
#             dy = 2*rx*rx*y
#         else:
#             x = x+1
#             y = y-1
#             p1 = p1+dx-dy+ry*ry
#             dx = 2*ry*ry*x
#             dy = 2*rx*rx*y
            
#         screen.set_at((round(xc+x),round(yc+y)), WHITE)
#         screen.set_at((round(xc+x),round(yc-y)), WHITE)
#         screen.set_at((round(xc-x),round(yc+y)), WHITE)
#         screen.set_at((round(xc-x),round(yc-y)), WHITE)
#     p2= ry*ry * (x+0.5)*(x+0.5)+rx*rx*(y-1)*(y-1)-rx*rx*ry*ry
#     while (y>=0):

#         if(p2>0):
#             x = x
#             y = y-1
#             p2 = p2-dy+rx*rx
#             dx = 2*ry*ry*x
#             dy = 2*rx*rx*y
#         else:
#             x = x+1
#             y = y-1
#             p2 = p2+dx-dy+rx*rx
#             dx = 2*ry*ry*x
#             dy = 2*rx*rx*y
#         screen.set_at((round(xc+x),round(yc+y)), WHITE)
#         screen.set_at((round(xc+x),round(yc-y)), WHITE)
#         screen.set_at((round(xc-x),round(yc+y)), WHITE)
#         screen.set_at((round(xc-x),round(yc-y)), WHITE)














# def ellipse(xc,yc,rx,ry):
#     x =0
#     y= ry
#     dx = 2*ry*ry*x
#     dy = 2*rx*rx*y
#     #reg1
#     p1 = ry*ry-rx*rx*ry+0.25*rx*rx
#     while(dx<dy):
#         if(p1<0):
#             x = x+1
#             y = y
#             p1 = p1+dx+ry*ry
#             dx = 2*ry*ry*x
#             dy = 2*rx*rx*y
#         else:
#             x = x+1
#             y = y-1
#             p1 = p1+dx-dy+ry*ry
#             dx = 2*ry*ry*x
#             dy = 2*rx*rx*y
#         screen.set_at((xc+x,yc+y), WHITE)
#         screen.set_at((xc+x,yc-y), WHITE)
#         screen.set_at((xc-x,yc+y), WHITE)
#         screen.set_at((xc-x,yc-y), WHITE)

#     p2 = ry*ry*(x+0.5)*(x+0.5)+rx*rx*(y-1)*(y-1)-rx*rx*ry*ry
#     while(y>=0):
#         if(p2>0):
#             x=x
#             y = y-1
#             p2 = p2-dy+rx*rx
#             dx = 2*ry*ry*x
#             dy = 2*rx*rx*y
#         else:
#             x = x+1
#             y = y-1
#             p2 = p2+dx-dy+rx*rx
#             dx = 2*ry*ry*x
#             dy = 2*rx*rx*y
#         screen.set_at((xc+x,yc+y), WHITE)
#         screen.set_at((xc+x,yc-y), WHITE)
#         screen.set_at((xc-x,yc+y), WHITE)
#         screen.set_at((xc-x,yc-y), WHITE)










# def ellipse(xx,yy,rx,ry):
#     x = 0
#     y  = ry
#     dx = 2*ry*ry*x
#     dy = 2*rx*rx*y
#     p1 = ry*ry-rx*rx*ry+0.25*rx*rx
#     while(dy>dx):
#         if(p1<0):
#             x = x+1
#             y = y
#             p1 = p1+dx+ry*ry
#             dx = 2*ry*ry*x
#             dy = 2*rx*rx*y
#         else:
#             x = x+1
#             y = y-1
#             p1 = p1+dx-dy+ry*ry
#             dx = 2*ry*ry*x
#             dy = 2*rx*rx*y
#         screen.set_at((round(xx+x), round(yy+y)),WHITE)
#         screen.set_at((round(xx-x), round(yy+y)),WHITE)
#         screen.set_at((round(xx+x), round(yy-y)),WHITE)
#         screen.set_at((round(xx-x), round(yy-y)),WHITE)
#     p2 = ry*ry*(0.5+x)*(0.5+x)+rx*rx*(y-1)*(y-1)-rx*rx*ry*ry
    
#     while(y>=0):
#         if(p2>0):
#             x = x
#             y = y-1
#             p2 = p2-dy+rx*rx
#             dx = 2*ry*ry*x
#             dy = 2*rx*rx*y
#         else:
#             x = x+1
#             y = y-1
#             p2 = p2+dx-dy+rx*rx
#             dx = 2*ry*ry*x
#             dy = 2*rx*rx*y 
#         screen.set_at((round(xx+x), round(yy+y)),WHITE)
#         screen.set_at((round(xx-x), round(yy+y)),WHITE)
#         screen.set_at((round(xx+x), round(yy-y)),WHITE)
#         screen.set_at((round(xx-x), round(yy-y)),WHITE)
















def ellipse(xc,yc,rx,ry):
    x = 0
    y = ry
    p1 = ry*ry-rx*rx*ry+0.25*rx*rx
    
    dx = 2*ry*ry*x
    dy = 2*rx*rx*y
    
    while(dx<dy):
        if(p1<0):
            x=x+1
            y=y
            p1 = p1+dx+ry*ry
            dx = 2*ry*ry*x
            dy = 2*rx*rx*y
        else:
            x = x+1
            y = y-1
            p1 = p1+dx-dy+ry*ry
            dx = 2*ry*ry*x
            dy = 2*rx*rx*y
        screen.set_at((round(xc+x),round(yc+y)), BLACK)
        screen.set_at((round(xc-x),round(yc+y)), BLACK)
        screen.set_at((round(xc+x),round(yc-y)), BLACK)
        screen.set_at((round(xc-x),round(yc-y)), BLACK)
    
    p2 = ry*ry*(x+0.5)*(x+0.5)+rx*rx*(y-1)*(y-1)-rx*rx*ry*ry
    while(y>=0):
        if(p2>0):
            x = x
            y=y-1
            p2 = p2-dy+rx*rx
            dx = 2*ry*ry*x
            dy = 2*rx*rx*y
        else:
            x = x+1
            y = y-1
            p2 = p2+dx-dy+rx*rx #probable mistake place hehe, care if its either * or +
            dx = 2*ry*ry*x
            dy = 2*rx*rx*y
        screen.set_at((round(xc+x),round(yc+y)), BLACK)
        screen.set_at((round(xc-x),round(yc+y)), BLACK)
        screen.set_at((round(xc+x),round(yc-y)), BLACK)
        screen.set_at((round(xc-x),round(yc-y)), BLACK)
def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        screen.fill(WHITE)
        ellipse(WIDTH//2,HEIGHT//2,30,50)
        pg.display.flip()
        pg.time.delay(100)
        
        




main()