import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS

class Cactus(Obstacle):

    def __init__(self, images):
        index = random.randint(0, 2)
        super().__init__(images, index)
        if images == SMALL_CACTUS:
            self.image_rect.y = 337
        else:
            self.image_rect.y = 310