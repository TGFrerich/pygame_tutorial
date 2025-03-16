import sys
import pygame
from scripts.entities import PhysicsEntity
from scripts.utils import load_image
class Game:
    def __init__(self):
                
        pygame.init()

        pygame.display.set_caption("My first game")
        self.screen = pygame.display.set_mode((1280,720))
        self.display = pygame.Surface((640,360))


        self.clock = pygame.time.Clock()
        self.movement = [False,False]
        

        self.collision_area = pygame.Rect(50,50,300,50)
        self.player = PhysicsEntity(self, 'Player',(50,50), (8,15))
        self.assets = {
            'player':load_image('entities/player.png')
        }


    def run(self):
        while True:
            self.display.fill((14,219,248))
            self.player.update((self.movement[1] - self.movement[0],0))
            self.player.render(self.display)

           

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()