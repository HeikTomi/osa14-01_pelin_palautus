# TEE PELI TÄHÄN
import pygame
import random

class Npc:
    def __init__(self, x: int, y: int, image: str):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.speed = 1
        
class Player(Npc):
    def __init__(self, x: int, y: int, image: str):
        super().__init__(x, y, image)
        self.speed = 1.5
        self.lives = 3
        self.score = 0
        self.to_right = False
        self.to_left = False
        self.to_up = False
        self.to_down = False
        
    def move_player(self, swidth: int, sheight: int):
        if self.to_right:
            if not self.x >= swidth-self.image.get_width():
                self.x += self.speed
        if self.to_left:
            if not self.x <= 0:
                self.x -= self.speed
        if self.to_up:
            if not self.y <= 0:
                self.y -= self.speed
        if self.to_down:
            if not self.y >= sheight-self.image.get_height():
                self.y += self.speed
        
        self.rect.topleft = [self.x, self.y]         
        
class Game:
    def __init__(self):
        self.level = 1
        self.swidth = 800
        self.sheight = 600
        self.fps = 120
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.swidth, self.sheight))
        self.color_black = (0,0,0)
        
    def input_events(self, player):  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_LEFT:
                    player.to_left = True
                if event.key == pygame.K_RIGHT:
                    player.to_right = True
                if event.key == pygame.K_UP:
                    player.to_up = True
                if event.key == pygame.K_DOWN:
                    player.to_down = True
                                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.to_left = False
                if event.key == pygame.K_RIGHT:
                    player.to_right = False
                if event.key == pygame.K_UP:
                    player.to_up = False
                if event.key == pygame.K_DOWN:
                    player.to_down = False 
                    
    def run(self):
        pygame.init()
        pygame.display.set_caption('Coin collector')
        
        player = Player(self.swidth//2-25, self.sheight-100, "robo.png")
        
        while True:
            self.input_events(player)
            
            self.screen.fill(self.color_black)
            
            # Draw player
            player.move_player(self.swidth, self.sheight)
            self.screen.blit(player.image, player.rect)
            
            # TODO: NPC creation
            
            # TODO: Coin creation
            
            # TODO: Collision detection
            
            # TODO: Info bar
            
            pygame.display.flip()
    
            self.clock.tick(self.fps)

if __name__ == "__main__":     
    game = Game()
    game.run()