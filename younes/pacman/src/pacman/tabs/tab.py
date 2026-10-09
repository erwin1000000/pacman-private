import pygame


class Tab:
    def __init__(self, window_w, window_h, c):
        self.tab_surface = pygame.Surface((window_w, window_h))
        self.window_w = window_w
        self.window_h = window_h
        self.c = c

    def draw(self, surface: pygame.Surface, x, y):
        self.tab_surface.fill(self.c)
        surface.blit(self.tab_surface, (x, y))

    # def window_size_update(self, window_w, window_h):
    #     self.window_w = window_w
    #     self.h = window_h
