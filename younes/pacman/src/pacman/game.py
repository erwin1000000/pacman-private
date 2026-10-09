import pygame
from src.pacman.tabs.main_menu_tab import MainMenu
from src.pacman.tabs.view_highscores_tab import ViewHighScores
from src.pacman.tabs.instructions_tab import Instructions
from src.pacman.tabs.game_tab.game_tab import GameTab

class Game:
    def __init__(self, data):
        self.data = data
        pygame.init()
        screen_info = pygame.display.Info()
        self.window_width = screen_info.current_w - 100
        self.window_height = screen_info.current_h - 100
        # self.window_width = 1000
        # self.window_height = 600
        self.window_surface = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Pac-Man")
        self.running = True
        self.clock = pygame.time.Clock()
        self.current_tab = 0
        main_menu_tab = MainMenu(
                        self.window_width,
                        self.window_height,
                        (40, 40, 40)
                        )
        self.tabs = [
            main_menu_tab,
            ViewHighScores(
                self.window_width,
                self.window_height,
                "High Scores",
                (0, 0, 0, 200),
                (255, 255, 255),
                main_menu_tab,
                self.data.highscore_filename),
            Instructions(
                self.window_width,
                self.window_height,
                "Instructions",
                (0, 0, 0, 200),
                (255, 255, 255),
                main_menu_tab,
                (
                    "CONTROLS:\n"
                    "   Movement:\n"
                    "       Arrow Keys ( Up, Down, Left, Right ) or ( w, s, a, d ) or ( W, S, A, D )\n"
                    "Menu Navigation:\n"
                    "   mouse\n"
                    "Pause / Back:\n"
                    "   ESC key.\n"
                    "RULES:\n"
                    "   Objective:\n"
                    "       Navigate through the corridors and eat\n"
                    "       all the pacgums in the maze to complete the level.\n"
                    "   Danger:\n"
                    "       Avoid the ghosts at all costs.\n"
                    "       If a ghost catches you, you lose a life.\n"
                    "   Super-Pacgums:\n"
                    "       Eat a super-pacgum to temporarily\n"
                    "       turn the ghosts vulnerable,\n"
                    "       allowing you to eat them for bonus points.\n"
                    "   Scoring:\n"
                    "       Your score increases by eating standard\n"
                    "       pacgums and super-pacgums.\n"
                    "   Time Limit:\n"
                    "       You must finish the maze before\n"
                    "       the level maximum time runs out.\n"
                    )),
            GameTab(
                self.window_width,
                self.window_height,
                self.data
                )
            ]

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # if event.type == pygame.VIDEORESIZE:
            #     self.window_width = event.w
            #     self.window_height = event.h
            #     for tab in self.tabs:
            #         tab.window_size_update(event.w, event.h)
            if event.type == pygame.MOUSEMOTION:
                if self.current_tab == 0:
                    tab = self.tabs[0]
                    for button in tab.buttons:
                        if button.mouse_is_inside(event.pos[0], event.pos[1], tab.x, tab.y):
                            button.mouse_inside = True
                        else:
                            button.mouse_inside = False
                if self.current_tab == 1:
                    tab = self.tabs[1]
                    exit = tab.exit
                    if exit.mouse_is_inside(event.pos[0], event.pos[1], tab.x, tab.y):
                        exit.mouse_inside = True
                    else:
                        exit.mouse_inside = False
                if self.current_tab == 2:
                    tab = self.tabs[2]
                    exit = tab.exit
                    if exit.mouse_is_inside(event.pos[0], event.pos[1], tab.x, tab.y):
                        exit.mouse_inside = True
                    else:
                        exit.mouse_inside = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.current_tab == 0:
                        tab = self.tabs[0]
                        start_game = tab.buttons[0]
                        if start_game.mouse_is_inside(event.pos[0], event.pos[1], tab.x, tab.y):
                            start_game.mouse_clicked = True
                            self.current_tab = 3
                        high_score = tab.buttons[1]
                        if high_score.mouse_is_inside(event.pos[0], event.pos[1], tab.x, tab.y):
                            high_score.mouse_clicked = True
                            self.current_tab = 1
                        intructions = tab.buttons[2]
                        if intructions.mouse_is_inside(event.pos[0], event.pos[1], tab.x, tab.y):
                            intructions.mouse_clicked = True
                            self.current_tab = 2
                        exit = tab.buttons[3]
                        if exit.mouse_is_inside(event.pos[0], event.pos[1], tab.x, tab.y):
                            exit.mouse_clicked = True
                            self.running = False
                    if self.current_tab == 1:
                        tab = self.tabs[1]
                        exit = tab.exit
                        if exit.mouse_is_inside(event.pos[0], event.pos[1], tab.x, tab.y):
                            exit.mouse_clicked = True
                            self.current_tab = 0
                    if self.current_tab == 2:
                        tab = self.tabs[2]
                        exit = tab.exit
                        if exit.mouse_is_inside(event.pos[0], event.pos[1], tab.x, tab.y):
                            exit.mouse_clicked = True
                            self.current_tab = 0
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if self.current_tab == 0:
                        tab = self.tabs[0]
                        for button in tab.buttons:
                            button.mouse_clicked = False
                    if self.current_tab == 1:
                        tab = self.tabs[1]
                        exit = tab.exit
                        exit.mouse_clicked = False
                    if self.current_tab == 2:
                        tab = self.tabs[2]
                        exit = tab.exit
                        exit.mouse_clicked = False

                

    def draw(self):
        self.window_surface.fill((0, 0, 0))
        self.tabs[self.current_tab].draw(self.window_surface)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.events()
            self.draw()
            self.clock.tick(60)
