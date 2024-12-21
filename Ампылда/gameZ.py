import pygame
import time
import asyncio
from game_settings2 import Settings
from actor2 import Actor
from item_script2 import Weapon, weapon_body_list, weapon_list

main_screen = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))

actor_1 = Actor(color=(0, 255, 0), x=150, y=400, speed=10)

actor_enemy_1 = Actor(x=300, y=350, speed=10)

weapon_1 = Weapon(x=20, y=480)
weapon_2 = Weapon(color=(255, 0, 255), x=400, y=480)

button_skill_1 = pygame.Rect(100, 400, 50, 50)

block_1 = pygame.Rect(300, 450, 80, 25)

print(weapon_list)
print(weapon_list[0].weapon_body, weapon_list[1].weapon_body)
isDashing = False
direction = 0
print(weapon_body_list)

while True:

    main_screen.fill((0, 0, 255))

    actor_1.rendering(rendering_surf=main_screen)
    weapon_1.rendering(rendering_surf=main_screen)
    weapon_2.rendering(rendering_surf=main_screen)
    actor_enemy_1.rendering(rendering_surf=main_screen)

    pygame.draw.rect(main_screen, color=(255, 255, 255), rect=block_1)





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 1
            elif event.key == pygame.K_LEFT:
                direction = -1
            elif event.key == pygame.K_SPACE:
               actor_1.jump()
            elif event.key == pygame.K_e:
                actor_1.dash()









            elif event.key == pygame.K_1:
                print('1')
                actor_1.equip_weapon(weapon_index=0)
                print(actor_1.current_weapon)
            elif event.key == pygame.K_2:
                print('2')
                actor_1.equip_weapon(weapon_index=1)
                print(actor_1.current_weapon)



        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                direction = 0
            elif event.key == pygame.K_LEFT:
                direction = 0

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if len(actor_1.backpack) > 0:
                actor_1.backpack[0].fire()

    if len(actor_1.backpack) > 0:
        actor_1.backpack[0].projectile.check_hit()

    actor_1.take_item()

    pygame.time.delay(60)

    actor_1.moving(direction, [block_1, ])

    pygame.display.update()
