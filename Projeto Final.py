# -*- coding: utf-8 -*-
"""
Created on Fri May  3 07:31:59 2019

@author:Aluno 1: Luis Filipe Carrete
"""

#Imports
import pygame
from os import path
import time
import random

img_dir = path.join(path.dirname(__file__), 'img_dir')
snd_dir = path.join(path.dirname(__file__), 'snd_dir')

#Dados gerais do jogo
WIDTH = 400
HEIGHT = 600
FPS = 60
road_speed = 3

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
    assets['tiles'] = pygame.image.load(path.join(img_dir,"Tile.png")).convert()
    assets['oil'] = pygame.image.load(path.join(img_dir,'oil.png')).convert()
    assets['cerca'] = pygame.image.load(path.join(img_dir,'Cerca.png')).convert()
    assets['speed_boost'] = pygame.image.load(path.join(img_dir,'speed_boost.png')).convert()
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
        self.speedy = 3
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        #Deixa dentro da tela
        if self.rect.right > WIDTH - 55:
            self.rect.right = WIDTH - 55
            
        if self.rect.left < 55:
            self.rect.left = 55
            
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        
        if self.rect.top < 0:
            self.rect.top = 0
            
class Tiles(pygame.sprite.Sprite):
    #Construtor de classe
    def __init__ (self, tiles_img, tiles_y):
        #Construtor de classe pai
        pygame.sprite.Sprite.__init__(self)
        
        #Cria sprite
        self.image = tiles_img
        
        #Define tamanho
        self.image = pygame.transform.scale(tiles_img,(25,60))
        
        #Deixa transparente
        self.image.set_colorkey(BLACK)
        
        #Detalhe sobre posicionamento
        self.rect = self.image.get_rect()
        
        self.rect.centerx = WIDTH / 2
        
        self.rect.bottom = tiles_y
        
        
    def update(self):
        self.rect.y += road_speed
        
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0

class Cerca(pygame.sprite.Sprite):
    #Construtor de classe
    def __init__ (self, cerca_img, cerca_y, cerca_x):
        #Construtor de classe pai
        pygame.sprite.Sprite.__init__(self)
        
        #Cria sprite
        self.image = cerca_img
        
        #Define tamanho
        self.image = pygame.transform.scale(cerca_img,(25,60))
        
        #Deixa transparente
        self.image.set_colorkey(BLACK)
        
        #Detalhe sobre posicionamento
        self.rect = self.image.get_rect()
        
        self.rect.centerx = cerca_x
        
        self.rect.bottom = cerca_y
        
    
    def update(self):
        self.rect.y += road_speed
        
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0

class Oil(pygame.sprite.Sprite):
    #Construtor de classe
    def __init__ (self, oil_img):
        #Construtor de classe pai
        pygame.sprite.Sprite.__init__(self)
        
        #Cria sprite
        self.image = oil_img
        
        #Define tamanho
        self.image = pygame.transform.scale(oil_img,(70,70))
        
        #Deixa transparente
        self.image.set_colorkey(BLACK)
        
        #Detalhe sobre posicionamento
        self.rect = self.image.get_rect()
        
        self.rect.centerx = random.randint(70 , WIDTH-70)
        
        self.rect.bottom = 0
        
    def update(self):
        self.rect.bottom += road_speed
        
        if self.rect.top == HEIGHT:
            self.kill()

class Boost(pygame.sprite.Sprite):
    #Construtor de classe
    def __init__ (self, boost_img):
        #Construtor de classe pai
        pygame.sprite.Sprite.__init__(self)
        
        #Cria sprite
        self.image = boost_img
        
        #Define tamanho
        self.image = pygame.transform.scale(boost_img,(50,60))
        
        #Deixa transparente
        self.image.set_colorkey(BLACK)
        
        #Detalhe sobre posicionamento
        self.rect = self.image.get_rect()
        
        self.rect.centerx = random.randint(70 , WIDTH-70)
        
        self.rect.bottom = 0
        
    def update(self):
        self.rect.bottom += road_speed
        
        if self.rect.top == HEIGHT:
            self.kill()

        
        
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

tiles_sprites = pygame.sprite.Group()

cerca_sprites = pygame.sprite.Group()

tile_y = 0

for i in range(7):
    i = Tiles(assets['tiles'], tile_y)
    tile_y -= 110
    tiles_sprites.add(i)

cerca_y = 0

for i in range(12):
    i = Cerca(assets['cerca'], cerca_y, 40)
    ii = Cerca(assets['cerca'], cerca_y, WIDTH - 40)
    cerca_y -= 60
    cerca_sprites.add(i)
    cerca_sprites.add(ii)
    
all_sprites.add(cerca_sprites)
all_sprites.add(tiles_sprites)
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
                    player.speedx = -8
                if event.key == pygame.K_RIGHT:
                    player.speedx = 8
                if event.key == pygame.K_UP:
                    player.speedy = -5
                if event.key == pygame.K_DOWN:
                    player.speedy = 5
            
            
            #Verifica se tecla soltou
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                if event.key == pygame.K_UP:
                    player.speedy = 3
                if event.key == pygame.K_DOWN:
                    player.speedy = 3
        
        #Spawn oil
        oil_spawn = random.randint(0,200)
        
        if oil_spawn == 57:
            i = Oil(assets['oil'])
            all_sprites.add(i)
        
        boost_spawn = random.randint(0,200)
        
        if oil_spawn == 57:
            i = Boost(assets['speed_boost'])
            all_sprites.add(i)

            
            
                
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