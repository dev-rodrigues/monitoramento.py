import psutil
import platform
import time
import pygame

# tamanho da tela
largura_tela = 800
altura_tela = 600

# cores disponiveis
preto = (0, 0, 0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
branco = (255, 255, 255)
cinza = (100, 100, 100)

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Carlos Henrique Info")

superficie_dados = pygame.surface.Surface((largura_tela, int(altura_tela/3)))
superficie_memoria = pygame.surface.Surface((largura_tela, int(altura_tela/3)))
superficie_cpu = pygame.surface.Surface((largura_tela, int(altura_tela/3)))
#superficie_disco = pygame.surface.Surface((largura_tela, 200))

pygame.font.init()
font = pygame.font.SysFont(None, 55)
pygame.display.init()
clock = pygame.time.Clock()

# deve desenhar um grafico com o total de memoria usado
def mostra_uso_memoria(s):
    s.fill(cinza)

    mem = psutil.virtual_memory()
    larg = largura_tela - 2*20
    tela.fill(preto)
    
    pygame.draw.rect(tela, azul, (20, 50, larg, 70))
    larg = larg * mem.percent/100
    
    pygame.draw.rect(tela, vermelho, (20, 50, larg, 70))

    total = round(mem.total/(1024*1024*1024),2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    tela.blit(s, (0, 0))

# deve desenhar um gráfico com o total de cpu usado
def mostrasuperficie_uso_cpu(s):
    s.fill(cinza)

    capacidade = psutil.cpu_percent(interval=0)
    larg = largura_tela - 2*20
    tela.fill(preto)

    pygame.draw.rect(tela, azul, (20, 50, larg, 70))
    larg = larg * capacidade/100
    
    pygame.draw.rect(tela, vermelho, (20, 50, larg, 70))
    text = font.render("Uso de CPU:", 1, branco)
    #s.blit(text, (20, 100))
    tela.blit(s, (0, 0))

# deve desenhar um gráfico com o total de disco usado
def mostra_uso_disco():
    disco = psutil.disk_usage('.')
    larg = largura_tela - 2*20
    tela.fill(preto)
    pygame.draw.rect(tela, azul, (20, 50, larg, 70))
    larg = larg * disco.percent/100
    pygame.draw.rect(tela, vermelho, (20, 50, larg, 70))
    total = round(disco.total/(1024*1024*1024), 2)
    texto_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 10))

# deve escrever os dados de rede
def escrever_dados():
    superficie_dados.fill(branco)
    mostra_texto(superficie_dados, "IP:", 10)
    tela.blit(superficie_dados, (0, 0))

def mostra_texto(s1, nome, pos_y):
    text = font.render(nome, True, preto)
    superficie_dados.blit(text, (10, pos_y))

################################APLICACAO#######################################

terminou = False
count = 60

while not terminou:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    
    if count == 60:
        mostra_uso_memoria(superficie_memoria)
        escrever_dados()
        #mostra_uso_cpu(superficie_cpu)
        #mostra_uso_disco()
        count = 0    
        
    pygame.display.update()
    clock.tick(60)
        
pygame.display.quit()
