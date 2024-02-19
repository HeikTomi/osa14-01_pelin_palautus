# TEE PELI TÄHÄN
import pygame
import random

class Npc:
    def __init__(self, x: int, y: int, image: str):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        
class Player(Npc):
    def __init__(self):
        super().__init__(x, y, image)
        
        
class Game:
    def __init__(self):
        self.swidth = 800
        self.sheight = 600
        self.fps = 120
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.swidth, self.sheight))
        
    def game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
    
    def run(self):
        pygame.init()
        
        while True:
            self.game_events()
            # TODO: player events
            
            # TODO: PLAYER creation
            # TODO: NPC creation
            
            # TODO: Coin creation
            
            # TODO: Collision detection
            
            self.screen.fill((0, 0, 0))
            pygame.display.flip()
    
            self.clock.tick(self.fps)
        
game = Game()
game.run()