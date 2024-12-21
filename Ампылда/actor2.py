import pygame
from time import sleep
import asyncio
from item_script2 import weapon_list, weapon_body_list
from game_settings2 import Settings
from physics_script2 import gravity

actor_body_list = []
actor_list = []

class Actor:
    def __init__(self, size: tuple = (50, 100), color: tuple = (255, 255, 0), health: int = 100,
                 x: float = 0, y: float = None, speed: float = 20, jump_force: float = 100):
        self.health = health
        self.dash_speed = 30
        self.is_dashing = False
        self.actor_size = size
        self.dash_time = 0
        self.dashdirection = 1
        self.actor_color = color
        self.actor_surf = pygame.surface.Surface(size=self.actor_size)
        self.rendering_surf = None
        self.backpack = []
        self.speed = speed
        self.jump_force = jump_force
        self.ground = Settings.screen_height - self.actor_size[1]
        if y is None:
            y = self.ground
        self.actor_body = self.actor_surf.get_rect(x=x, y=y)
        self.is_jump = False
        self.action = 2
        self.flag_turn = True
        self.dead = False
        self.current_weapon = None
        actor_list.append(self)
        actor_body_list.append(self.actor_body)

    def rendering(self, rendering_surf: pygame.surface.Surface=None,
                  color: tuple=None):
        if rendering_surf is not None:
            self.rendering_surf = rendering_surf
        rendering_surf = self.rendering_surf
        if color is None:
            color = self.actor_color
        if self.actor_surf is not None:
            self.actor_surf.fill(color)
            rendering_surf.blit(self.actor_surf, self.actor_body)
        if len(self.backpack) > 0 and self.current_weapon is not None:
            self.backpack[self.current_weapon].weapon_body.x = self.actor_body.centerx
            self.backpack[self.current_weapon].weapon_body.y = self.actor_body.centery
        if self.dead:
            self.actor_surf = None
            self.actor_body = None

    def equip_weapon(self, weapon_index: int = None):
        if weapon_index is not None and weapon_index < len(self.backpack):
            print(weapon_body_list)
            print(weapon_list)
            print(self.backpack)
            if self.current_weapon is not None:
                self.backpack[self.current_weapon].use = 1
            self.current_weapon = weapon_index
            self.backpack[self.current_weapon].use = 2

    def get_hit(self):
            self.health -= 10
            self.rendering(color=(255, 0, 0))
            if self.health <= 0:
                self.rendering(color=(255, 0, 0))
                self.health = 0
                self.dead = True
                print('Death')

    def take_item(self):
        if self.actor_body.collidelist(weapon_body_list) != -1:
            if weapon_list[self.actor_body.collidelist(weapon_body_list)] not in self.backpack:
                print(self.actor_body.collidelist(weapon_body_list))
                print('take it')
                print(weapon_body_list[self.actor_body.collidelist(weapon_body_list)])
                self.backpack.append(weapon_list[self.actor_body.collidelist(weapon_body_list)])
                print(self.backpack)
                weapon_list[self.actor_body.collidelist(weapon_body_list)].use = 1
            else:
                print('this')


    def moving(self, direction, block_list=None):
        if block_list is not None:
            if self.actor_body.collidelist(block_list) != -1:
                current_block = block_list[self.actor_body.collidelist(block_list)]
                if self.actor_body.collidepoint(current_block.bottomleft[0], current_block.bottomleft[1]):
                    self.actor_body.right = current_block.left

                elif self.actor_body.collidepoint(current_block.bottomright[0], current_block.bottomright[1]):
                    self.actor_body.left = current_block.right

                if self.actor_body.bottomright[0] > current_block.topleft[0] and self.actor_body.bottomleft[0] < current_block.topright[0]:
                    self.ground = current_block.top - self.actor_size[1]

            else:
                self.ground = Settings.screen_height - self.actor_size[1]

        if direction == 1:
            self.actor_body.x += self.speed
            self.dashdirection = 1

        if direction == -1:
            self.actor_body.x -= self.speed
            self.dashdirection = -1

        if direction == 2:
            self.actor_body.y += self.speed

        if direction == -2:
            self.actor_body.y -= self.speed

        if Settings.need_gravity:
            if self.actor_body.y < self.ground:
                self.actor_body.y += gravity
            else:
                self.is_jump = False


    def jump(self):
        if not self.is_jump:

            self.is_jump = True
            self.actor_body.y -= self.jump_force
    def dash(self):
        if self.is_dashing == False:
            self.dash_time = 0
            self.is_dashing = True
            self.actor_body.x += self.dash_speed * self.dashdirection
            print("ы")
            self.is_dashing = False


    def use_attack(self, enemy):
        self.action -= 1
        enemy.get_hit()

    def use_heal(self):
        self.action -= 1
        self.health += 5
        if self.health >= 100:
            self.health = 100