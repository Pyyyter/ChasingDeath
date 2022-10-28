import pygame
from settings import *
from tile import Tile
from player import Player
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
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == "x":
                    Tile((x,y),[self.visible_sprites])

                if col == "p":
                    Player((x,y),[self.visible_sprites])
    def run(self): 
        ##### Atualizar e desenhar o jogo #####
        self.visible_sprites.draw(self.display_surface)