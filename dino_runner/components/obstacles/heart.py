import random
from dino_runner.components.obstacles.obstacle import Obstacle

class Heart(Obstacle):
    def __init__(self, images):
        index = 0
        height_position = random.randint(0, 2)
        height = {0 : 200,
                1 : 270,
                2 : 330}

        super().__init__(images, index)
        self.image_rect.y = height[height_position]