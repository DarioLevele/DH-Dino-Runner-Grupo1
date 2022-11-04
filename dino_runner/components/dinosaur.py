import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import JUMPING, RUNNING, DUCKING, RUNNING_SHIELD, JUMPING_HAMMER, JUMPING_SHIELD, DUCKING_HAMMER, DUCKING_SHIELD, RUNNING_HAMMER, DEFAULT_TYPE, SHIELD_TYPE, HAMMER_TYPE

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}


class Dinosaur(Sprite):
    DINO_X_POS = 50
    DINO_Y_POS = 315
    INITIAL_STEP = 0
    MAX_STEP = 10
    ACELERATION = 4
    REDUCE_VELOCITY = 0.9
    INITIAL_VELOCITY = 10

    def __init__(self):
        self.image = RUNNING[0]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.DINO_X_POS
        self.image_rect.y = self.DINO_Y_POS
        self.step = self.INITIAL_STEP
        self.dino_jump = False
        self.dino_run = True
        self.dino_duck = False
        self.dino_velocity = self.INITIAL_VELOCITY
        self.dino_type = DEFAULT_TYPE
        self.five = 0

    def update(self, dino_event):
        if self.dino_jump:
            self.jump()
        if self.dino_run:
            self.run()
        if self.dino_duck:
            self.duck()

        if dino_event[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
        
        elif dino_event[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True

        elif not self.dino_jump:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

        if self.step > self.MAX_STEP:
            self.step = self.INITIAL_STEP
    def run(self):#, run_sprite):
        
        self.image = RUN_IMG[self.dino_type][self.step%2]

        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.DINO_X_POS
        self.image_rect.y = self.DINO_Y_POS
        self.five+= 1
        if self.five %5 == 0:
            self.step += 1

    def duck(self):
        self.image = DUCK_IMG[self.dino_type][self.step%2]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.DINO_X_POS - 8
        self.image_rect.y = self.DINO_Y_POS + 32
        self.five+= 1
        if self.five %5 == 0:
            self.step += 1

    def jump(self):
        self.image = JUMP_IMG[self.dino_type]
        if self.dino_jump:
            self.image_rect.y -= self.dino_velocity.__mul__(self.ACELERATION)
            self.dino_velocity -= self.REDUCE_VELOCITY
        if self.dino_velocity < -self.INITIAL_VELOCITY:
            self.image_rect.y = self.DINO_Y_POS
            self.dino_jump = False
            self.dino_velocity = self.INITIAL_VELOCITY
            self.dino_run = True

    def draw(self, screen):
        screen.blit(self.image, (self.image_rect.x, self.image_rect.y))

    def power(self, message_obstacle):
        if message_obstacle.mesage_obs == "shield":
            self.power2([1])

    def power2(self, xd):
        
        if xd[0] == 1:
            self.dino_type = SHIELD_TYPE
            print(xd[0])
            print(self.dino_type)

