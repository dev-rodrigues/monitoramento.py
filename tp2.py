import psutil
import platform

memoria = psutil.virtual_memory()

capacidade = round(memoria.total/(1024*1024*1024), 2)
# print(capacidade)

# informações do processador
processador = platform.processor()
print(processador)

# informações da rede
rede = platform.node()
print(rede)

# detalhes da plataforma
plataforma = platform.platform()
print(plataforma)

# sistema operacional
sistema = platform.system()
print(sistema)