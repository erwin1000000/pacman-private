from src.pacman.tabs.instructions_tab import Instructions
from pathlib import Path
import json
from sys import exit
from src.pacman.text import Text
import pygame

class ContentError(Exception):
    pass

class ViewHighScores(Instructions):
    def __init__(self, window_w, window_h, t, b_c, t_c, main_menu_tab, content):
        super().__init__(window_w, window_h, t, b_c, t_c, main_menu_tab, content)
        self.text = ""
        self.path = Path(f"./src/cache/{content}")
        self._load_high_scores()
        self.content = Text(self.text, Path("./src/fonts/Pixel-Game.otf"))

    def _valid_name(self, name: str):
        if not name:
            return False
        characters = "abcdefghijklmnopqrstuvwxyz0123456789 "
        name = name.lower()
        for c in name:
            if c not in characters:
                return False
        return True

    def _is_list_sorted(self, lst):
        if not lst:
            return True
        x = lst[0]
        for y in lst:
            if y > x:
                return False
            else:
                x = y
        return True

    def _load_high_scores(self):
        try:
            with self.path.open("r", encoding="utf-8") as f:
                dic = json.load(f)
                lst = []
                i = 0
                for i, (k, v) in enumerate(dic.items()):
                    if i == 10:
                        break
                    if self._valid_name(k) and isinstance(v, int) and v >= 0:
                        self.text += f"{i + 1} - {k} : {v}\n"
                        lst.append(v)
                    else:
                        raise ContentError("Error: high scores content is currupted")
                if not self._is_list_sorted(lst):
                    raise ContentError("Error: high scores content is not sorted")
                for i in range(i, 10):
                    self.text += "                             \n"
        except FileNotFoundError:
            print("Error: high scores file does not exist")
            exit(1)
        except json.decoder.JSONDecodeError:
            print("Error: high scores file is currupted")
            exit(1)
        except ContentError as e:
            print(e)
            exit(1)

    def draw(self, surface: pygame.Surface):
        self.main_menu_tab.draw(surface)
        self.tab_surface.fill(self.b_c)
        self.top_tab_surface.draw(self.tab_surface)
        self.exit.draw(self.tab_surface)
        content_w = self.tab_w * 5.5
        self.content.draw(self.tab_surface, content_w, None, self.tab_w / 20, self.top_banner_h * 2)
        surface.blit(self.tab_surface, (self.x, self.y))