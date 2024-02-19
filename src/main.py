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
        
class Coin(Npc):
    def __init__(self, x: int, y: int, image: str):
        super().__init__(x, y, image)
        
    def move_coin(self, maxwidth, maxheight):
        if self.y <= 250:
                self.x = random.randrange(maxwidth-50)
                self.y = maxheight-self.image.get_height()-25
                self.rect.topleft = [self.x,self.y]
        else: 
            self.x = random.randrange(maxwidth-50)
            self.y = random.randrange(25)
            self.rect.topleft = [self.x, self.y]
       
class Player(Npc):
    def __init__(self, x: int, y: int, image: str):
        super().__init__(x, y, image)
        self.speed = 1.5
        self.lives = 3
        self.level = 1
        self.score = 0
        self.counter = 0
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
        
    def check_coin_collision(self, coin, maxwidth, maxheight):
        if self.check_collision(coin.rect):
            self.score += 100
            self.counter += 100
            if self.counter >= 1000:
                self.level += 1
                self.counter = 0
                
            coin.move_coin(maxwidth, maxheight)
                
            print(self.score)
        
    def check_collision(self, target):
        return pygame.Rect.colliderect(self.rect, target)    
        
class Game:
    def __init__(self):
        self.swidth = 800
        self.sheight = 600
        self.fps = 120
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.swidth, self.sheight))
        self.bg_color = (0,0,0)
        
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
        coin = Coin(random.randrange(self.swidth+50), random.randrange(25), "kolikko.png")
        
        while True:
            self.input_events(player)
            
            self.screen.fill(self.bg_color)
            
            # Draw player
            player.move_player(self.swidth, self.sheight)
            self.screen.blit(player.image, player.rect)
            
            # TODO: NPC creation
            
            # Draw coin
            self.screen.blit(coin.image, coin.rect)
            
            # TODO: Collision detection
            player.check_coin_collision(coin, self.swidth, self.sheight)
            
            # TODO: Info bar
            
            pygame.display.flip()
    
            self.clock.tick(self.fps)

if __name__ == "__main__":     
    game = Game()
    game.run()