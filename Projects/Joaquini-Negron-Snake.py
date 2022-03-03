# create the screen
import pygame as pg
import time
import random
pg.init()

yellow = (179, 178, 70)# score
purple = (154, 59, 255)# snake
red = (255, 59, 91)# food
green = (0, 80, 34)# background
light_green = (0, 232, 101)# game over


dis_width = 800
dis_height = 700

dis=pg.display.set_mode((dis_width,dis_height))
pg.display.set_caption("Snake game by MF")
game_over=False

 
clock = pg.time.Clock()
snake_speed = 20
snake_block = 10

 

font_style = pg.font.SysFont(None, 25)

 
def my_snake(snake_block, snake_list):
    for x in snake_list:
        pg.draw.rect(dis, purple, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2.5, dis_height/2])

def thescore(score):
    value = font_style.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0,0])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    snake_List = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
    foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10

    while not game_over:
        while game_close == True:
            dis.fill(green)
            message("YOU DIED. Press Q to quit and P to play again.", red)
            thescore(length_of_snake -1)
            pg.display.update()

            for event in pg.event.get():
                if event.type==pg.KEYDOWN:
                    if event.key == pg.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pg.K_q:
                        gameLoop()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over == True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pg.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pg.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pg.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(green)
        # pg.draw.rect(dis, purple, [x1, y1, snake_block, snake_block])
        pg.draw.rect(dis, red,[foodx, foody, snake_block, snake_block])
        
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]
        
        for x in snake_List[: -1]:
            if x  == snake_head:
                game_close == True
        
        my_snake(snake_block, snake_List)
        thescore(length_of_snake -1)

        pg.display.update()

        if x1  == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
            foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10
            length_of_snake +=1

        clock.tick(snake_speed)

    pg.quit()
    quit()

gameLoop()
 