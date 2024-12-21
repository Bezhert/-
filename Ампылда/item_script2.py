import pygame
import math
import actor2

weapon_body_list = []
weapon_list = []

class Projectile:
    def __init__(self, size: tuple = (10, 10), color: tuple = (255, 0, 0),
                 x: float = 0, y: float = 0):
        self.size = size
        self.color = color
        self.surf = pygame.surface.Surface(size=self.size)
        self.body = self.surf.get_rect(x=x, y=y)
        self.fire = False

    def check_hit(self):
        if self.fire:
            target_list = actor2.actor_body_list
            if len(actor2.actor_body_list) > 0:
                if self.body.collidelist(target_list) != -1:
                    current_target = actor2.actor_list[self.body.collidelist(target_list)]
                    current_target.get_hit()
                    if current_target.dead:
                        actor2.actor_list.pop(self.body.collidelist(target_list))
                        actor2.actor_body_list.pop(self.body.collidelist(target_list))

class Weapon:
    def __init__(self, size: tuple = (40, 20), color: tuple = (200, 180, 120),
                 x: float = 0, y: float = 0):
        self.weapon_size = size
        self.weapon_color = color
        self.weapon_surf = pygame.surface.Surface(size=self.weapon_size)
        self.weapon_body = self.weapon_surf.get_rect(x=x, y=y)
        self.rendering_surf = None
        self.projectile = Projectile()
        self.projectile_tau = 0
        self.fire_flag = False
        self.use = 0
        weapon_list.append(self)
        weapon_body_list.append(self.weapon_body)

    def rendering(self, rendering_surf: pygame.surface.Surface=None,
                  color: tuple=None):
        if rendering_surf is not None:
            self.rendering_surf = rendering_surf
        rendering_surf = self.rendering_surf
        if color is None:
            color = self.weapon_color
        self.weapon_surf.fill(color)
        if self.use == 0 or self.use == 2:
            self.weapon_surf.set_alpha(255)
        elif self.use == 1:
            self.weapon_surf.set_alpha(0)
        rendering_surf.blit(self.weapon_surf, self.weapon_body)

        if not self.fire_flag:
            self.projectile.body.x = self.weapon_body.midright[0]
            self.projectile.body.y = self.weapon_body.midright[1]
        else:
            pygame.draw.rect(rendering_surf, color=(255, 100, 50), rect=self.projectile.body)
            self.projectile.body.x += 50 * math.cos(math.radians(45))
            self.projectile.body.y -= (10 * math.sin(math.radians(45)) - (9.81 * self.projectile_tau ** 2) / 2)

            if self.projectile.body.y > 500 or self.projectile.body.x > 500:
                self.fire_flag = False
                self.projectile.fire = False

    def fire(self):
        self.fire_flag = True
        self.projectile.fire = True
