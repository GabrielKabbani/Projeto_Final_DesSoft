# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:49:39 2019

@author: lfcsa
"""

from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img_dir')
snd_dir = path.join(path.dirname(__file__), 'snd_dir')
fnt_dir = path.join(path.dirname(__file__), 'font')

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

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2
