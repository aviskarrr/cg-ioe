import pygame
import sys

def midpointEllipse(rx,ry,xc,yc):
    x = 0
    y = ry
    p1 = ry * ry - rx * rx * ry + 0.25 * rx * rx
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y
    while(dx < dy):
        if(p1<0):
            x = x+1
            y= y
            p1 = p1+ dx + ry * ry
            dx = 2 * ry * ry * x
            dy = 2 * rx * rx * y

        else:
            x = x+1
            y =y-1  
            p1 = p1 + dx - dy + ry * ry
            dy = 2 * rx * rx * y
            dx = 2 * ry * ry * x


        screen.set_at((round(xc + x), round(yc + y)), WHITE)
        screen.set_at((round(xc - x), round(yc + y)), WHITE)
        screen.set_at((round(xc + x), round(yc - y)), WHITE)
        screen.set_at((round(xc - x), round(yc - y)), WHITE)
            
    p2 = ry * ry* (x+ 0.5) * (x+0.5) + rx*rx*(y-1)*(y-1)-rx*rx*ry*ry
    
    while(y!=0):
        if(p2>0):
            x = x
            y = y-1
            p2 = p2 + rx * rx - dy
            dy = 2 * rx * rx * y
            dx = 2 * ry * ry * x

        else:
            x = x+1
            y = y-1
            p2 = p2 + dx - dy + rx * rx
            dy = 2 * rx * rx * y
            dx = 2 * ry * ry * x
        
        screen.set_at((round(xc + x), round(yc + y)), WHITE)
        screen.set_at((round(xc - x), round(yc + y)), WHITE)
        screen.set_at((round(xc + x), round(yc - y)), WHITE)
        screen.set_at((round(xc - x), round(yc - y)), WHITE)


pygame.init()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Midpoint Ellipse Algorithm")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        midpointEllipse(160, 160, 400, 300)
        pygame.display.flip()
        pygame.time.delay(100)

if __name__ == "__main__":
    main()