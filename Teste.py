import pygame
import psutil
import cpuinfo

info_cpu = cpuinfo.get_cpu_info()

# for i in info:
#     print(i, ":", info[i])

preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (100, 100, 100)

largura_tela = 1050
altura_tela = 600

# configurações da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Informações de CPU")
pygame.display.init()

# configurando a fonte
pygame.font.init()
font = pygame.font.SysFont(None, 55)


superficie = pygame.surface.Surface((largura_tela, altura_tela/3))

clock = pygame.time.Clock()

terminou = False
count = 60


def mostra_info_cpu():
    superficie.fill(branco)
    mostra_texto(superficie, "Nome:", "brand_raw", 50)
    mostra_texto(superficie, "Arquitetura:", "arch", 30)
    mostra_texto(superficie, "Palavra (bits):", "bits", 50)
    mostra_texto(superficie, "Frequência (MHz):", "hz_actual_friendly", 70)
    mostra_texto(superficie, "Núcleos (físicos):", "count", 90)
    tela.blit(superficie, (0, 0))
    
# Mostra texto de acordo com uma chave:
def mostra_texto(s1, nome, chave, pos_y):
    text = font.render(nome, True, preto)
    s1.blit(text, (30, pos_y))
    if chave == "freq":
        s = str(round(psutil.cpu_freq().current, 2))
        
    elif chave == "nucleos":
        s = str(psutil.cpu_count())
        s = s + " (" + str(psutil.cpu_count(logical=False)) + ")"
        
    else:
        s = str(info_cpu[chave])
        text = font.render(s, True, cinza)
        superficie.blit(text, (350, pos_y))


while not terminou:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    
    if count == 60:
        mostra_info_cpu()
        count = 0    
        
    pygame.display.update()
    clock.tick(60)
        
pygame.display.quit()
  
  
  
  
  
  
  