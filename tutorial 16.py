# Date 18-04-2021
import pygame as pg
import random as rd


def food_placement(axis_value_parameter_mimimum, axis_value_parameter_maximum):
    """This function will generate numbers from axis_value_parameter_mimimum t axis_value_parameter_maximum;
And it will store those numbers in a list named screen_width_list_for_food or screen_height_list_for_food
    Args:
        axis_value_parameter_mimimum ([integer]): [it is the value of minimum range/parameter of food(of snake) from game terminal end]
        axis_value_parameter_maximum ([integer]): [it is the value of maximum range/parameter of food(of snake) from game terminal end]
    """
    for i in range(axis_value_parameter_mimimum, axis_value_parameter_maximum - axis_value_parameter_mimimum + 1):
        if i % 15 == 0:
            if axis_value_parameter_maximum == screen_width:
                screen_width_list_for_food.append(i)
            elif axis_value_parameter_maximum == screen_height:
                screen_height_list_for_food.append(i)


#! user's choice
fps = 60

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
snake_position_x = 300
snake_position_y = 300
snake_size_width = 15
snake_size_height = 15
snake_velocity_x = 0
snake_velocity_y = 0
snake_user_given_velocity = 10

# food making for snake
snake_food_color = (246, 2, 40)
snake_food_size_x = 15
snake_food_size_y = 15
minimum_range_of_food_from_screen = 30
screen_width_list_for_food = list()
screen_height_list_for_food = list()
food_placement(minimum_range_of_food_from_screen, screen_width)
food_placement(minimum_range_of_food_from_screen, screen_height)
snake_food_position_x = rd.choice(screen_height_list_for_food)
snake_food_position_y = rd.choice(screen_width_list_for_food)

# making a variable for score
score = 0

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
    if abs(snake_position_x-snake_food_position_x) < 15 and abs(snake_position_y-snake_food_position_y) < 15:
        score += 1
        print(f"Score:{score}")
        snake_food_position_x = rd.choice(screen_height_list_for_food)
        snake_food_position_y = rd.choice(screen_width_list_for_food)
        pg.display.set_caption(f"Snake Game by Aman!  Your Score is {score}")
    pg.display.update()

    game_window.fill(screen_background_color)
    # pg.display.flip()
    pg.draw.rect(game_window, snake_color, [
                 snake_position_x, snake_position_y, snake_size_width, snake_size_height])
    pg.draw.rect(game_window, snake_food_color, [
                 snake_food_position_x, snake_food_position_y, snake_food_size_x, snake_food_size_y])
    clock.tick(fps)
    pg.display.update()
