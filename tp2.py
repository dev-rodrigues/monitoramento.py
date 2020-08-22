import psutil
import platform
import time

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

# fazendo o pc trabalhar para ver o percentual
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




