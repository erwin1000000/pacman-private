import pygame

class Wall:
    def __init__(self, cell_d, wall, c):
        self.w = cell_d
        self.h = cell_d
        self.x = 0
        self.y = 0
        self.c = c
        if wall == 1 or wall == 4:
            self.h = cell_d / 10
            if wall == 4:
                self.y = cell_d - self.h
        elif wall == 2 or wall == 8:
            self.w = cell_d / 10
            if wall == 2:
                self.x = cell_d - self.w
        self.wall_surface = pygame.Surface((self.w, self.h))

    def draw(self, cell_surface: pygame.Surface):
        self.wall_surface.fill(self.c)
        cell_surface.blit(self.wall_surface, (self.x, self.y))
