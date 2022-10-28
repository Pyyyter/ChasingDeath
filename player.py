import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("assets/game/mapaMundo1/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5

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
            
    # Definindo função de movimento
    def move(self,speed):
        # Normalizando o vetor para não ter velocidade vetorial dobrada
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        # movendo, de fato, a classe Player
        self.rect.center += self.direction * speed

    def update(self):
        self.input()
        self.move(self.speed)