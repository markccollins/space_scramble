# space scramble
# ludwig game jam 2021
# written and designed by capnsquishy
import os
import pygame
from pygame import Rect
from pygame.math import Vector2
from views import title_screen, resource_screen


class Interface:
    def __init__(self):
        pygame.init()

        self.cell_size = Vector2(64, 64)
        self.world_size = Vector2(16, 10)

        self.views = {          # decides which view we are rendering and updating for
            'title': None,
            'menu': None,
            'resource_overview': None,
            'options': None,
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

        # keep track of events for views to process
        self.event_list = None

    # collect events for processing, and ensure that we quit the program if needed
    def process_input(self):
        self.event_list = pygame.event.get()
        for event in self.event_list:
            if event.type == pygame.QUIT:
                self.running = False
                break

    # send events to view for processing and rendering, and check for change in view
    def update(self):
        # update view
        self.views[self.view].update(self.event_list)

        # check for change in view
        self.view = self.views[self.view].view_change()
        # initialize new view if changed
        if not self.views[self.view]:
            if self.view == 'resource_overview':
                self.views[self.view] = resource_screen.ResourceScreenView(self.window, self.cell_size)

        # exit if needed
        if self.view == 'exit':
            self.running = False

    # main game loop to process inputs, update game state, and render screen
    def run(self):
        while self.running:
            self.process_input()
            self.update()
            self.clock.tick(60)


# initializes the game interface and begins the main game loop
interface = Interface()
interface.run()

# exits the game
pygame.quit()
