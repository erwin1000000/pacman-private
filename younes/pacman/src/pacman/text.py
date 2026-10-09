import pygame
from pathlib import Path


class Text:
    def __init__(self, text, font_path: Path | None = None, color=(255, 255, 255), b_g_c=None):
        self.text = text
        self.font_path = font_path
        self.color = color
        self.text_surface = None
        self.font = None
        self.b_g_c = b_g_c

    def get_text_s_w_h_f(self, w, max_h):
        size = 1
        text_w = 1
        text_h = 1
        if max_h:
            while text_h < max_h:
                font = pygame.Font(self.font_path, size)
                text_w, text_h = font.size(self.text)
                size += 1
        else:
            while text_w < w:
                font = pygame.Font(self.font_path, size)
                text_w, text_h = font.size(self.text)
                size += 1
        self.font = font
        return (size, text_w, text_h, font)

    def _get_text_surface(self, w, max_h):
        if not self.font:
            _, __, ___, self.font = self.get_text_s_w_h_f(w, max_h)
        return self.font.render(self.text, True, self.color, self.b_g_c)
        
    def draw(self, surface: pygame.Surface, w_text, max_h_text, x, y):
        if not self.text_surface:
            self.text_surface = self._get_text_surface(w_text, max_h_text)
        if max_h_text:
            b_w = surface.get_width()
            b_h = surface.get_height()
            t_w = self.text_surface.get_width()
            t_h = self.text_surface.get_height()
            x = (b_w / 2) - (t_w / 2)
            y = (b_h / 2) - (t_h / 3)
        surface.blit(self.text_surface, (x, y))
