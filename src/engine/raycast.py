import pygame, math
from settings import *

class RayCast:
    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        ox, oy = self.game.player.pos
        x_map , y_map = self.game.player.map_pos

        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        for ray in range(NUM_RAYS):
            
            pygame.draw.line(self.game.screen, 'white', (ox, oy), (ray + 50, ray), 1)

    def update(self):
        self.ray_cast()


