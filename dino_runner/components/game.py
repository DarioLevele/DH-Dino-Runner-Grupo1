import pygame
import random
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.extras import Extra
from dino_runner.components.obstacles.obstacle_handler import ObstacleHandler
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONDO_INICIO, FONDO_GAME_OVER, CLOUD
from dino_runner.utils import text_utils



class Game:
    MAX_LIVE = 3
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.dinosaur = Dinosaur()
        self.obstacle_handler = ObstacleHandler()
        self.vidas = Extra()
        self.playing = False
        self.running = True
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.lives = self.MAX_LIVE    # Mientras tanto :)
        self.points = 0
        self.score_hight = 0
        self.shields = 0
        self.wrd_color = (0, 0, 0)
        self.bg_color = (255, 255, 255)

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def run(self):
        # Game loop: events - update - draw
        self.reset_attributes()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()
    
    def reset_attributes(self):
        self.playing = True
        self.dinosaur = Dinosaur()
        self.vidas = Extra()
        self.points = 0
        self.game_speed = 20
        self.lives = self.MAX_LIVE
        self.shields = 1


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        dino_event = pygame.key.get_pressed()
        self.dinosaur.update(dino_event)
        self.obstacle_handler.update(self)
        self.update_score()
        

        if self.lives == 0:
            self.playing = False
            self.running = True
            self.execute()

    def draw(self):
        self.clock.tick(FPS)
        bg_color = (255, 255, 255) if self.points // 600 != 1 else (0,0,0)
        self.screen.fill(bg_color)
        self.draw_background()
        self.dinosaur.draw(self.screen)
        self.obstacle_handler.draw(self.screen)
        self.vidas.vida_3_coras(self.lives)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    


    def draw_score(self):
        wrd_color = (0,0,0) if self.points // 600 != 1 else (255, 255, 255)
        self.points += 1
        message = "Points: " + str(self.points)
        points_text, points_rect = text_utils.get_text_element(message, SCREEN_WIDTH - 135, 20, font_color=wrd_color)
        self.screen.blit(points_text, points_rect)
        if self.points > self.score_hight:
            self.score_hight = self.points
        message_2 = "Highest score:" + str(self.score_hight)
        points_text, points_rect = text_utils.get_text_element(message_2, SCREEN_WIDTH - 135, 20, font_color=wrd_color)
        self.screen.blit(points_text, (50,25))

    def update_score(self):
        #self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 2
        

    def show_menu(self):
        self.running = True

        self.screen.fill(self.bg_color)
        self.show_menu_options()

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()
    
    def show_menu_options(self):
        red_color = (255, 0, 0)
        if self.points > 0:
            self.screen.blit(FONDO_GAME_OVER, (0, 0))
            text, text_rect = text_utils.get_text_element("Press any key to start again",pos_x=150, pos_y=400 ,font_size=60, font_color=red_color)
            self.screen.blit(text, text_rect)
            text, text_rect = text_utils.get_text_element("Highest score:"+ str(self.score_hight) ,pos_x = 400, pos_y = 470, font_size=30, font_color=(0,255,0))
        else:
            self.screen.blit(FONDO_INICIO, (0, 0))
            text, text_rect = text_utils.get_text_element("Press any key to Start",pos_x = 230, pos_y = 360, font_size=60, font_color=red_color)
        self.screen.blit(text, text_rect)