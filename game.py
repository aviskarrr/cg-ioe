import pygame
import time
import random

# Initialize
pygame.init()

# Screen settings
width = 600
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game with Sound Fix')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Snake settings
snake_block = 10
snake_speed = 15

# Fonts
font = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Load sounds
# eat_sound = pygame.mixer.Sound("eat.wav")
# gameover_sound = pygame.mixer.Sound("gameover.wav")

# Clock
clock = pygame.time.Clock()

def show_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    window.blit(value, [0, 0])

def message(msg, color):
    mesg = font.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])

def game_over_screen(score):
    window.fill(black)
    message("You Lost! Press Q-Quit or C-Play Again", red)
    show_score(score)
    pygame.display.update()

    gameover_sound.play()  # Play once here only

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    waiting = False

def gameLoop():
    x = width / 2
    y = height / 2
    x_change = 0
    y_change = 0

    snake_List = []
    Length_of_snake = 1
    score = 0

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        x += x_change
        y += y_change

        if x >= width or x < 0 or y >= height or y < 0:
            game_over_screen(score)
            return gameLoop()

        window.fill(black)
        pygame.draw.rect(window, red, [foodx, foody, snake_block, snake_block])

        snake_Head = [x, y]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for segment in snake_List[:-1]:
            if segment == snake_Head:
                game_over_screen(score)
                return gameLoop()

        draw_snake(snake_block, snake_List)
        show_score(score)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 10
            # eat_sound.play()

        clock.tick(snake_speed)

# Start the game
gameLoop()