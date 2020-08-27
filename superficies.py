import psutil
import platform
import time
import pygame


largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Surface")
pygame.display.init()

preto = (0, 0, 0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
branco = (255, 255, 255)

pygame.font.init()
font = pygame.font.SysFont(None, 55)

superficie1 = pygame.surface.Surface((largura_tela, altura_tela/3))
superficie2 = pygame.surface.Surface((largura_tela, altura_tela/3))
superficie3 = pygame.surface.Surface((largura_tela, altura_tela/3))


pygame.draw.rect(superficie1, azul, (20, 50, largura_tela-2*20, 70))
tela.blit(superficie1, (0, 0))

pygame.draw.rect(superficie2, azul, (20, 50, largura_tela-2*20, 70))
tela.blit(superficie2, (0, altura_tela/3))

pygame.draw.rect(superficie3, azul, (20, 50, largura_tela-2*20, 70))
tela.blit(superficie3, (0, 2 * altura_tela/3))


clock = pygame.time.Clock()

terminou = False
while not terminou:

  # Checar os eventos do mouse aqui:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          terminou = True

  # Atualiza o desenho na tela
  pygame.display.update()
  # 60 frames por segundo
  clock.tick(60)

# Finaliza a janela
pygame.display.quit()










