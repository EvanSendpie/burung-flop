import pygame, sys, time
from settings import *
from sprite import BG

class Game:
    def __init__(self):
        
        # Setup awal
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Burung Flop')
        self.clock = pygame.time.Clock()
        
        # Grup sprite
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        
        # Scale factor
        bg_height = pygame.image.load('graphics/environment/background.png').get_height()
        self.scale_factor = WINDOW_HEIGHT / bg_height
        
        # Sprite setup
        BG(self.all_sprites, self.scale_factor)
    
    def run(self):
        last_time = time.time()
        while True:
            
            # Delta time
            dt = time.time() - last_time
            last_time = time.time()
            
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Logika game
            self.display_surface.fill('black')
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display_surface)
            
            pygame.display.update()
            self.clock.tick(FRAMERATE)
    
if __name__ == '__main__':
    game = Game()
    game.run()