import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Extra(Sprite):
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def vida_3_coras(self, number_of_lives, corazon, game_over):
        if number_of_lives == 3:
            self.draw(corazon, 970, 50)
            self.draw(corazon, 1005, 50)
            self.draw(corazon, 1040, 50)
        elif number_of_lives == 2:
            self.draw(corazon, 970, 50)
            self.draw(corazon, 1005, 50)
        elif number_of_lives == 1:
            self.draw(corazon, 970, 50)
        else: 
            self.draw(game_over, 380, 200)
            

    def draw(self, imagen, position_x, position_y):
        self.screen.blit(imagen, (position_x, position_y))

