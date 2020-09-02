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
Dim = (105,105,105)
branco = (255, 255, 255)
cinza = (100, 100, 100)

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Carlos Henrique Info")

superficie_dados = pygame.surface.Surface((largura_tela, 50))
superficie_cpu = pygame.surface.Surface((largura_tela, int(altura_tela/3)))
superficie_memoria = pygame.surface.Surface((largura_tela, int(altura_tela/3)))
superficie_disco = pygame.surface.Surface((largura_tela, int(altura_tela/2)))

pygame.font.init()
font = pygame.font.SysFont(None, 55)
pygame.display.init()
clock = pygame.time.Clock()

# deve escrever os dados de rede
def escrever_dados():
  superficie_dados.fill(preto)

  plataforma = "IP: " + getIp()
  
  mostra_texto(superficie_dados, plataforma, 10)
  tela.blit(superficie_dados, (20, 0))
  
def mostra_texto(s1, nome, pos_y):
  text = font.render(nome, True, branco)
  superficie_dados.blit(text, (10, pos_y))

# obter o endereco de ip do usuario baseado no S.O
def getIp():
  plataforma = platform.system()
  dic_interfaces = psutil.net_if_addrs()

  if plataforma == 'Linux':
    ip = (dic_interfaces['wlp3s0'][0].address)
    return ip
  elif plataforma == "Windows":
    ip = (dic_interfaces['Ethernet'][1].address)
    return ip
  else:
    ip = (dic_interfaces['wlp3s0'][0].address)
    return ip

# desenhar uso cpu
def mostra_uso_cpu():
  capacidade = psutil.cpu_percent(interval=0.1)  
  larg = largura_tela - 2*20

  pygame.draw.rect(superficie_cpu, azul, (20, 50, larg/2, 70))
  larg = larg * capacidade/100

  pygame.draw.rect(superficie_cpu, Dim, (20, 50, larg/2, 70))
  cpu = psutil.cpu_percent()
  
  frase = "Uso de CPU: " + str(capacidade)
  texto = font.render(frase, 1, branco)
  superficie_cpu.blit(texto, (20, 10))
  tela.blit(superficie_cpu, (20, 100))

# deve desenhar um grafico com o total de memoria usado
def mostra_uso_memoria():
  mem = psutil.virtual_memory()
  larg = largura_tela - 2*20
  
  pygame.draw.rect(superficie_memoria, azul, (20, 50, larg/2, 70))
  larg = larg * mem.percent/100
  
  pygame.draw.rect(superficie_memoria, Dim, (20, 50, larg/2, 70))

  total = round(mem.total/(1024*1024*1024), 2)
  texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
  texto = font.render(texto_barra, 1, branco)
  
  superficie_memoria.blit(texto, (20, 10))
  tela.blit(superficie_memoria, (20, 250))
  
# deve desenhar um gráfico com o total de disco usado
def mostra_uso_disco():
    disco = psutil.disk_usage('/')
    larg = largura_tela - 2*20
    
    pygame.draw.rect(superficie_disco, azul, (20, 50, larg/2, 70))
    larg = larg * disco.percent/100
    
    pygame.draw.rect(superficie_disco, Dim, (20, 50, larg/2, 70))
    total = round(disco.total/(1024*1024*1024), 2)
    
    texto_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
    texto = font.render(texto_barra, 1, branco)
    superficie_disco.blit(texto, (20, 10))
    tela.blit(superficie_disco, (20, 410))

terminou = False
count = 60

while not terminou:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          terminou = True
  
    if count == 60:
        escrever_dados()
        mostra_uso_cpu()
        mostra_uso_memoria()
        mostra_uso_disco()
        count = 0    
     
    pygame.display.update()
    clock.tick(60)
    count = count + 1
    
pygame.display.quit()
