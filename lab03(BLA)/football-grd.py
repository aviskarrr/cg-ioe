#implementation of BLA algorithm in Python
import pygame
import sys


def BLA(x1, y1, x2, y2):
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    x = x1
    y = y1
    
    if(x2> x1):
        lx = 1
    else:
        lx = -1
        
    if(y2 > y1):
        ly = 1
    else:
        ly = -1
    
    if dx > dy:
        p = 2*dy-dx
        
        for i in range(dx+1):
            if p<0:
                x = x+lx
                y = y
                p = p + 2*dy
            else:
                x = x + lx
                y = y + ly
                p = p + 2*(dy - dx)
            
            screen.set_at((round(x), round(y)), WHITE)#plot(int(x), int(y))
    else:
        p = 2*dx-dy
            
        for i in range(dy+1):
            if p<0:
                x = x
                y = y + ly
                p = p + 2*dx
            else:
                x = x + lx
                y = y + ly
                p = p + 2*(dx - dy)
                
            screen.set_at((round(x), round(y)), WHITE)


pygame.init()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Bresenham's Line Algorithm")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 100)

#making a football field like design using BLA algorithm

def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        
        screen.fill(GREEN)
        #draw the football field
        BLA(100, 100, 700, 100)
        BLA(100, 500, 700, 500)
        BLA(100, 100, 100, 500)
        BLA(700, 100, 700, 500)   
        #make center circle
        pygame.draw.circle(screen, WHITE, (400, 300), 50, 1)
        #draw center line
        BLA(400, 100, 400, 500)
        
        pygame.display.flip()
        pygame.time.delay(100)

if __name__ == "__main__":
    main()
