import time
import pygame
import random

pygame.init()
canvas = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Nikus Snake Game")

grey = (138, 138, 138)
white = (255, 255, 255)
red = (255, 0, 0)


clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont(None, 35)

snake_size = 10
snake_speed = 20


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, red)
    canvas.blit(value, [0, 0])


def our_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(canvas, grey, [x[0], x[1], snake_size, snake_size])


def message(msg, colour):
    mesg = font_style.render(msg, True, colour)
    canvas.blit(mesg, [160, 200])

def gameLoop():
    game_over = False
    game_close = False

    x1 = 250
    y1 = 250

    x1_change = 0
    y1_change = 0

    snake_List = []
    snake_Lenght = 1

    foodx = round(random.randrange(0, 500 - 10) / 10) * 10
    foody = round(random.randrange(0, 500 - 10) / 10) * 10

    while not game_over:

        while game_close == True:
            canvas.fill(white)
            message("You Lost! Press Q to quit or P to play again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0

        if x1 >= 500 or x1 < 0 or y1 >= 500 or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        canvas.fill(white)
        pygame.draw.rect(canvas, red, [foodx, foody, 10, 10])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > snake_Lenght:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_size, snake_List)
        your_score(snake_Lenght - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, 500 - snake_size) / 10) * 10
            foody = round(random.randrange(0, 500 - snake_size) / 10) * 10
            snake_Lenght += 1


        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()