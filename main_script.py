from curses.textpad import rectangle

import pygame as pg
my_list = [100, 100, 200] #список
my_tuple = (100, 100, 200) #кортеж
main_screen = pg.display.set_mode((500, 500))

actor_surf = pg.Surface((50, 100))
actor_rect = actor_surf.get_rect()

button_skill_1 = pg.Rect(100, 400, 50, 50)

delta = 0
while True:
    pg.time.delay(60)
    main_screen.fill((255, 0, 0))
    main_screen.blit(actor_surf, actor_rect)
    actor_surf.fill((255, 150, 0))
    pg.draw.rect(main_screen, color=(100, 100, 0), rect = button_skill_1)

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

    actor_rect.x += delta
    pg.display.update()