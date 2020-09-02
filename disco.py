import pygame
import psutil
import cpuinfo

disco = psutil.disk_usage('/')

# bytes
print("Total:", disco.total, "B")

# usado
print("Em uso:", disco.used, "B")

# disponivel
print("Livre:", disco.free, "B")


print("Total:", round(disco.total/(1024**3), 2), "GB")
#print("Em uso:", round(disco.used/(1024**3), 2), "GB")
#print("Livre:", round(disco.free/(1024**3), 2), "GB")

#
#print("Percentual de Disco Usado:", disco.percent)
