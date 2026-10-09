import pygame
from src.pacman.tabs.tab import Tab
from src.pacman.text import Text
from pathlib import Path
from src.pacman.variables.button import Button

class MainMenu(Tab):
    def __init__(self, window_w, window_h, c):
        self.c = c
        self.tab_w = window_h
        self.tab_h = window_h
        self.tab_surface = pygame.Surface((self.tab_w, self.tab_h))
        self.pacman_text = Text("Pac9Man", Path("./src/fonts/PAC-FONT.TTF"), (255, 209, 0))
        self.x = (window_w - window_h) / 2
        self.y = 0
        self.first_button_y = 2 * (self.tab_h / 5)
        self.cst = (self.tab_h / 20) + 20
        self.buttons = [
            Button(
                self.tab_w / 2,
                self.tab_h / 20,
                self.tab_w / 4,
                self.first_button_y,
                "Start Game",
                (255, 255, 255),
                Path("./src/fonts/Pixel-Game.otf"),
                (255, 145, 0),
                (255, 200, 43),
                (247, 86, 40)
                ),
            Button(
                self.tab_w / 2,
                self.tab_h / 20,
                self.tab_w / 4,
                self.first_button_y + self.cst * 1,
                "View Highscores",
                (255, 255, 255),
                Path("./src/fonts/Pixel-Game.otf"),
                (255, 145, 0),
                (255, 200, 43),
                (247, 86, 40)
                ),
            Button(
                self.tab_w / 2,
                self.tab_h / 20,
                self.tab_w / 4,
                self.first_button_y + self.cst * 2,
                "Instructions",
                (255, 255, 255),
                Path("./src/fonts/Pixel-Game.otf"),
                (255, 145, 0),
                (255, 200, 43),
                (247, 86, 40)
                ),
            Button(
                self.tab_w / 2,
                self.tab_h / 20,
                self.tab_w / 4,
                self.first_button_y + self.cst * 3,
                "Exit",
                (255, 255, 255),
                Path("./src/fonts/Pixel-Game.otf"),
                (255, 145, 0),
                (255, 200, 43),
                (247, 86, 40)
                )
        ]

    def draw(self, surface: pygame.Surface):
        self.tab_surface.fill(self.c)
        w_pacman_text = (self.tab_w) - (self.tab_w / 20)
        self.pacman_text.draw(self.tab_surface, w_pacman_text, None, (self.tab_w / 40), (self.tab_h / 40))
        for button in self.buttons:
            button.draw(self.tab_surface)
        surface.blit(self.tab_surface, (self.x, self.y))

    # def window_size_update(self, window_w, window_h):
    #     super().window_size_update(window_w, window_h)
    #     self.tab_w = self.window_w / 2
    #     self.tab_h = window_h
    #     self.tab_surface = pygame.Surface((self.tab_w, self.tab_h))
    #     self.x = self.window_w / 4
    #     self.y = 0
    #     self.f_b_y = 2 * (self.tab_h / 5)
    #     self.cst = (self.tab_h / 20) + 10
    #     for i, button in enumerate(self.buttons):
    #         button.window_size_update(
    #             self.tab_w / 2,
    #             self.tab_h / 20,
    #             self.tab_w / 4,
    #             self.f_b_y + self.cst * i
    #         )
