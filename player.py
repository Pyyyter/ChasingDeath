import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, groups, obstacles_sprites):

        # Definindo player
        super().__init__(groups)
        self.image = pygame.image.load("assets/game/mapaMundo1/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)


        # Definindo vetores e velocidade
        self.direction = pygame.math.Vector2()
        self.speed = 5

        # Definindo obstáculos
        self.obstacles_sprites = obstacles_sprites



    def input(self):
        # Reconhecendo entrada de teclado
        keys = pygame.key.get_pressed()

        # Definindo orientação no eixo Y com entradas do teclado
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
            
        # Definindo orientação no eixo Y com entradas do teclado
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else :
            self.direction.x = 0
            

    def move(self,speed):
        # Definindo função de movimento
        # Normalizando o vetor para não ter velocidade vetorial dobrada
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        # movendo, de fato, a classe Player
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center


    
    def collision(self, direction):
        # Função que detecta colisões

        if direction == 'horizontal':
            for sprite in self.obstacles_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    #movendo-se para a direita
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left

                    #movendo-se para a esquerda
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right



        if direction == 'vertical':
            for sprite in self.obstacles_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top

                    #movendo-se para cima
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom



    def update(self):
        self.input()
        self.move(self.speed)