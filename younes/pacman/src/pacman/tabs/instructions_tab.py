import pygame
from src.pacman.tabs.tab import Tab
from src.pacman.text import Text
from src.pacman.variables.button import Button
from pathlib import Path


class Instructions(Tab):
    def __init__(self, window_w, window_h, t, b_c, t_c, main_menu_tab, content):
        self.tab_w = window_h - (window_h / 5)
        self.tab_h = window_h - (window_h / 6)
        self.x = (window_w - self.tab_w) / 2
        self.y = (window_h - self.tab_h) / 3
        self.tab_surface = pygame.Surface((self.tab_w, self.tab_h), pygame.SRCALPHA)
        self.content = Text(content, Path("./src/fonts/Pixel-Game.otf"))
        self.top_banner_h = self.tab_h / 35
        self.top_tab_surface = Button(
            self.tab_w,
            self.top_banner_h,
            0,
            0,
            t,
            (0, 0, 0),
            Path("./src/fonts/Pixel-Game.otf"),
            (255, 255, 255),
            (255, 255, 255),
            (255, 255, 255),
            )
        self.t_c = t_c
        self.b_c = b_c
        
        self.main_menu_tab = main_menu_tab
        self.exit = Button(
            self.top_banner_h,
            self.top_banner_h,
            self.tab_w - (self.tab_h / 35) + 1,
            0,
            "X",
            (0, 0, 0),
            None,
            (255, 107, 107),
            (255, 54, 54),
            (255, 0, 0)
        )

    def draw(self, surface: pygame.Surface):
        self.main_menu_tab.draw(surface)
        self.tab_surface.fill(self.b_c)
        self.top_tab_surface.draw(self.tab_surface)
        self.exit.draw(self.tab_surface)
        content_w = self.tab_w * 8
        self.content.draw(self.tab_surface, content_w, None, self.tab_w / 20, self.top_banner_h * 2)
        surface.blit(self.tab_surface, (self.x, self.y))

