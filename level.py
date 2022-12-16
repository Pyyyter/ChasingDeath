import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import import_csv_layout, import_folder
from random import choice
from weapons import Weapon
from ui import UI
class Level:
    def __init__(self):

        # reconhecer a surface
        self.display_surface = pygame.display.get_surface()

        # configurando grupos de sprites com propriedades diferentes 
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        # Criando sprite de ataque
        self.current_attack = None

        # Configurando sprites
        self.create_map()
 
        #interface do usuario
        self.ui = UI()

    def create_map(self):
        layouts = {
            'borda': import_csv_layout('assets/Mapa/CSVs/Mapa_Floorblock.csv'),
            'objetos': import_csv_layout('assets/Mapa/CSVs/Mapa_Objetos com colisão.csv'),
            'plataformas': import_csv_layout('assets/Mapa/CSVs/Mapa_Plataformas.csv'),
        }
        # graphics = {
            #  'grama': import_folder('')
        # }
        # overlay = pygame.image.load("assets/Mapa/Imagens/overlay.png").convert()
        for style,layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'borda':
                            Tile((x,y), [self.obstacles_sprites],'invisible')
        self.player  = Player((4145,1900),[self.visible_sprites],self.obstacles_sprites, self.create_attack,self.destroy_attack, self.create_magic )

    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites])

    def create_magic(self,style,strength,cost):
        pass

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def run(self): 
        # Atualizar e desenhar o jogo
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.ui.display(self.player)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # configurações gerais
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2
        self.offset = pygame.math.Vector2()

        # Criando overlay
        self.overlay_surf = pygame.image.load("assets/Mapa/Imagens/overlay.png").convert_alpha()
        self.overlay_rect = self.overlay_surf.get_rect(topleft = (0,0))

        # Criando o chão
        self.floor_surf = pygame.image.load("assets/Mapa/Imagens/Mapa.png").convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self, player):

        # Desenhar as árvores
        overlay_offset_pos = self.floor_rect.topleft-self.offset
        self.display_surface.blit(self.overlay_surf,overlay_offset_pos)

        # Recebendo o desvio do player
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Desenhando o chão
        floor_offset_pos = self.floor_rect.topleft-self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)


        for sprite in sorted(self.sprites(), key = lambda sprite : sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
        