import pygame
from src.pacman.tabs.game_tab.cell.cell import Cell


class MazeSurface:
    def __init__(self, w, h, x, y, bot_ban_h, cell_d, the_2d_list, c):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.bot_ban_h = bot_ban_h
        self.cell_d = cell_d
        self.maze_surface = pygame.Surface((w, h + self.bot_ban_h))
        self.the_2d_list = the_2d_list
        self.c = c
        self.maze_cells = self.make_cells()
        
    def make_cells(self):
        maze_cells = []
        y = 0
        for lst in self.the_2d_list:
            line_cells = []
            x = 0
            for v in lst:
                line_cells.append(Cell(self.cell_d, x, y, v, self.c))
                x += self.cell_d - (self.cell_d / 10)
            y += self.cell_d - (self.cell_d / 10)
            maze_cells.append(line_cells)
        return maze_cells

    def draw(self, tab_surface: pygame.Surface):
        self.maze_surface.fill((15, 40, 50))
        for line in self.maze_cells:
            for cell in line:
                cell.draw(self.maze_surface)
        tab_surface.blit(self.maze_surface, (self.x, self.y))

