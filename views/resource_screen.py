import os
import pygame
from pygame import Rect


class ResourceScreenView:
    # initializes and loads necessary resources for resource screen
    def __init__(self, window, cell_size):
        # initialize window variables
        self.window = window
        self.cell_size = cell_size
        self.view = 'resource_overview'

    def view_change(self):
        return self.view

    # processes events for title screen
    def process_input(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                # select new view: new game, options, exit
                elif event.key == pygame.K_z:
                    pass

    # updates game state for title screen
    def update(self, event_list):
        self.process_input(event_list)

        self.render()

    # renders title screen
    def render(self):
        # clear screen with blank window to prepare for render
        self.window.fill((0, 0, 0))

        pygame.display.update()
