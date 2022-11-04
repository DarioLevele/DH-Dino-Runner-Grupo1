from dino_runner.components.obstacles.obstacle import Obstacle

class Power_shield(Obstacle):
    def __init__(self, images):
        index = 0
        super().__init__(images, index)
        self.image_rect.y = 337