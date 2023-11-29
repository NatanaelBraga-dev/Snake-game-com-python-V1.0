import pygame 
from pygame.locals import *
from sys import exit

#importaremos a função random para que a posição do retângulo vermelho mude a cada colisão
from random import randint

pygame.init()
pygame.mixer.init()

som = pygame.mixer.music.load('C:/Users/Natanael/Python VScode/pygame/smw_coin.wav')


relogio=pygame.time.Clock()

largura= 640
altura= 480

x_cobra = largura/2 - 50/2
y_cobra = altura/2

x_controle = 20
y_controle = 0
velocidade= 5

x_maça = randint(40,600)
y_maça = randint(50,430)

tela= pygame.display.set_mode((largura,altura))
pygame.display.set_caption('snake game beta')

pontos = 0
font= pygame.font.Font('freesansbold.ttf',40)

lista_corpo=[]
comprimento_inicial = 5 

#função que aumenta a cobra 
def aumenta_cobra(lista_corpo):
    for XeY in lista_corpo:
        pygame.draw.rect(tela,(0,255,0),(XeY[0],XeY[1],20,20))


#é preciso deixar a parte de criação do retângulo do texto dentro do loop while caso você queira que a cor permaneça a que você escolheu dps que a tela atualizar

while True:
    text = font.render('Pontos:'+ str(pontos),True,(255,255,255),(0,0,255))
    textrect = text.get_rect()
    textrect.center = (450,40)
    relogio.tick(60)
    tela.fill((0,0,255))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()

#essa é a parte do código que vai permitir a movimentação do meu objeto
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else: 
                    x_controle = velocidade
                    y_controle = 0 
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0 
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0 
    
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle 

#essa parte do código permite que toda vez que objeto saia da tela ele volte para o ponto de partida 
    if y_cobra>=altura:
        y_cobra = 0
    if x_cobra> largura:
        x_cobra = 0
    if y_cobra<0:
        y_cobra = 480
    if x_cobra < 0:
        x_cobra = 640
    
    cobra = pygame.draw.rect(tela,(0,255,0),(x_cobra,y_cobra,20,20))
    maça = pygame.draw.rect(tela,(255,0,0),(x_maça,y_maça,20,20))

# agora vamos criar o nosso método para colisão 
    if cobra.colliderect(maça):
        x_maça = randint(40,600)
        y_maça = randint(50,430)
        pontos = pontos + 1
        text = font.render('Pontos:'+ str(pontos),True,(255,255,255),(0,0,0)) 
        pygame.mixer.music.play()
        pygame.event.wait()
        comprimento_inicial = comprimento_inicial + 1 

    lista_cabeça=[]
    lista_cabeça.append(x_cobra)
    lista_cabeça.append(y_cobra)
    
    lista_corpo.append(lista_cabeça)

#essa parte do código impede que a cobra cresça indefinidamente 
    if len(lista_corpo) > comprimento_inicial:
        del lista_corpo[0]
  
    aumenta_cobra(lista_corpo)


# agora toda vez que os retângulos colidirem o vermelho mudará de posição
    tela.blit(text,textrect)
    pygame.display.update()