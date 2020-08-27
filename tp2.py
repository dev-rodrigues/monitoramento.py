import psutil
import platform
import time
import pygame

memoria = psutil.virtual_memory()

capacidade = round(memoria.total/(1024*1024*1024), 2)
# print(capacidade)

# informações do processador
processador = platform.processor()
# print(processador)

# informações da rede
rede = platform.node()
# print(rede)

# detalhes da plataforma
plataforma = platform.platform()
# print(plataforma)

# sistema operacional
sistema = platform.system()
# print(sistema)

percentual_cpu = psutil.cpu_percent()
# print(percentual_cpu)

# fazendo o pc trabalhar para ver o percentual subir
# for i in range(0, 100):
#     print(psutil.cpu_percent())
#     time.sleep(i)

# informações do disco
disco = psutil.disk_usage('/')
total_disco = disco.total
disco_usado = disco.used
disco_livre = disco.free

# print(round(total_disco / (1024 * 1024 * 1024), 2))
# print(round (disco_usado / (1024 * 1024 * 1024), 2))
# print(round (disco_livre / (1024 * 1024 * 1024), 2))

# percentual do disco
percentual_disco = disco.percent
# print(percentual_disco)

dic_interfaces = psutil.net_if_addrs()
# print(dic_interfaces)


########################################################################
# Mostar uso de memória
def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    larg = largura_tela - 2*20
    tela.fill(preto)
    pygame.draw.rect(tela, azul, (20, 50, larg, 70))
    larg = larg * mem.percent/100
    pygame.draw.rect(tela, vermelho, (20, 50, larg, 70))
    total = round(mem.total/(1024*1024*1024),2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 10))
    
def mostra_uso_cpu():
    capacidade = psutil.cpu_percent(interval=0)
    larg = largura_tela - 2*20
    tela.fill(preto)
    pygame.draw.rect(tela, azul, (20, 50, larg, 70))
    larg = larg * capacidade/100
    pygame.draw.rect(tela, vermelho, (20, 50, larg, 70))
    text = font.render("Uso de CPU:", 1, branco)
    tela.blit(text, (20, 10))
    
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
    


largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Uso de memória")

preto = (0, 0, 0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
branco = (255, 255, 255)

pygame.font.init()
font = pygame.font.SysFont(None, 55)

pygame.display.init()

clock = pygame.time.Clock()

terminou = False
count = 60

while not terminou:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    
    if count == 60:
        # mostra_uso_memoria()
        mostra_uso_cpu()
        #mostra_uso_disco()
        count = 0    
        
    pygame.display.update()
    clock.tick(60)
        
pygame.display.quit()


































