# -*- coding: utf-8 -*-
"""
Created on Fri May  3 07:31:59 2019

@author: lfcsa
"""

#Imports
import pygame
from os import path
import time


img_dir = path.join(path.dirname(__file__), 'img_dir')
snd_dir = path.join(path.dirname(__file__), 'snd_dir')

#Dados gerais do jogo
WIDTH = 400
HEIGHT = 600
FPS = 60

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#Inicia pygame

pygame.init()
pygame.mixer.init()

#Cria assets

def load_assets (img_dir, snd_dir):
    assets = {}
    assets['player_img'] = pygame.image.load(path.join(img_dir,"player_1.png")).convert()
    assets['background'] = pygame.image.load(path.join(img_dir,"Background.png")).convert()
    return assets


#Classes
    
#Classe player
class Player(pygame.sprite.Sprite):
    #Construtor de classe
    def __init__ (self, player_img):
        #Construtor de classe pai
        pygame.sprite.Sprite.__init__(self)
        
        #Cria sprite
        self.image = player_img
        
        #Define tamanho
        self.image = pygame.transform.scale(player_img,(40,55))
        
        #Deixa transparente
        self.image.set_colorkey(BLACK)
        
        #Detalhe sobre posicionamento
        self.rect = self.image.get_rect()
        
        #Centraliza no baixo da tela 
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 40
        
        #Velocidade 
        self.speedx = 0
        self.speedy = 0
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        #Deixa dentro da tela
        if self.rect.right > WIDTH - 55 or self.rect.left < 55:
            self.speedx = 0
        
        
#Tamanho da tela
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#Display nome do jogo
pygame.display.set_caption("Ride Along")
        
#Variavel de relogio:
clock = pygame.time.Clock()

#Carrega os assets 
assets = load_assets(img_dir, snd_dir)

#Carrega fundo
background = assets["background"]
background_rect = background.get_rect()

#Cria a variavel que contem classe do player
player = Player(assets['player_img'])

#Adiciona sprite 
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
    

#Para nao travarmos:
try:
    
    running = True
    while running:
        #Ajusta velocidade de jogo
        clock.tick(FPS)
        
        # Processa os eventos
        for event in pygame.event.get():
            
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
                
            #Verifica se clica tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speedx = -10
                if event.key == pygame.K_RIGHT:
                    player.speedx = 10
            
            #Verifica se tecla soltou
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                
        #Atualiza sprites depois de cada evento
        all_sprites.update()
        
        
        #Cada loop redesenha os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        #Depois de desenhar inverte o display
        pygame.display.flip()
        
finally:
    pygame.quit()