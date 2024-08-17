import sys
import pygame
from pygame.locals import *
from sys import exit
import time
import random

pygame.init()

largura = 640
altura = 480

x_l= largura -600
y_l = altura/2

x_r= largura -40
y_r = altura/2

ball_x = largura // 2
ball_y = altura // 2


cont = 0

ball_speed_x = 5
ball_speed_y = 5


# Configurações de Tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Pong')
relogio = pygame.time.Clock()

while True:
    relogio.tick(60)
    tela.fill((0,0,0))

    hori_line = pygame.draw.line(tela, (192, 192, 192), (largura // 2, 40), (largura // 2, altura - 40), 5)
    #eli = pygame.draw.
    rec_left = pygame.draw.rect(tela, (255, 255, 255), (x_l, y_l, 10, 60))
    rec_right = pygame.draw.rect(tela, (255, 255, 255), (x_r, y_r, 10, 60))
    circle = pygame.draw.circle(tela, (255, 0, 255), (ball_x, ball_y), 5)



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    ball_x += ball_speed_x
    ball_y += ball_speed_y




    # Colisão da bola com as bordas superiores e inferiores
    if ball_y - 5 <= 0 or ball_y + 5 >= altura:
        ball_speed_y =-ball_speed_y  # Inverter a direção no eixo y



     # Quando a bolinha sai para bate em uma das paredes laterais ela retorna ao meio
    if ball_x - 5 <= 0 or ball_x + 5 >= largura:
        # Configuração para a velocidade da bolinha voltar ao inicio
        cont = 0
        ball_speed_y = 5
        ball_speed_x = 5
          #bola retorna ao centro da tela
        ball_x = largura // 2
        ball_y = altura // 2


    # Colisão com as raquetes
    if circle.colliderect(rec_left):
        ball_speed_x = -ball_speed_x
        ball_x = rec_left.right + 5
        cont += 1
        if cont % 10 == 0:
            ball_speed_x += 1 if ball_speed_x > 0 else -1
            ball_speed_y += 1 if ball_speed_y > 0 else -1

        print(cont)
        print(ball_speed_x)
        print(ball_speed_y)

    elif circle.colliderect(rec_right):
        ball_speed_x = - ball_speed_x
        ball_x = rec_right.left - 5
        cont += 1
        if cont % 10 == 0:
            ball_speed_x += 1 if ball_speed_x > 0 else -1
            ball_speed_y += 1 if ball_speed_y > 0 else -1
        print(cont)
        print(ball_speed_x)
        print(ball_speed_y)

    # Pega as teclas pressionadas
    if pygame.key.get_pressed()[K_w]:
        y_l -= 10
    elif pygame.key.get_pressed()[K_s]:
        y_l += 10

    if pygame.key.get_pressed()[K_i]:
        y_r -= 10
    elif pygame.key.get_pressed()[K_k]:
        y_r += 10


    # Define limite das raquetes
    if y_l < 0:
        y_l = 0
    elif y_l > altura - 55:
        y_l = altura - 55


    if y_r < 0:
        y_r = 0
    elif y_r > altura - 55:
       y_r = altura - 55


    pygame.display.update()