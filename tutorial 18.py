# Date 18-04-2021
import pygame as pg
import random as rd


def game_loop():
    pg.init()
    #! user's choice
    fps = 20
    font = pg.font.Font('freesansbold.ttf', 32)
    color_of_text_to_be_display_on_screen = (233, 54, 100)
    x_position_of_text_to_be_display_on_screen = 0
    y_position_of_text_to_be_display_on_screen = 0
    minimum_range_of_food_from_screen = 150

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

    def displaying_text_on_game_terminal(text, color, x, y):
        text_to_display_on_screen = font.render(text, True, color)
        game_window.blit(text_to_display_on_screen, [x, y])

    def snake_deployeing(game_window, snake_color, snake_incrementation_list, snake_size_width, snake_size_height):
        for snake_position_x, snake_position_y in snake_incrementation_list:
            pg.draw.rect(game_window, snake_color, [
                snake_position_x, snake_position_y, snake_size_width, snake_size_height])

    # if snake_food_position_x > screen_width:
    #     snake_food_position_x -= screen_width
    # elif snake_food_position_y > screen_height:
    #     snake_food_position_y -= screen_height

    # our game colors
    screen_background_color = (13, 40, 84)
    screen_after_game_over_background_color = (255, 255, 255)

    # creating game window
    screen_width = 1920
    screen_height = 1080
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
    snake_user_given_velocity = 20
    snake_incrementation_list = []
    snake_length = 1

    # food making for snake
    snake_food_color = (246, 200, 40)
    snake_food_size_x = 15
    snake_food_size_y = 15
    screen_width_list_for_food = list()
    screen_height_list_for_food = list()
    food_placement(minimum_range_of_food_from_screen, screen_width)
    food_placement(minimum_range_of_food_from_screen, screen_height)
    snake_food_position_x = rd.choice(screen_height_list_for_food)
    snake_food_position_y = rd.choice(screen_width_list_for_food)
    if snake_food_position_x > screen_width:
        snake_food_position_x -= screen_width
    elif snake_food_position_y > screen_height:
        snake_food_position_y -= screen_height

    # making a variable for score
    score = 0

    while not game_exit:
        if game_over == False:
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
                    elif event.key == pg.K_ESCAPE:
                        game_exit = True
                        exit()

            snake_position_x += snake_velocity_x
            snake_position_y += snake_velocity_y
            if abs(snake_position_x-snake_food_position_x) < 15 and abs(snake_position_y-snake_food_position_y) < 15:
                score += 1
                snake_food_position_x = rd.choice(screen_height_list_for_food)
                snake_food_position_y = rd.choice(screen_width_list_for_food)
                if snake_food_position_x > screen_width:
                    snake_food_position_x -= screen_width
                elif snake_food_position_y > screen_height:
                    snake_food_position_y -= screen_height
                pg.display.set_caption(
                    f"Snake Game by Aman!  Your Score is {score}")
                snake_length += 30
            pg.display.update()

            game_window.fill(screen_background_color)
            # pg.display.flip()
            # pg.draw.rect(game_window, snake_color, [
            #              snake_position_x, snake_position_y, snake_size_width, snake_size_height])

            pg.draw.rect(game_window, snake_food_color, [
                snake_food_position_x, snake_food_position_y, snake_food_size_x, snake_food_size_y])
            displaying_text_on_game_terminal(f"Score: {score}", color_of_text_to_be_display_on_screen,
                                             x_position_of_text_to_be_display_on_screen, y_position_of_text_to_be_display_on_screen)
            displaying_text_on_game_terminal(f"Snake's food x position: {snake_food_position_x}", color_of_text_to_be_display_on_screen,
                                             x_position_of_text_to_be_display_on_screen, y_position_of_text_to_be_display_on_screen+50)
            displaying_text_on_game_terminal(f"Snake's food y position: {snake_food_position_y}", color_of_text_to_be_display_on_screen,
                                             x_position_of_text_to_be_display_on_screen, y_position_of_text_to_be_display_on_screen + 100)
            snake_head = list()
            snake_head.append(snake_position_x)
            snake_head.append(snake_position_y)
            snake_incrementation_list.append(snake_head)
            if len(snake_incrementation_list) > snake_length:
                del snake_incrementation_list[0]
            if snake_position_x < 0 or snake_position_x > screen_width or snake_position_y < 0 or snake_position_y > screen_height:
                game_over = True
            snake_deployeing(game_window, snake_color,
                             snake_incrementation_list, snake_size_width, snake_size_height)
            if snake_head in snake_incrementation_list[:-1]:
                game_over = True
        elif game_over == True:
            game_window.fill(screen_after_game_over_background_color)
            displaying_text_on_game_terminal(f"Game Over! Your Score Is: {score}        Press Enter To Play Again", [
                                             0, 0, 0], 450, 500)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_exit = True
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        game_loop()
                    elif event.key == pg.K_ESCAPE:
                        game_exit = True
                        exit()
        clock.tick(fps)
        pg.display.update()


game_loop()
