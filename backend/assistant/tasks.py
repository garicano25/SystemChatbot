from celery import shared_task
import time

@shared_task
def tarea_prueba(nombre):
    print(f"Iniciando tarea para {nombre}...")
    time.sleep(5)  # Simula trabajo
    print(f"Tarea finalizada para {nombre}")
    return f"Tarea terminada para {nombre}"
