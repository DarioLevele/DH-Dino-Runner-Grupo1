from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, SHIELD, SHIELD_TYPE,HEART_RED, COIN
import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.power_up_shield import Power_shield
from dino_runner.components.obstacles.heart import Heart
from dino_runner.components.obstacles.coin import Coin
from dino_runner.components.dinosaur import Dinosaur



class ObstacleHandler():
    def __init__(self):
        self.obstacles = []
        self.cactus_size = [SMALL_CACTUS, LARGE_CACTUS]
        self.muestra = 0
        self.message_dino = Dinosaur()

        

    def update(self, game):
        self.mesage_obs = SHIELD_TYPE
        if len(self.obstacles) == 0:
            self.how_often_shield = game.points % 500
            self.obstacle_type = random.randint(0,random.randint(1,4))

            
            if self.obstacle_type == 2:
                self.obstacles.append(Power_shield(SHIELD))
            elif self.obstacle_type == 0:
                self.obstacles.append(Cactus(self.cactus_size[random.randint(0, 1)]))
            elif self.obstacle_type == 1:
                self.obstacles.append(Bird(BIRD))
            elif self.obstacle_type == 3:
                self.obstacles.append(Coin(COIN))
            elif self.obstacle_type == 4:
                self.obstacles.append(Heart(HEART_RED))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed)  
            if game.lives >3:
                game.lives =3
                
            if game.dinosaur.image_rect.colliderect(obstacle.image_rect) and self.obstacle_type ==2:
                self.obstacles.pop()
                if game.game_speed > 40:
                    game.game_speed = 20
                    self.message_dino.power(self)
                    self.mesage_obs = SHIELD_TYPE
            elif game.dinosaur.image_rect.colliderect(obstacle.image_rect) and self.obstacle_type ==3:
                game.points += 200
                self.obstacles.pop()
                if game.game_speed > 40:
                    game.game_speed = 20
            elif game.dinosaur.image_rect.colliderect(obstacle.image_rect) and self.obstacle_type ==4:
                self.obstacles.pop()
                game.lives += 1
            
            elif game.dinosaur.image_rect.colliderect(obstacle.image_rect):
                game.lives -= 1
                pygame.time.delay(300)
                self.obstacles.pop()
            if obstacle.image_rect.x < -obstacle.image_rect.width:
                self.obstacles.pop()
            

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
