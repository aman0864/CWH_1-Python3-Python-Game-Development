# Date 18-04-2021
import pygame as pg
import random

# user's choice
fps = 15

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
snake_size_width = 15
snake_size_height = 15
snake_velocity_x = 0
snake_velocity_y = 0
snake_user_given_velocity = 10

# food making for snake
snake_food_position_x = random.randint(0, screen_width)
snake_food_position_y = random.randint(0, screen_height)
snake_food_color = (246, 2, 40)
snake_food_size_x = 15
snake_food_size_y = 15

while not game_exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_exit = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                snake_velocity_y = 0
                snake_velocity_x = snake_user_given_velocity
            elif event.key == pg.K_LEFT:
                snake_velocity_y = 0
                snake_velocity_x = -snake_user_given_velocity
            elif event.key == pg.K_DOWN:
                snake_velocity_x = 0
                snake_velocity_y = snake_user_given_velocity
            elif event.key == pg.K_UP:
                snake_velocity_x = 0
                snake_velocity_y = -snake_user_given_velocity

    snake_position_x += snake_velocity_x
    snake_position_y += snake_velocity_y
    pg.display.update()

    game_window.fill(screen_background_color)
    # pg.display.flip()
    pg.draw.rect(game_window, snake_color, [
                 snake_position_x, snake_position_y, snake_size_width, snake_size_height])
    pg.draw.rect(game_window, snake_food_color, [
                 snake_food_position_x, snake_food_position_y, snake_food_size_x, snake_food_size_y])
    clock.tick(fps)
    pg.display.update()
