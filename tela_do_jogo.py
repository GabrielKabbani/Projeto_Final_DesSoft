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
import json

from config import img_dir, snd_dir, fnt_dir, WIDTH, HEIGHT, BLACK, YELLOW, FPS, INIT


#Cria assets

def load_assets (img_dir, snd_dir):
    assets = {}
    player_img = []
    for i in range (1,7):
        filename = "player_{}.png".format(i)
        img = pygame.image.load(path.join(img_dir, filename)).convert()
        player_img.append(img)
    assets['player_img'] = player_img
    assets['background'] = pygame.image.load(path.join(img_dir,"Background.png")).convert()
    assets['tiles'] = pygame.image.load(path.join(img_dir,"Tile.png")).convert()
    assets['lama'] = pygame.image.load(path.join(img_dir,'lama.png')).convert()
    assets['cerca'] = pygame.image.load(path.join(img_dir,'Cerca.png')).convert()
    assets['speed_boost'] = pygame.image.load(path.join(img_dir,'speed_boost.png')).convert()
    assets['score_board'] = pygame.image.load(path.join(img_dir,'score_board.png')).convert()
    assets['crash'] = pygame.mixer.Sound(path.join(snd_dir, 'carcrash.wav'))
    assets['carsound'] = pygame.mixer.Sound(path.join(snd_dir, 'carsound.wav'))
    assets['coinsound'] = pygame.mixer.Sound(path.join(snd_dir,'coinsound.wav'))
    assets['boostsound'] = pygame.mixer.Sound(path.join(snd_dir, 'turbosound.wav'))
    assets["score_font"] = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 12)
    assets["top_score_font"] = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 8)
    coins_anim = []
    for i in range(1,7):
        filename = "coin_{}.png".format(i)
        img = pygame.image.load(path.join(img_dir, filename)).convert()
        img = pygame.transform.scale(img, (32,32))
        img.set_colorkey(BLACK)
        coins_anim.append(img)
    assets['coin'] = coins_anim
    mobs_array=[]
    for i in range(1,5):
        filename = "mob{}.png".format(i)
        img = pygame.image.load(path.join(img_dir, filename)).convert()
        mobs_array.append(img)
    assets['mobs'] = mobs_array 
    explosion_anim = []
    for i in range(9):
        filename = 'regularExplosion0{}.png'.format(i)
        img = pygame.image.load(path.join(img_dir, filename)).convert()
        img = pygame.transform.scale(img, (32, 32))        
        img.set_colorkey(BLACK)
        explosion_anim.append(img)
    assets["explosion_anim"] = explosion_anim
    raposa_anim = []
    for i in range(1,5):
        filename = "raposa_{}.png".format(i)
        img = pygame.image.load(path.join(img_dir, filename)).convert()
        img = pygame.transform.scale(img, (20,40))
        img.set_colorkey(BLACK)
        raposa_anim.append(img)
    assets['raposa'] = raposa_anim
    grass_anim = []
    for i in range(1,6):
        filename = "grass_{}.png".format(i)
        img = pygame.image.load(path.join(img_dir, filename)).convert()
        img = pygame.transform.scale(img, (32,32))
        img.set_colorkey(BLACK)
        grass_anim.append(img)
    assets['grass'] = grass_anim
    return assets




#Classes
    
#Classe player
class Player(pygame.sprite.Sprite):
    #Construtor de classe
    def __init__ (self, player_img, road_speed):
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
        
        #Quantidade de dinheiro inicial
        self.cash = 0
        
        #Variavel road_speed
        self.road_speed = road_speed
        
        #Velocidade 
        self.speedx = 0
        self.speedy = self.road_speed
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.bottom += self.speedy
    
        
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
    def __init__ (self, tiles_img, tiles_y, road_speed):
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
        
        #Velocidade da tela
        self.road_speed = road_speed
        
        
    def update(self):
        self.rect.y += self.road_speed
        
        if self.rect.top >= HEIGHT:
            self.rect.bottom = self.rect.top - HEIGHT - 30


