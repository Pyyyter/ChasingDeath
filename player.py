import pygame
from settings import *
from support import import_folder
from entity import Entity
class Player(Entity):

    def __init__(self, pos, groups, obstacle_sprites, create_attack,destroy_attack,create_magic):

        # Definindo player
        super().__init__(groups)
        self.image = pygame.image.load("assets/player/down/down_1.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-30, -26)

        # Setup dos gráficos
        self.import_player_assets()
        self.status = 'down'


        # Definindo vetores e velocidade

        self.speed = 5
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = 0 

        # Definindo obstáculos
        self.obstacle_sprites = obstacle_sprites

        # Weapon
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.switch_duration_cooldown = 200

        # Magic
        self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(magic_data.keys())[self.magic_index]
        self.can_switch_magic = True
        self.magic_switch_time = None

        # Stats
        self.stats = {'health':100,'energy':60,'attack':10,'magic':4, 'speed':6}
        self.health = self.stats['health'] * 0.5
        self.energy = self.stats['energy'] * 0.8
        self.exp = 666
        self.speed = self.stats['speed']
        
    def import_player_assets(self):
        character_path = 'assets/player/'
        self.animations = {'up': [],'down': [],'left': [],'right': [],
                           'up_idle': [],'down_idle': [],'left_idle': [],'right_idle': [],
                           'up_attack': [],'down_attack': [],'left_attack': [],'right_attack': [],}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        # Reconhecendo entrada de teclado
        keys = pygame.key.get_pressed()

        # Definindo orientação no eixo Y com entradas do teclado
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0
            
        # Definindo orientação no eixo Y com entradas do teclado
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else :
            self.direction.x = 0

        # Attack input
        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            self.create_attack()

        # Magic input
        if keys[pygame.K_LCTRL]and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()   
            style = list(magic_data.keys())[self.magic_index]
            strength= list(magic_data.values())[self.magic_index]['strength'] + self.stats['magic']
            cost= list(magic_data.values())[self.magic_index]['cost']
            self.create_magic(style,strength,cost)

        if keys[pygame.K_q] and self.can_switch_weapon:
            self.can_switch_weapon = False
            self.weapon_switch_time = pygame.time.get_ticks()
            if self.weapon_index< len(list(weapon_data.keys())) - 1:
                self.weapon_index +=1
            else:
                self.weapon_index = 0
            self.weapon =  list(weapon_data.keys())[self.weapon_index]

        if keys[pygame.K_e] and self.can_switch_weapon:
            self.can_switch_weapon = False
            self.weapon_switch_time = pygame.time.get_ticks()
            self.weapon_index -=1
            self.weapon =  list(weapon_data.keys())[self.weapon_index]

    def get_status (self):
        
        # Definindo sempre como idle
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'

        # Travando o char enquanto ele ataca
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack') 
                else:
                    self.status = self.status + '_attack'
        else :
            if 'attack' in self.status :
                self.status = self.status.replace('_attack','')

    def cooldowns(self):
        current_time  = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_attack()
        if not self.can_switch_weapon:
            
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown: # type: ignore
                self.can_switch_weapon = True

    def animate(self):
        animation = self.animations[self.status]

        # Fazendo looping dos frames
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # Acessando e usando as imagens
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def animate (self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def get_full_weapon_damage(self):
        base_damage = self.stats['attack']
        weapon_damage = weapon_data[self.weapon]['damage']
        return base_damage + weapon_damage

    def check_death(self):
        if self.health<= 0:
            self.kill()

    def update(self):
        self.input()
        self.animate()
        self.check_death()
        self.cooldowns()
        self.get_status()
        self.move(self.speed)