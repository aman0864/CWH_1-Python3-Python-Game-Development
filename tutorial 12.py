# Date 18-04-2021
import pygame as pg
import time

# user's choice
fps = 30

# our game colors
screen_background_color = (13, 4, 84)

# creating game window
screen_width = 1200
screen_height = 900
game_window = pg.display.set_mode((screen_width, screen_height))

# Setting caption of our game window
pg.display.set_caption("Snake Game by Aman")

# todo pg.display.update()

# game specific variables
game_exit = False
game_over = False
clock = pg.time.Clock()

# snake classification
snake_color = (56, 255, 4)
snake_position_x = 220
snake_position_y = 220
snake_width = 50
snake_height = 50
snake_velocity = 5

while not game_exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_exit = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                snake_position_x += snake_velocity
            elif event.key == pg.K_LEFT:
                snake_position_x += snake_velocity
            elif event.key == pg.K_DOWN:
                snake_position_y += snake_velocity
            elif event.key == pg.K_UP:
                snake_position_y -= snake_velocity

    game_window.fill(screen_background_color)
    # pg.display.flip()
    pg.draw.rect(game_window, snake_color, [
                 snake_position_x, snake_position_y, snake_width, snake_height])
    clock.tick(fps)
    pg.display.update()
