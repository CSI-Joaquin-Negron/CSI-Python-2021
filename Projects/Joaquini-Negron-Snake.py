# create the screen
import pygame as pg
import time
pg.init()

yellow = (179, 178, 70)# score
purple = (154, 59, 255)# snake
red = (255, 59, 91)# food
green = (0, 80, 34)# background
light_green = (0, 232, 101)# game over


dis_width = 600
dis_height = 500
dis = pg.display.set_mode((dis_width,dis_height)) #define screen resolution
# pg.display.update

pg.display.set_caption('Snake Game By JN')
game_over = False

clock = pg.time.Clock()
snake_speed = 15

snake_block = 10

font_style = pg.font.SysFont(None,50)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2
    
    x1_change = 0
    y1_change = 0
while not game_over:
    while game_close == True:
        dis.fill(green)
         

while not game_over:
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
    pg.draw.rect(dis, purple, [x1, y1, snake_block, snake_block])
    pg.display.update()
    clock.tick(30)
message("GAME OVER", red)
pg.display.update
time.sleep(5)
pg.quit()
pg.quit()
quit()
