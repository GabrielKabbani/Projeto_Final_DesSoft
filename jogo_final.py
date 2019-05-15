# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:06:54 2019

@author: lfcsa
"""

# Importando as bibliotecas necessárias.
import pygame
import random
import time


from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from tela_inicial import tela_inicial
from tela_do_jogo import tela_do_jogo

# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Ride Along")

# Comando para evitar travamentos.
try:
    state = INIT
    while state != QUIT:
        if state == INIT:
            state = tela_inicial(screen)
        elif state == GAME:
            state = tela_do_jogo(screen)
        else:
            state = QUIT
finally:
    pygame.quit()