class Cerca(pygame.sprite.Sprite):
    #Construtor de classe
    def __init__ (self, cerca_img, cerca_y, cerca_x, road_speed):
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
        
        #velocidade de cerca
        self.road_speed = road_speed
        
    
    def update(self):
        self.rect.y += self.road_speed
        
        if self.rect.top >= HEIGHT:
            self.rect.bottom = self.rect.top - HEIGHT

class Boost(pygame.sprite.Sprite):
    #Construtor de classe
    def __init__ (self, boost_img, road_speed):
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
        
        self.rect.bottom = random.randint(-2000, -500)
        
        self.speed_up = False
        
        self.last_update = pygame.time.get_ticks()
        
        #Velocidade de tela
        self.road_speed = road_speed
        
        
    def update(self):
        self.rect.bottom += self.road_speed
        
        
        if self.rect.top >= HEIGHT:
            #Faz com que spawn longe da tela para controlar melhor a quantidade de spawn
            self.rect.y = random.randint(-2000, -500)
            self.rect.centerx = random.randint(70 , WIDTH-70)
            
        now = pygame.time.get_ticks()
        
        time_elapsed = now - self.last_update
        
        if time_elapsed > 2000:
            self.speed_up = False
                
                

class Coins(pygame.sprite.Sprite):
    #Construtor de classe.
    def __init__ (self, center, coins_anim, road_speed):
        #Construtor de classe pai.
        pygame.sprite.Sprite.__init__(self)
        
        #Carregar animacao de explosao.
        self.coins_anim = coins_anim
        
        #Inicia processo de animacao.
        self.frame = 0
        self.image = self.coins_anim[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.rect.y = random.randint(-2000, -500)
        
        #Guarda tick da primeira imagem
        self.last_update = pygame.time.get_ticks()
        
        #Controlle de ticks da animacao 1 tick = 1 milisegundo
        self.frame_ticks = 100
        
        #Velocidade da tela
        self.road_speed = road_speed
        
    
    def update(self):
        self.rect.y += self.road_speed
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
            if self.frame == len(self.coins_anim):
                #Se sim mate explosao.
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.coins_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
        if self.rect.y > HEIGHT:
            self.rect.x = random.randint(70, WIDTH-70)
            self.rect.y = random.randint(-2000, -500)


        
class Score(pygame.sprite.Sprite):
    #Construtor de classe
    def __init__ (self, score_img):
        #Construtor de classe pai
        pygame.sprite.Sprite.__init__(self)
        
        #Cria sprite
        self.image = score_img
        
        #Define tamanho
        self.image = pygame.transform.scale(score_img,(150,50))
        
        #Detalhe sobre posicionamento
        self.rect = self.image.get_rect()
        
        self.rect.top = 5
        self.rect.left = 5

#classe mobs (OPONENTS):
class Mobs(pygame.sprite.Sprite):
    def __init__(self, mobs_sprite, road_speed):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image = mobs_sprite
        
        #Define tamanho
        self.image = pygame.transform.scale(mobs_sprite,(40,55))
        
        #Detalhe sobre posicionamento
        self.rect = self.image.get_rect()
        
        #Deixa transparente
        self.image.set_colorkey(BLACK)
        
        #Centraliza no baixo da tela 
        self.rect.centerx = random.randint(70 , WIDTH-70)
        
        self.rect.bottom = random.randint(-2000, -500)
        
        self.road_speed = road_speed
        
    def update(self):
        self.rect.bottom += self.road_speed + 3
        
        if self.rect.top >= HEIGHT:
            #Faz com que spawn longe da tela para controlar melhor a quantidade de spawn
            self.rect.bottom = random.randint(-2000, -500)
    
# Classe que representa uma explosão de meteoro
class Explosion(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, center, explosion_anim, state):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Carrega a animação de explosão
        self.explosion_anim = explosion_anim

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0
        self.image = self.explosion_anim[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center

        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 50

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.explosion_anim):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center         
                
class Raposa(pygame.sprite.Sprite):
    #Construtor de classe.
    def __init__ (self, center, raposa_anim, road_speed, centerx):
        #Construtor de classe pai.
        pygame.sprite.Sprite.__init__(self)
        
        #Carregar animacao de explosao.
        self.raposa_anim = raposa_anim
        
        #Inicia processo de animacao.
        self.frame = 0
        self.image = self.raposa_anim[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center
      
        
        self.road_speed = road_speed
        
        #Guarda tick da primeira imagem
        self.last_update = pygame.time.get_ticks()
        
        #Controlle de ticks da animacao 1 tick = 1 milisegundo
        self.frame_ticks = 120
        
        self.centerx = centerx
        
    def update(self):
        self.rect.y += self.road_speed - 1
        #Verifica tick atual.
        now = pygame.time.get_ticks()
        
        #Verifica quantos ticks passaram des da ultima mudanca de frame
        elapsed_tick = now - self.last_update
        
        #Se ja esta na hora de mudar de imagem.
        if (elapsed_tick > self.frame_ticks):
            
            #Marca o tick da nova imagem.
            self.last_update = now
            
            #Verifica se acabou a animacao.
            if self.frame >= len(self.raposa_anim):
                #Se sim mate explosao.
                self.frame = 0
                
            else:
                center = self.rect.center
                self.image = self.raposa_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
                #Avanca um quadro.
                self.frame += 1
        
        if self.rect.top > HEIGHT:
            self.rect.x = self.centerx
            self.rect.y = random.randint(-10000, -500)
        

class Grass(pygame.sprite.Sprite):
    #Construtor de classe.
    def __init__ (self, center, grass_anim, frame, road_speed, centerx):
        #Construtor de classe pai.
        pygame.sprite.Sprite.__init__(self)
        
        #Carregar animacao de explosao.
        self.grass_anim = grass_anim
        
        #Inicia processo de animacao.
        self.frame = frame
        self.image = self.grass_anim[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center
      
        
        self.road_speed = road_speed
        
        #Guarda tick da primeira imagem
        self.last_update = pygame.time.get_ticks()
        
        #Controlle de ticks da animacao 1 tick = 1 milisegundo
        self.frame_ticks = 120
        
        self.centerx = centerx
        
    def update(self):
        self.rect.y += self.road_speed
        
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
        if self.rect.bottom > HEIGHT:
            self.rect.x = self.centerx
            self.rect.y = random.randint(-2000, -500)
        


def tela_do_jogo(screen):
    
    #Abre historico de jogador
    with open('historico_de_player.txt','r') as arquivo:
        texto = arquivo.read()
    
    dados = json.loads(texto)
    
    road_speed = 5 #Velocidade do carro

    #Variavel de relogio:
    clock = pygame.time.Clock()

    #Carrega os assets
    assets = load_assets(img_dir, snd_dir)
    
    #carrega os sons do jogo
    pygame.mixer.music.load(path.join(snd_dir, 'carsound.wav'))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)
    crash_sound=assets['crash']
    car_sound=assets['carsound']
    boost_sound=assets['boostsound']
    coin_sound=assets['coinsound']

    #Carrega skin de player
    player_img = assets['player_img']
    car_selected = dados["car_selected"] - 1

    # Carrega a fonte para desenhar o score.
    score_font = assets["score_font"]
    top_score_font = assets["top_score_font"]

    #Carrega fundo
    background = assets["background"]
    background_rect = background.get_rect()

    #Cria a variavel que contem classes
    score_board = Score(assets["score_board"])
    
    
    player = Player(player_img[car_selected], road_speed)

    coin = Coins((random.randint(70, WIDTH - 70),0),assets['coin'], road_speed)

    speed_boost = Boost(assets['speed_boost'], road_speed)
    
    raposa_left = Raposa((16, -1000), assets['raposa'], road_speed, 16)
    raposa_right = Raposa((WIDTH - 16, -2000), assets['raposa'], road_speed, WIDTH - 16)
    
    #Adiciona sprite 
    all_sprites = pygame.sprite.Group()

    tiles_sprites = pygame.sprite.Group()

    cerca_sprites = pygame.sprite.Group()
    
    mobs_sprites = pygame.sprite.Group()
    
    grass_sprites = pygame.sprite.Group()

    #Loops que criam plano de fundo e mobs
    tile_y = 0

    for i in range(7):
        i = Tiles(assets['tiles'], tile_y, road_speed)
        tile_y -= 100
        tiles_sprites.add(i)

    cerca_y = 0

    for i in range(12):
        i = Cerca(assets['cerca'], cerca_y, 40, road_speed)
        ii = Cerca(assets['cerca'], cerca_y, WIDTH - 40, road_speed)
        cerca_y -= 60
        cerca_sprites.add(i)
        cerca_sprites.add(ii)
    
    for i in assets["mobs"]:
        ii = Mobs(i, road_speed)
        mobs_sprites.add(ii)
    
    grass_y = -500
    for i in range(1,4):
        frame = random.randint(0,4)
        i = Grass((10,grass_y), assets['grass'], frame, road_speed, 6)
        grass_sprites.add(i)
        grass_y += 13
        
    grass_y = -200
    for i in range(1,4):
        frame = random.randint(0,4)
        i = Grass((385, grass_y), assets['grass'], frame, road_speed, WIDTH - 20)
        grass_sprites.add(i)
        grass_y += 13


    all_sprites.add(cerca_sprites)
    all_sprites.add(tiles_sprites)
    all_sprites.add(speed_boost)
    all_sprites.add(coin)
    all_sprites.add(mobs_sprites)
    all_sprites.add(player)
    all_sprites.add(raposa_right)
    all_sprites.add(raposa_left)
    all_sprites.add(grass_sprites)
    all_sprites.add(score_board)

    
    PLAYING = 0
    DONE = 2

    state = PLAYING
    while state != DONE:
        #Ajusta velocidade de jogo
        clock.tick(FPS)
        
        if state == PLAYING:
            # Processa os eventos
            for event in pygame.event.get():
            
                # Verifica se foi fechado
                if event.type == pygame.QUIT:
                    state = DONE
                
                #Verifica se clica tecla
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.speedx = -3
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 3
                    if event.key == pygame.K_UP:
                        player.speedy = -5
                    

                #Verifica se tecla soltou
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.speedx = 0
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 0
                    if event.key == pygame.K_UP:
                        player.speedy = player.road_speed
                
                #Colisao com o boost
            boost_on = pygame.sprite.collide_rect(player, speed_boost)
            if boost_on:
                boost_sound.play()
                speed_boost.speed_up = True
                speed_boost.last_update = pygame.time.get_ticks()
                
            #Colisao com a moeda
            get_coin = pygame.sprite.collide_rect(player, coin)
            if get_coin:
                coin_sound.play()
                coin.rect.y = random.randint(-2000, -500)
                player.cash += 10
                
            #Colisao com os mobs
            hit_mobs = pygame.sprite.spritecollide(player, mobs_sprites, False, pygame.sprite.collide_rect)
            if hit_mobs:
                pygame.mixer.music.stop()
                boost_sound.stop()
                crash_sound.play()
                explosao = Explosion(player.rect.center, assets["explosion_anim"], state)
                all_sprites.add(explosao)
                pygame.time.wait(1500)
                state = DONE
                
                
        
        if state == PLAYING:
            if speed_boost.speed_up:
                road_speed = 12
                
            else:
                road_speed = 5
                
        #Atualoza road_speed
        for sp in all_sprites:
            sp.road_speed = road_speed
            
        #Atualiza sprites depois de cada evento
        all_sprites.update()
        
        
    
            
        #Cada loop redesenha os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Desenha o score
        text_surface = score_font.render("Score:{0}".format(player.cash), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.left = (15)
        text_rect.top = (18)
        screen.blit(text_surface, text_rect)
        
        text_surface = top_score_font.render("Top Score:{0}".format(dados['top_score']), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.left = (13)
        text_rect.top = (38)
        screen.blit(text_surface, text_rect)
        
        #Depois de desenhar inverte o display
        pygame.display.flip()
        
        #Escreve cash do jogador na biblio json
        if dados['top_score'] < player.cash:    
            dados['top_score'] = player.cash
            json_dados = json.dumps(dados, sort_keys = True, indent = 4)
            with open('historico_de_player.txt','w') as arquivo:
                arquivo.write(json_dados)
        
    return INIT