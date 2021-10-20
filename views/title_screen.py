import os
import pygame
from pygame import Rect


class TitleScreenView:
    # initializes and loads necessary resources for title screen
    def __init__(self, window, cell_size):
        # initialize window variables
        self.window = window
        self.cell_size = cell_size

        # load background textures
        self.title_bg = pygame.image.load(os.path.join('sprites', 'title_screen.png'))
        self.title_stars_1 = pygame.image.load(os.path.join('sprites', 'stars_1.png'))
        self.title_stars_2 = pygame.image.load(os.path.join('sprites', 'stars_2.png'))
        self.title_stars_3 = pygame.image.load(os.path.join('sprites', 'stars_3.png'))

        # load rocket cursor
        self.title_rocket = pygame.image.load(os.path.join('sprites', 'rocket.png'))

        # initialize star background timers
        self.star_tick_1 = 0
        self.star_tick_2 = 0
        self.star_tick_3 = 0

        # title variables
        self.title_option_position = 0

    # processes events for title screen
    def process_input(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if self.title_option_position < 2:
                        self.title_option_position += 1
                elif event.key == pygame.K_UP:
                    if self.title_option_position > 0:
                        self.title_option_position += -1

    # updates game state for title screen
    def update(self, event_list):
        self.process_input(event_list)

        self.star_tick_1 += 1
        self.star_tick_2 += 2
        self.star_tick_3 += 3
        if self.star_tick_1 > self.title_stars_1.get_height():
            self.star_tick_1 = 0
        if self.star_tick_2 > self.title_stars_2.get_height():
            self.star_tick_2 = 0
        if self.star_tick_3 > self.title_stars_3.get_height():
            self.star_tick_3 = 0

        self.render()

    # renders title screen
    def render(self):
        # clear screen with blank window to prepare for render
        self.window.fill((0, 0, 0))

        # draw title background
        self.window.blit(self.title_bg, (0, 0))

        # draw star background
        self.window.blit(self.title_stars_1, (0, self.star_tick_1))
        self.window.blit(self.title_stars_1, (0, self.title_stars_1.get_height() * -1 + self.star_tick_1))

        self.window.blit(self.title_stars_2, (0, int(self.star_tick_2)))
        self.window.blit(self.title_stars_2, (0, int(self.title_stars_2.get_height() * -1 + self.star_tick_2)))

        self.window.blit(self.title_stars_3, (0, int(self.star_tick_3)))
        self.window.blit(self.title_stars_3, (0, int(self.title_stars_3.get_height() * -1 + self.star_tick_3)))

        # draw rocket cursor
        sprite_rect = Rect(0, 0, int(self.cell_size.x), int(self.cell_size.y))
        self.window.blit(self.title_rocket, (int(5.5 * self.cell_size.x),
                         int((4.15 * self.cell_size.y) + self.title_option_position * 80)), sprite_rect)

        pygame.display.update()
