import pygame
import psutil
import cpuinfo


mem = psutil.virtual_memory()
capacidade = round(mem.total/(1024**3),  2)
disponivel = round(mem.available/(1024**3), 2)

print("Capacidade total:", capacidade, "GB")
print("Disponivel:", disponivel, "GB")
