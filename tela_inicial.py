# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:03:39 2019

@author: lfcsa
"""

import pygame
import random
import time
from os import path

from config import img_dir, BLACK, FPS, GAME, QUIT, GARAGEM


def load_assets (img_dir):
    assets = {}
    grass_anim = []
    for i in range(1,6):
        filename = "grass_{}.png".format(i)
        img = pygame.image.load(path.join(img_dir, filename)).convert()
        img = pygame.transform.scale(img, (32,32))
        img.set_colorkey(BLACK)
        grass_anim.append(img)
    assets['grass'] = grass_anim
    return assets


class Grass(pygame.sprite.Sprite):
    #Construtor de classe.
    def __init__ (self, center, grass_anim, frame):
        #Construtor de classe pai.
        pygame.sprite.Sprite.__init__(self)
        
        #Carregar animacao de explosao.
        self.grass_anim = grass_anim
        
        #Inicia processo de animacao.
        self.frame = frame
        self.image = self.grass_anim[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center
      
        
        
        #Guarda tick da primeira imagem
        self.last_update = pygame.time.get_ticks()
        
        #Controlle de ticks da animacao 1 tick = 1 milisegundo
        self.frame_ticks = 120
        
    
    def update(self):
     
        #Verifica tick atual.
        now = pygame.time.get_ticks()
        
        #Verifica quantos ticks passaram des da ultima mudanca de frame
        elapsed_tick = now - self.last_update
        
        #Se ja esta na hora de mudar de imagem.
        if (elapsed_tick > self.frame_ticks):
            
            #Marca o tick da nova imagem.
            self.last_update = now
            
            #Avanca um quadro.
            self.frame += 1
            
            #Verifica se acabou a animacao.
            if self.frame == len(self.grass_anim):
                #Se sim mate explosao.
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.grass_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
                
def tela_inicial(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    
    #Carrega os assets
    assets = load_assets(img_dir)
    grass_sprites = pygame.sprite.Group()
    
    x = 110
    for i in range(1,4):
        frame = random.randint(0,4)
        i = Grass((x,350), assets['grass'], frame)
        grass_sprites.add(i)
        x += 25
    x = 110
    for i in range(1,4):
        frame = random.randint(0,4)
        i = Grass((x,370), assets['grass'], frame)
        grass_sprites.add(i)
        x += 25
    
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(grass_sprites)
    
    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(img_dir, 'inicio.png')).convert()
    background_rect = background.get_rect()

    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
                      
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
                
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    state = QUIT
                    running = False
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    state = GAME
                    running = False
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_g:
                    state = GARAGEM
                    running = False
        
        #Atualiza animacoes 
        all_sprites.update()
        
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        
        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
