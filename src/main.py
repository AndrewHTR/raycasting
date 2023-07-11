import pygame
from settings import *
from engine.modules.gamemap import GameMap
from engine.player import Player
from engine.raycast import RayCast

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.time = 0
        self.delta_time = 0.01

        self.map = GameMap(self)
        self.player = Player(self)
        self.raycast = RayCast(self)

    def update(self):
        self.player.update()
        self.raycast.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick()
        pygame.display.set_caption(f"FPS: {self.clock.get_fps():.1f}")

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.map.draw()
        self.player.draw()
        
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
    def get_time(self):
        self.time = pygame.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.check_events()
            self.get_time()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()


