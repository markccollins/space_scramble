# space scramble
# ludwig game jam 2021
# written and designed by capnsquishy
import pygame
from pygame.math import Vector2


# stores data on current game state
class GameState():
    def __init__(self):
        self.world_size = Vector2(16, 10)
        self.views = ['title', 'menu', 'resource', 'ship']      # decides which view we are rendering and updating for
        self.view = 'title'

    def update(self, event):
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
        pass

    def render(self):
        self.window.fill((0, 0, 0))
        pygame.draw.rect(self.window, (0, 0, 255), (120, 120, 400, 240))
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
