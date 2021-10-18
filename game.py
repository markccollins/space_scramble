# space scramble
# ludwig game jam 2021
# written and designed by capnsquishy
import os
import pygame
from pygame import Rect
from pygame.math import Vector2


# stores data on current game state
class GameState():
    def __init__(self):
        self.world_size = Vector2(16, 10)
        self.views = ['title', 'menu', 'resource', 'ship']      # decides which view we are rendering and updating for
        self.view = 'title'

        # title variables
        self.title_option_position = 0

    def update(self, event):
        if self.view is 'title':
            if event.key == pygame.K_DOWN:
                if self.title_option_position < 2:
                    self.title_option_position += 1
            elif event.key == pygame.K_UP:
                if self.title_option_position > 0:
                    self.title_option_position += -1

        if self.view is 'menu':
            pass

        if self.view is 'resource':
            pass

        if self.view is 'ship':
            pass


class Interface():
    def __init__(self):
        pygame.init()

        self.game_state = GameState()

        self.cell_size = Vector2(64, 64)
        # self.units_texture = pygame.image.load('units.png')

        # initialize window settings
        window_size = self.game_state.world_size.elementwise() * self.cell_size
        self.window = pygame.display.set_mode((int(window_size.x), int(window_size.y)))
        pygame.display.set_caption('space scramble')

        # load default textures
        self.title_bg = pygame.image.load(os.path.join('sprites', 'title_screen.png'))
        self.title_rocket = pygame.image.load(os.path.join('sprites', 'rocket.png'))
        self.star_tick_1 = 0
        self.star_tick_2 = 0
        self.star_tick_3 = 0
        self.title_stars_1 = pygame.image.load(os.path.join('sprites', 'stars_1.png'))
        self.title_stars_2 = pygame.image.load(os.path.join('sprites', 'stars_2.png'))
        self.title_stars_3 = pygame.image.load(os.path.join('sprites', 'stars_3.png'))

        # game loop settings
        self.clock = pygame.time.Clock()
        self.running = True

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                self.game_state.update(event)
                pass

    def update(self):
        if self.game_state.view is 'title':
            self.star_tick_1 += 1
            self.star_tick_2 += 2
            self.star_tick_3 += 3
            if self.star_tick_1 > self.title_stars_1.get_height():
                self.star_tick_1 = 0
            if self.star_tick_2 > self.title_stars_2.get_height():
                self.star_tick_2 = 0
            if self.star_tick_3 > self.title_stars_3.get_height():
                self.star_tick_3 = 0

    def render(self):
        self.update()
        self.window.fill((0, 0, 0))

        if self.game_state.view is 'title':
            # draw title background
            self.window.blit(self.title_bg, (0, 0))

            # draw star background
            self.window.blit(self.title_stars_1, (0, self.star_tick_1))
            self.window.blit(self.title_stars_1, (0, self.title_stars_1.get_height() * -1 + self.star_tick_1))

            self.window.blit(self.title_stars_2, (0, int(self.star_tick_2)))
            self.window.blit(self.title_stars_2, (0, int(self.title_stars_2.get_height() * -1 + self.star_tick_2)))

            self.window.blit(self.title_stars_2, (0, int(self.star_tick_3 )))
            self.window.blit(self.title_stars_2, (0, int(self.title_stars_3.get_height() * -1 + self.star_tick_3)))

            # draw rocket cursor
            sprite_rect = Rect(0, 0, int(self.cell_size.x), int(self.cell_size.y))
            self.window.blit(self.title_rocket, (int(5.5 * self.cell_size.x),
                int((4.15 * self.cell_size.y) + self.game_state.title_option_position * 80)), sprite_rect)

        if self.game_state.view is 'menu':
            pass

        if self.game_state.view is 'resource':
            pass

        if self.game_state.view is 'ship':
            pass

        pygame.display.update()

    def run(self):
        while self.running:
            self.process_input()
            self.update()
            self.render()
            self.clock.tick(60)


interface = Interface()
interface.run()

pygame.quit()
