# Date 18-04-2021
import pygame as pg
import time

# our game colors
screen_background_color = (13, 4, 84)

# creating game window
screen_width = 1200
screen_height = 900
game_window = pg.display.set_mode((screen_width, screen_height))

# Setting caption of our game window
pg.display.set_caption("Snake Game by Aman")
game_window.fill(screen_background_color)
pg.display.flip()
# todo pg.display.update()

# game specific variables
game_exit = False
game_over = False

# time.sleep(4)

while not game_exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_exit = True
