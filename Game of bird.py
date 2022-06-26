import pygame
import os
import random

tela_altura = 700
tela_largura = 550

img_cano = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
img_chao = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
img_fundo = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
imgs_passaro =  [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
]

pygame.font.init()
fonte_pontuacao = pygame.font.SysFont('arial', 50)

class Passaro:
    """Iniciando a orientação a objeto..."""
    imgs = imgs_passaro
    #definindo as animações da rotação...
    rot_max = 25
    vel_rot = 20
    tmp_anim = 5

    def __init__(self, x, y):
        """Começando as configurações do pássaro..."""
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem = 0
        self.imagem = imgs[0]

    def pular (self):
        """Atribuindo a função de pular ao personagem..."""
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover (self):
        """Atribuindo movimento ao personagem..."""
        #calculando o deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo 

        #limitando o  deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento
        #angulo do personagem
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.rot_max:
                self.angulo = self.rot_max
        else:
            if self.angulo > -90:
                self.angulo -= self.vel_rot



class Chao:
    pass

class Cano:
    pass