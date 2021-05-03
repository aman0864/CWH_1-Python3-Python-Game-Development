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

# snake classification
snake_color = (56, 255, 4)
snake_position_x = 220
snake_position_y = 220
snake_width = 50
snake_height = 50

while not game_exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_exit = True

    pg.draw.rect(game_window, snake_color, [
                 snake_position_x, snake_position_y, snake_width, snake_height])
    pg.display.update()
