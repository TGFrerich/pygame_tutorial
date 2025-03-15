import sys
import pygame

class Game:
    def __init__(self):
                
        pygame.init()

        pygame.display.set_caption("My first game")
        self.screen = pygame.display.set_mode((1280,720))

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load("data/images/clouds/cloud_1.png")
        self.img_pos = [50,100]
        self.img.set_colorkey((0,0,0))
        self.movement = [False,False]

    def run(self):
        while True:
            self.screen.fill((14,219,248))
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.screen.blit(self.img,self.img_pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)

Game().run()