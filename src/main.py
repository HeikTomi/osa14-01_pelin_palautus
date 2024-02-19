# TEE PELI TÄHÄN
import pygame
import random
import time

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
            self.y = 50
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
        self.score_time = time.time()
        
    def move_player(self, swidth: int, sheight: int):
        if self.to_right:
            if not self.x >= swidth-self.image.get_width():
                self.x += self.speed
        if self.to_left:
            if not self.x <= 0:
                self.x -= self.speed
        if self.to_up:
            if not self.y <= 30:
                self.y -= self.speed
        if self.to_down:
            if not self.y >= sheight-self.image.get_height():
                self.y += self.speed
        
        self.rect.topleft = [self.x, self.y]
        
    def check_coin_collision(self, coin, maxwidth, maxheight):
        if self.check_collision(coin.rect):
            # Socre is based how fast you got to the coin countim 10seconds down to zero
            t1 = time.time()
            dt = t1-self.score_time
            score = 10-int(dt) 
            if score < 0:
                score = 0
                
            self.score += score
            self.counter += score
            self.score_time = time.time() # rest timer

            if self.counter >= 100: # every 100 points you level up
                self.level += 1
                self.counter = 0
                self.speed += 0.5
                
            coin.move_coin(maxwidth, maxheight)
                
            print(self.score)
        
    def check_collision(self, target):
        return pygame.Rect.colliderect(self.rect, target)    
        
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Coin collector')
        
        self.swidth = 800
        self.sheight = 600
        self.fps = 120
        self.bg_color = (0,0,0)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.swidth, self.sheight))
        self.panel_font = pygame.font.SysFont("Arial", 24)
        self.player = Player(self.swidth//2-25, self.sheight-85, "robo.png")
        self.coin = Coin(random.randrange(self.swidth+50), 50, "kolikko.png")
             
    def input_events(self):  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_LEFT:
                    self.player.to_left = True
                if event.key == pygame.K_RIGHT:
                    self.player.to_right = True
                if event.key == pygame.K_UP:
                    self.player.to_up = True
                if event.key == pygame.K_DOWN:
                    self.player.to_down = True
                                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.to_left = False
                if event.key == pygame.K_RIGHT:
                    self.player.to_right = False
                if event.key == pygame.K_UP:
                    self.player.to_up = False
                if event.key == pygame.K_DOWN:
                    self.player.to_down = False
                    
    def draw_panel(self):        
        text = self.panel_font.render(f"Level: {self.player.level}", True, (255, 0, 0))
        self.screen.blit(text, (400, 0))
        
        text = self.panel_font.render(f"Scores: {self.player.score}", True, (255, 0, 0))
        self.screen.blit(text, (200, 0))
        
        text = self.panel_font.render("Esc = end game", True, (255, 0, 0))
        self.screen.blit(text, (600, 0))
        
        pygame.draw.line(self.screen, (255, 0 ,0), (0, 30), (800, 30) )
                    
    def run(self):        
        while True:
            self.input_events()
            
            self.screen.fill(self.bg_color)
            
            # Draw player
            self.player.move_player(self.swidth, self.sheight)
            self.screen.blit(self.player.image, self.player.rect)
            
            # TODO: NPC creation
            
            # Draw coin
            self.screen.blit(self.coin.image, self.coin.rect)
            
            # TODO: Collision detection
            self.player.check_coin_collision(self.coin, self.swidth, self.sheight)
            
            # Draw Info bar
            self.draw_panel()
            
            pygame.display.flip()
    
            self.clock.tick(self.fps)

if __name__ == "__main__":     
    game = Game()
    game.run()