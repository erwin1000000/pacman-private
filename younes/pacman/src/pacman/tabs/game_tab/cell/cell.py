import pygame
from src.pacman.tabs.game_tab.cell.wall import Wall

class Cell:
    def __init__(self, cell_d, x, y, value, c):
        self.cell_d = cell_d
        self.x = x
        self.y = y
        self.value = value
        self.c = c
        self.cell_surface = pygame.Surface((self.cell_d, self.cell_d), pygame.SRCALPHA)
        self.walls: list[Wall] = self.make_walls()

    def make_walls(self):
        v = self.value
        lst = [1, 2, 4, 8]
        walls = []
        for i in lst:
            if v & i:
                walls.append(Wall(self.cell_d, i, self.c))
        return walls


    def draw(self, maze_surface: pygame.Surface):
        if len(self.walls) == 4:
            self.cell_surface.fill((14, 18, 65))
        for wall in self.walls:
            wall.draw(self.cell_surface)
        maze_surface.blit(self.cell_surface, (self.x, self.y))