import pygame as pg


class Actor:
    def __init__(self, size: tuple = (50, 100), color: tuple = (255, 255, 0), x: float = 0, y: float = 0,):
        self.actor_size = size
        self.actor_color = color
        self.actor_surf = pg.surface.Surface(size=self.actor_size)
        self.actor_body = self.actor_surf.get_rect(x=x, y=y)
        self.rendering_surf = None

    def rendering(self, rendering_surf: pg.surface.Surface=None, color: tuple=None):
        if rendering_surf is not None:
            self.rendering_surf = rendering_surf
        rendering_surf = self.rendering_surf
        if color is None:
            color = self.actor_color
        self.actor_surf.fill(color)
        rendering_surf.blit(self.actor_surf, self.actor_body)

    def get_hit(self, projectile: pg.rect.Rect):
        if self.actor_body.colliderect(projectile):
            self.rendering(color=(200, 0, 0))
