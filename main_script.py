from curses.textpad import rectangle
import math
import pygame as pg
from actor_script import Actor

my_list = [100, 100, 200] #список
my_tuple = (100, 100, 200) #кортеж
main_screen = pg.display.set_mode((500, 500))

POMI = Actor(color = (23, 255, 0), x=0, y=400)
KERIIL = Actor(color = (255, 0, 255), x=400, y=400)

button_skill_1 = pg.Rect(100, 400, 50, 50)

stone = pg.Rect(0, 480, 20, 20) #камень Амич

delta = 0
flag_stone_throw = False
t = 0

while True:

    pg.time.delay(60)
    main_screen.fill((255, 0, 0))
    POMI.rendering(rendering_surf=main_screen)
    KERIIL.rendering(rendering_surf=main_screen)

    pg.draw.rect(main_screen, color=(100, 100, 0), rect = button_skill_1)
    pg.draw.rect(main_screen, color=(155, 155, 155), rect = stone)

    for event in pg.event.get():
        if event.type ==  pg.QUIT:
            pg.quit()
            exit()

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                delta = 20
            elif event.key == pg.K_LEFT:
                delta = -20
        elif event.type == pg.KEYUP:
            delta = 0

        elif event.type == pg.MOUSEBUTTONDOWN:
            if button_skill_1.collidepoint(event.pos):
                flag_stone_throw = True

    if flag_stone_throw: # по сути равно тру
        stone.x = 100 * t * math.cos(math.radians(45))
        stone.y = 480 - (50 * t * math.sin(math.radians(45)) - (9.81 * t ** 2) / 2)
        t += 1
    if stone.y > 480:
        stone.x = 0
        stone.y = 480
        flag_stone_throw = False
        t = 0




    KERIIL.get_hit(projectile=stone)
    POMI.actor_body.x += delta
    pg.display.update()
