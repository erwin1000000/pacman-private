import pygame
from src.pacman.text import Text
from pathlib import Path


class Button:
    def __init__(self, w, h, x, y, t, t_c, font_path, b_c1, b_c2, b_c3, trans=None):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.b_c1 = b_c1
        self.b_c2 = b_c2
        self.b_c3 = b_c3
        self.button_surface = pygame.Surface((w, h), pygame.SRCALPHA)
        self.button_text = Text(t, font_path, t_c)
        self.mouse_inside = False
        self.mouse_clicked = False
        self.flag = True
        self.text_h = None
        self.text_w = None
        self.text_x = 0
        self.text_y = 0
        self.transparent = trans

    def mouse_is_inside(self, mx, my, tab_x, tab_y):
        x = self.x + tab_x
        y = self.y + tab_y
        left = x
        right = x + self.w
        top = y
        bottom = y + self.h
        return left <= mx <= right and top <= my <= bottom

    def draw(self, surface: pygame.Surface):
        color = self.b_c1
        if self.mouse_inside:
            color = self.b_c2
            if self.mouse_clicked:
                color = self.b_c3
        if self.transparent:
            color = list(color)
            color.append(self.transparent)
            color = tuple(color)
            self.button_surface.fill(color)
        else:
            self.button_surface.fill(color)
        self.text_h = self.h * 2
        if not self.text_h:
            _, self.text_w, self.text_h, _ = self.button_text.get_text_s_w_h_f(self.w / 2, self.h)
        self.button_text.draw(self.button_surface, self.text_w, self.text_h - (self.text_h / 1.55), 0, 0)
        surface.blit(self.button_surface, (self.x, self.y))

    def window_size_update(self, w, h, x, y):
        self.button_surface = pygame.Surface((w, h))
        self.w = w
        self.h = h
        self.x = x
        self.y = y

