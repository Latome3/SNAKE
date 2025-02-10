import pygame
import random
width=1000
heigth=650
pygame.display.set_caption("SNAKE")
screen=pygame.display.set_mode((width, heigth))
class Balle:
    def __init__(self):
        self.rayon=18
        self.color=(255, 67, 30)
        self.position=[width/2, heigth/2]

    def representation(self):
        pygame.draw.circle(screen, self.color, (self.position[0], self.position[1]), self.rayon)
    def changement(self):
        self.position=[random.randint(20, (width-self.rayon)), random.randint(20, (heigth-self.rayon))]
        pygame.draw.circle(screen, self.color, (self.position[0], self.position[1]), self.rayon)