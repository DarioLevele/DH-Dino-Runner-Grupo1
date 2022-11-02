import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self, images):
        index = random.randint(0, 1)
        height_position = random.randint(0, 2)
        height = {0 : 200,
                1 : 280,
                2 : 330}

        super().__init__(images, index)
        self.image_rect.y = height[height_position]

    def fly(self):
        self.image = BIRD[0] if self.step <= 5 else BIRD[1]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.DINO_X_POS
        self.image_rect.y = self.DINO_Y_POS
        self.step += 1