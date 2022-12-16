import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import import_csv_layout, import_folder
from random import choice
from weapons import Weapon
from ui import UI
from enemy import Enemy
class Level:
    def __init__(self):

        # reconhecer a surface
        self.display_surface = pygame.display.get_surface()

        # configurando grupos de sprites com propriedades diferentes 
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # Criando sprite de ataque
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        # Configurando sprites
        self.create_map()
 
        #interface do usuario
        self.ui = UI()
        
        #self.animation_player = AnimationPlayer()
        #self.magic_player = MagicPlayer(self.animation_player)
                    #'objetos': import_csv_layout('assets/Mapa/CSVs/Mapa_Objetos com colisão.csv'),
                    #'plataformas': import_csv_layout('assets/Mapa/CSVs/Mapa_Plataformas.csv'),
    def create_map(self):
        layouts = {
            'borda': import_csv_layout('assets/Mapa/CSVs/Mapa_Floorblock.csv'),
            'enemies' : import_csv_layout('assets/Mapa/CSVs/Mapa_Enemies.csv')
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
                            Tile((x,y), [self.obstacle_sprites],'invisible')
                        
                        if style == 'enemies':
                            if col == '420':
                                self.player  = Enemy('bamboo',(x,y),[self.visible_sprites,self.attackable_sprites],self.obstacle_sprites)
                            elif col == '69':
                                self.player  = Enemy('squid',(x,y),[self.visible_sprites,self.attackable_sprites],self.obstacle_sprites)
                            elif col == '24':
                                self.player  = Enemy('spirit',(x,y),[self.visible_sprites,self.attackable_sprites],self.obstacle_sprites)
                            elif col == '22':
                                self.player  = Enemy('raccoon',(x,y),[self.visible_sprites,self.attackable_sprites ],self.obstacle_sprites)
                           

        self.player  = Player((4145,1900),[self.visible_sprites],self.obstacle_sprites, self.create_attack,self.destroy_attack, self.create_magic )

    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])

    def create_magic(self,style,strength,cost):
        pass  
            

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,True)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        #target_sprite.kill()
                        target_sprite.get_damage(self.player,attack_sprite.sprite_type)

    def run(self): 
        # Atualizar e desenhar o jogo
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.player_attack_logic()  
        self.visible_sprites.enemy_update(self.player)
        self.ui.display(self.player)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # configurações gerais
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2
        self.offset = pygame.math.Vector2()

        # Criando o chão
        self.floor_surf = pygame.image.load("assets/Mapa/Imagens/Mapa.png").convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self, player):

        # Recebendo o desvio do player
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Desenhando o chão
        floor_offset_pos = self.floor_rect.topleft-self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)


        for sprite in sorted(self.sprites(), key = lambda sprite : sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
    
    def enemy_update(self,player):
        enemy_sprites=[sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy' ]
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
    


# class overlay(pygame.sprite.Sprite):
#     def __init__(self, groups):
#         super().__init__(groups)
#         self.overlay_surf = pygame.image.load("assets/Mapa/Imagens/overlay.png").convert_alpha()
#         self.overlay_rect = self.overlay_surf.get_rect(topleft = (0,0))
#         self.mask = pygame.mask.from_surface(self.overlay_surf)