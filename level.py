import pygame
from settings import *

class Level:
    def __init__(self):

        ##### reconhecer a surface
        self.display_surface = pygame.display.get_surface()

        ##### configurando grupos de sprites com propriedades diferentes #####
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        ##### configurando sprites
        self.create_map()

    def create_map(self):
        for row in WORLD_MAP:
            print(row)

    def run(self): 
        ##### Atualizar e desenhar o jogo #####
        pass