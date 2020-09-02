import pygame
import psutil

# Iniciando a janela principal
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Exemplo Surface")
pygame.display.init()

azul = (0, 0, 255)

s1 = pygame.surface.Surface((largura_tela, altura_tela/3))
s2 = pygame.surface.Surface((largura_tela, altura_tela/3))
s3 = pygame.surface.Surface((largura_tela, altura_tela/3))

pygame.draw.rect(s1, azul, (20, 50, largura_tela-2*20, 70))
tela.blit(s1, (0, 0))

pygame.draw.rect(s2, azul, (20, 50, largura_tela-2*20, 70))
tela.blit(s2, (0, altura_tela/3))

pygame.draw.rect(s3, azul, (20, 50, largura_tela-2*20, 70))
tela.blit(s3, (0, 2*altura_tela/3))

# Cria relógio
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
