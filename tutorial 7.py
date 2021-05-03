# Date 18-04-2021
import pygame as pg
import time

# creating game window
game_window = pg.display.set_mode((1200, 800))
pg.display.set_caption("My first Terminal with name")

# game variables
game_exit = False
game_over = False

# time.sleep(4)

while not game_exit:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                print("You had pressed the right key")
        elif event.type == pg.QUIT:
            game_exit = True
