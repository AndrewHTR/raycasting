from settings import *
import pygame
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.angle = PLAYER_ANGLE
        self.x, self.y = PLAYER_POS

        self.diag_move_corr = 1 / math.sqrt(2)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        self.speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = self.speed * sin_a
        speed_cos = self.speed * cos_a
        keys = pygame.key.get_pressed()


        num_key_pressed = -1
        if keys[pygame.K_w]:
            num_key_pressed += 1
            dx += speed_cos
            dy += speed_sin

        if keys[pygame.K_s]:
            num_key_pressed += 1
            dx += -speed_cos
            dy += -speed_sin

        if keys[pygame.K_a]:
            num_key_pressed += 1
            dx += speed_sin
            dy += -speed_cos

        if keys[pygame.K_d]:
            num_key_pressed += 1
            dx += -speed_sin
            dy += speed_cos

        if num_key_pressed:
            dx *= self.diag_move_corr
            dy *= self.diag_move_corr

        self.x += dx
        self.y += dy

        if keys[pygame.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pygame.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def draw(self):
        pygame.draw.line(self.game.screen, 'blue', (self.x * 50, self.y * 50),
         (self.x * 50 + 100 * math.cos(self.angle),
          self.y * 50 + 100 * math.sin(self.angle)), 1)
        pygame.draw.circle(self.game.screen, 'red', (self.x * 50, self.y * 50), 15)

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)