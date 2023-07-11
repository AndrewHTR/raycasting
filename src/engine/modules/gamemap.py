import pygame

_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, 1, _, _, _, _, 1],
    [1, _, _, _, 1, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, _, 1, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class GameMap:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.rows = len(self.mini_map)
        self.cols = len(self.mini_map[0])
        self.get_map()

    def get_map(self):
        for x, row in enumerate(self.mini_map):
            for y, value in enumerate(row):
                if value:
                    self.world_map[(y, x)] = value

    def draw(self):
        [pygame.draw.rect(self.game.screen, 'darkgray', (pos[0] * 50, pos[1] * 50, 50, 50), 1)
         for pos in self.world_map]