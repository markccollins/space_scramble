# space scramble
# ludwig game jam 2021
# written and designed by capnsquishy
import os
import pygame
from pygame import Rect
from pygame.math import Vector2
from views import title_screen


class Interface:
    def __init__(self):
        pygame.init()

        self.cell_size = Vector2(64, 64)
        self.world_size = Vector2(16, 10)

        self.views = {          # decides which view we are rendering and updating for
            'title': None,
            'menu': None,
            'resource': None,
            'ship': None
        }
        self.view = 'title'

        # initialize window settings
        window_size = self.world_size.elementwise() * self.cell_size
        self.window = pygame.display.set_mode((int(window_size.x), int(window_size.y)))
        pygame.display.set_caption('space scramble')

        # game loop settings
        self.clock = pygame.time.Clock()
        self.running = True

        # initialize title view
        self.views['title'] = title_screen.TitleScreenView(self.window, self.cell_size)

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break

    def update(self):
        self.views[self.view].update()

    def run(self):
        while self.running:
            self.process_input()
            self.update()
            self.clock.tick(60)


interface = Interface()
interface.run()

pygame.quit()
