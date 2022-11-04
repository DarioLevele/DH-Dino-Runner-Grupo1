import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.extras import Extra
from dino_runner.components.obstacles.obstacle_handler import ObstacleHandler
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, HEART, GAME_OVER,CLOUD
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
        #self.music = pygame.mixer.Sound("dino_runner/assets/Sound/GIGA.mp3")
    
    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def run(self):
        #self.music.play()
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
        self.obstacle_handler = ObstacleHandler()
        self.vidas = Extra()
        self.points = 0
        self.lives = self.MAX_LIVE

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
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.dinosaur.draw(self.screen)
        self.obstacle_handler.draw(self.screen)
        self.vidas.vida_3_coras(self.lives, HEART, GAME_OVER)
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
        self.points += 1
        message = "Points: " + str(self.points)
        points_text, points_rect = text_utils.get_text_element(message, SCREEN_WIDTH - 135, 20)
        self.screen.blit(points_text, points_rect)

    def update_score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 2

    def show_menu(self):
        self.running = True

        black_color = (0, 0, 0)
        self.screen.fill(black_color)
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
        white_color = (255, 255, 255)
        if self.points > 0:
            text, text_rect = text_utils.get_text_element("GAME OVER!", font_size=40, font_color=white_color)
        else:
            text, text_rect = text_utils.get_text_element("Press any key to Start", font_size=40, font_color=white_color)
        self.screen.blit(text, text_rect)