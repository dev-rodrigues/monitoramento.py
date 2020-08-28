import pygame
import psutil
import cpuinfo

info_cpu = cpuinfo.get_cpu_info()
psutil.cpu_percent(interval=1, percpu=True)

preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (100, 100, 100)
azul = (0, 0, 255)
vermelho = (255, 0, 0)

largura_tela = 1050
altura_tela = 600

# configurações da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Informações de CPU")
pygame.display.init()

# configurando a fonte
pygame.font.init()
font = pygame.font.SysFont(None, 20)

superficie = pygame.surface.Surface((largura_tela, 200))
superficie_grafico = pygame.surface.Surface((largura_tela, 400))

clock = pygame.time.Clock()

terminou = False
count = 60

# escreve na superficie 1 os dados estáticos
def mostra_info_cpu():
    superficie.fill(branco)
    mostra_texto(superficie, "Nome:", "brand_raw", 110)
    mostra_texto(superficie, "Arquitetura:", "arch", 30)
    mostra_texto(superficie, "Palavra (bits):", "bits", 50)
    mostra_texto(superficie, "Frequência (MHz):", "hz_actual_friendly", 70)
    mostra_texto(superficie, "Núcleos (físicos):", "count", 90)
    tela.blit(superficie, (0, 0))
    
# Escreve de acordo com a chave presente em info_cpu
def mostra_texto(s1, nome, chave, pos_y):
    text = font.render(nome, True, preto)
    s1.blit(text, (40, pos_y))
    if chave == "freq":
        s = str(round(psutil.cpu_freq().current, 2))
        
    elif chave == "nucleos":
        s = str(psutil.cpu_count())
        s = s + " (" + str(psutil.cpu_count(logical=False)) + ")"
        
    else:
        s = str(info_cpu[chave])
        text = font.render(s, True, cinza)
        superficie.blit(text, (155, pos_y))

# Desenha grafico  
def mostrar_uso_cpu(s, l_cpu_percent):
    s.fill(cinza)
    num_cpu = len(l_cpu_percent)
    x = y = 10
    desl = 10
    alt = s.get_height() - 2*y
    larg = (s.get_width()- 2*y - (num_cpu+1) * desl) / num_cpu
    d = x + desl
    
    for i in l_cpu_percent:
        pygame.draw.rect(s, vermelho, (d, y, larg, alt))
        pygame.draw.rect(s, azul, (d, y, larg, (1-i/100)*alt))
        d = d + larg + desl
        tela.blit(s, (0, altura_tela/5))

while not terminou:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
            
    if count == 60:
        mostra_info_cpu()
        teste = psutil.cpu_percent(percpu=True)
        mostrar_uso_cpu(superficie_grafico, teste)
        count = 0    
        
    pygame.display.update()
    
    clock.tick(60)
    count = count + 1
        
pygame.display.quit()
