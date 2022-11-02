from dino_runner.utils.constants import SMALL_CACTUS, BIRD
import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

class ObstacleHandler():
    def __init__(self):
        self.obstacles = []

    def update(self, speed, dino):
        if len(self.obstacles) == 0:
            obstacle_type = random.randint(0,1)
            if obstacle_type == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif obstacle_type == 1:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(speed)
            if dino.image_rect.colliderect(obstacle.image_rect):
                pygame.time.delay(300)
                self.obstacles.pop()
            if obstacle.image_rect.x < -obstacle.image_rect.width:
                self.obstacles.pop()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)