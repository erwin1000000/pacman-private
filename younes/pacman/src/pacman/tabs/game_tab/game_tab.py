import pygame
from mazegenerator import MazeGenerator
from src.parse_validate_data.data_container import Data
from src.pacman.tabs.game_tab.maze import MazeSurface

class GameTab:
    def __init__(self, window_w, window_h, data: Data):
        self.tab_w = window_w
        self.tab_h = window_h
        self.data: Data = data
        self.levels = data.levels
        self.level = 0
        self.the_level_w = self.levels[self.level].width
        self.the_level_h = self.levels[self.level].height
        self.maze_2d_list = self.generate_maze(self.the_level_w, self.the_level_h, data.seed)
        self.bot_ban_h = self.tab_h / 20
        cell_w = self.tab_w / self.the_level_w
        cell_h = (self.tab_h - self.bot_ban_h) / self.the_level_h
        if cell_w > cell_h:
            self.cell_d = cell_h + (cell_h / 10)
        else:
            self.cell_d = cell_w + (cell_w / 10)
        wall_w = (self.cell_d / 10)
        self.wm = ((self.cell_d - wall_w) * self.the_level_w) + wall_w
        self.hm = ((self.cell_d - wall_w) * self.the_level_h) + wall_w
        self.xm = (self.tab_w - self.wm) / 2
        self.ym = (self.tab_h - (self.hm + self.bot_ban_h)) / 2
        self.maze = MazeSurface(
            self.wm,
            self.hm,
            self.xm,
            self.ym,
            self.bot_ban_h,
            self.cell_d,
            self.maze_2d_list,
            (255, 255, 255)
        )

    def generate_maze(self, the_level_w, the_level_h, seed):
        mazegen = MazeGenerator((the_level_w, the_level_h), seed)
        mazegen.generate()
        maze_2d_list = mazegen.maze
        for line in maze_2d_list:
            for i, v in enumerate(line):
                if not (v & 1 and v & 2 and v & 4 and v & 8):
                    line[i] += 16
        maze_2d_list[0][0] += (32 - 16)
        maze_2d_list[0][-1] += (32 - 16)
        maze_2d_list[-1][0] += (32 - 16)
        maze_2d_list[-1][-1] += (32 - 16)
        return maze_2d_list



    def draw(self, surface):
        self.maze.draw(surface)
