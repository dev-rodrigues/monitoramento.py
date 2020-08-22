import psutil
import platform

memoria = psutil.virtual_memory()

capacidade = round(memoria.total/(1024*1024*1024), 2)
print(capacidade)