### Imports ###
import time
import tracemalloc

# Decorator para medir tempo de execução
def medirTempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter() # Marca o tempo de início
        resultado = func(*args, **kwargs) # Chama a função original
        fim = time.perf_counter() # Marca o fim da medição
        tempo = 1000 * (fim - inicio) # Calcula e converte o tempo decorrido para ms
        return {'resultado' : resultado, 'tempo' : tempo} # Retorna o resultado da função original
    return wrapper

# Decorator para medir uso de memória
def medirMemoria(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start() # Inicia o rastreamento de alocação de memória
        resultado = func(*args, **kwargs) # Chama a função original
        memoria = tracemalloc.get_traced_memory() # Obtém a memória atual e o pico de uso
        tracemalloc.stop() # Termina o rastreamento de alocação de memória
        memoria = memoria[1] / 1024 # Converte o pico de memória para KB
        return {'resultado' : resultado, 'memoria' : memoria} # Retorna o resultado da função original
    return wrapper

def executar(func, *args, **kwargs):
    tempo = medirTempo(func)(*args, **kwargs)
    memoria = medirMemoria(func)(*args, **kwargs)
    return {
        'resultado': tempo['resultado'],
        'tempo': tempo['tempo'],
        'memoria': memoria['memoria']
    }