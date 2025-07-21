import pygame
import sys
WHITE = (222,55,255)
BLACK = (0,0,0)
WIDTH = 800
HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("ok")

# def bla(x1,y1,x2,y2):
#     dx= x2-x1
#     dy = y1-y1
    
#     x = x1
#     y = y1
    
#     if(x2>x1):
#         lx = 1
        
#     else:
#         lx = -1
    
#     if(y2>y1):
#         ly = 1
#     else:
#         ly = -1
        
#     if dx>dy:
#         p = 2*dy-dx
        
#         for i in range (dx +1):
#             if p<0:
#                 x = x+lx
#                 y = y
#                 p+=dy
#             else:
#                 x = x+lx
#                 y = y +ly
#                 p+=2*(dy-dx)




def bla(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    x = x1
    y = y1
    
    if(x2>x1):
        lx = 1
        
    else:
        lx = -1
        
    if (y2>y1):
        ly = 1
    else:
        ly = -1
    
    if dx>dy:
        p = 2*dy-dx
        for i in range(dx+1):
            if p<0:
                x = x+lx
                y = y
                p+=dy
            else:
                x = x+lx
                y = y+ly
                p+=2*(dy-dx)
            screen.set_at((x,y), WHITE)
    else:
        p = 2*dx-dy
        for i in range(dy+1):
            if p<0:
                y = y+ly
                x = x
                p +=dx
            else:
                y = y + ly
                x= x+lx
                p+=2*(dx-dy)
            screen.set_at((x,y), WHITE)
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(BLACK)
        bla(30,30,500,500)
        pygame.display.flip()
        pygame.time.delay(100)


if __name__=="__main__":
    main()