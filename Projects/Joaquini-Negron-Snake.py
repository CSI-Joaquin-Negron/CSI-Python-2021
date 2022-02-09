# create the screen
import pygame as pg
pg.init()

yellow = (179, 178, 70)# score
purple = (154, 59, 255)# snake
red = (255, 59, 91)# food
green = (0, 80, 34)# background
light_green = (0, 232, 101)# game over

dis = pg.display.set_mode((600,500))
pg.display.set_caption('Snake Game By JN')
game_over = False
while not game_over:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over == True
    pg.draw.rect(dis, purple, [300, 250, 10, 10])
    pg.display.update()
pg.quit()

quit()
