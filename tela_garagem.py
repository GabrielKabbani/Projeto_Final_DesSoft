# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:03:39 2019

@author: lfcsa
"""

import pygame
import random
from os import path
import json

from config import fnt_dir, img_dir, BLACK, YELLOW, FPS, GAME, QUIT, INIT

def tela_garagem(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(img_dir, 'garagem.png')).convert()
    background_rect = background.get_rect()
    
    score_font = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 12)
    
    with open('historico_de_player.txt','r') as arquivo:
        texto = arquivo.read()
    
    dados = json.loads(texto)
    
    car_selected = dados["car_selected"]
    
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
                if event.key == pygame.K_ESCAPE:
                    state = INIT
                    running = False
                if event.key == pygame.K_1:
                    car_selected = 1
                if event.key == pygame.K_2:
                    car_selected = 2
                if event.key == pygame.K_3:
                    car_selected = 3
                if event.key == pygame.K_4:
                    car_selected = 4
                if event.key == pygame.K_5:
                    car_selected = 5
                if event.key == pygame.K_6:
                    car_selected = 6
                    
            
                    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        
        text_surface = score_font.render("Car Selected:{0}".format(car_selected), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.left = (15)
        text_rect.top = (525)
        screen.blit(text_surface, text_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
        
        dados["car_selected"] = car_selected
        json_dados = json.dumps(dados, sort_keys = True, indent = 4)
        with open('historico_de_player.txt','w') as arquivo:
            arquivo.write(json_dados)
            
    return state
