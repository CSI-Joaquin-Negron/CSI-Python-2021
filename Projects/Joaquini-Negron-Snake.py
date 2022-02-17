# create the screen
import pygame as pg
pg.init()

yellow = (179, 178, 70)# score
purple = (154, 59, 255)# snake
red = (255, 59, 91)# food
green = (0, 80, 34)# background
light_green = (0, 232, 101)# game over


dis = pg.display.set_mode((600,500)) #define screen resolution
# pg.display.update

pg.display.set_caption('Snake Game By JN')
game_over = False

x1 = 300
y1 = 250

x1_change = 0
y1_change = 0

clock = pg.time.Clock()

while not game_over:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over == True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pg.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pg.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pg.K_DOWN:
                y1_change = 10
                x1_change = 0
    x1 += x1_change
    y1 += y1_change
    dis.fill(green)
    pg.draw.rect(dis, purple, [x1, y1, 10, 10])
    pg.display.update()
    clock.tick(70)
pg.quit()

quit()
