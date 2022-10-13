import pygame
import os

##### Iniciando o PyGame e a Janela #####
pygame.init()
#
windowWidth = 1280
windowHeight = 720
##### Definindo e ajustando o Background #####
screen = pygame.display.set_mode((windowWidth, windowHeight))
background = pygame.transform.scale(pygame.image.load(
    os.path.join("assets", "menu", "background.png")), (9000, windowHeight))
running = True
i = 0

##### Definindo Sidebar #####
sidebar = pygame.transform.scale(pygame.image.load(
    os.path.join("assets", "menu", "Sidebar.png")), (320, windowHeight))
screen.blit(background, [960, 0])

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
##### Animando Janela #####

    screen.blit(background, [-i, 0])
    screen.blit(background, [-windowHeight+i, 0])
    if i == 9000:
        i = 0
    i += 5
    screen.blit(sidebar, [960, 0])
    pygame.display.update()
    
###########################
