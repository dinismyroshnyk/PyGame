import pygame
from pygame.locals import *
from menu import *

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.SELECT_KEY = False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1280, 720
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = 'assets/fonts/8-BIT WONDER.TTF'
        self.BLACK, self.WHITE, self.GRAY = (0, 0, 0), (255, 255, 255), (128, 128, 128)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.SELECT_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            self.draw_text('Thanks for Playing', 20, (self.DISPLAY_W / 2, self.DISPLAY_H / 2), self.WHITE)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handle_quit_event()
            if event.type == pygame.KEYDOWN:
                self.handle_keydown_event(event)

    def handle_quit_event(self):
        self.running, self.playing = False, False
        self.curr_menu.run_display = False

    def handle_keydown_event(self, event):
        if event.key == pygame.K_RETURN:
            self.SELECT_KEY = True
        if event.key == pygame.K_UP:
            self.UP_KEY = True
        if event.key == pygame.K_DOWN:
            self.DOWN_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.SELECT_KEY = False, False, False

    def draw_text(self, text, size, xy, color):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (xy)
        self.display.blit(text_surface, text_rect)