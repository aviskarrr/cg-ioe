# import pygame
# import sys

# BLCAK = (0,0,0)
# WHITE = (255,255,255)
# WIDTH = 800
# HEIGHT = 600



# pygame.init()
# screen = pygame.display.set_mode((WIDTH,HEIGHT))
# pygame.display.set_caption("DDA")



# def main():
#     while True:
#         for event in pygame.event.get():
#             if event.type==pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
        
#         screen.fill(BLCAK)
#         pygame.display.flip
#         pygame.time.delay(100)


# if __name__ == "__main__":
#     main()
            






# import pygame
# import sys

WHITE = (222,55,255)
BLACK = (0,0,0)
WIDTH = 800
HEIGHT = 600

# pygame.init()
# screen = pygame.display.set_mode((WIDTH,HEIGHT))
# pygame.display.set_caption("DDA")

# def main():
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
        
#         screen.fill(BLACK)
#         pygame.display.flip
#         pygame.time.delay(100)
    
    
# if __name__ == "__main__":
#     main()





import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("DDA")

# def main():
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
                
#         screen.fill(BLACK)
#         pygame.display.flip()
#         pygame.time.delay(100)


# if __name__ == "__main__":
#     main()




# def dda(x1,y1,x2,y2):
#     dx = x2-x1
#     dy = y2-y1
    
#     if(dx>dy):
#         steps= abs(dx)
#     else:
#         steps = abs(dy)

#     xinc = dx/steps
#     yinc = dy/steps
    
#     x = x1
#     y = y1
    
    
#     for i in range (int(steps)+1):
#         screen.set_at((round(x),round(y)), WHITE)
#         x = x + xinc
#         y = y+ yinc

# pygame.init()

# screen = pygame.display.set_mode((WIDTH,HEIGHT))
# pygame.display.set_caption("DD")


def dda(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    
    if(dx>dy):
        steps= abs(dx)
    else:
        steps = abs(dy)
        
    xinc = dx/steps
    yinc = dy/steps
    x = x1
    y = y1
    for i in range (int(steps)+1):
        screen.set_at((round(x),round(y)), WHITE)
        x = x+xinc
        y = y + yinc

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                

        screen.fill(BLACK)
        dda(25, 125, 700, 500)
        pygame.display.flip()
        pygame.time.delay(100)
        
if __name__ == "__main__":
    main()
    


