import subprocess
#Author Almy

# Arp-scan  

def escanear_red_arp(interface):
    try:
        comando = ["arp-scan", "--interface", interface, "--localnet", "--ignoredups"]
        resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if resultado.returncode == 0:
            print(resultado.stdout)
        else:
            print("Ocurrió un error al ejecutar arp-scan:")
            print(resultado.stderr)
    except Exception as e:
        print("Ocurrió un error:", e)

# Solicitar la interfaz de red al usuario
interfaz_red = input("Ingresa el nombre de la interfaz de red (por ejemplo, 'eth0, wlan0, etc'): ")

# Llamar a la función para escanear la red utilizando arp-scan
escanear_red_arp(interfaz_red)

#NMAP

def escanear_ip_con_nmap(direccion_ip, opcion):
    opciones = {
        "1": ["nmap", "-p-", "--open", "--min-rate", "5000", "-T5", "-sS", "-Pn", "-n", "-v", direccion_ip],
        "2": ["nmap", "-p-", "--open", direccion_ip],
        "3": ["nmap", "-p-", "-T2", "-sS", "-Pn", "-f", direccion_ip],
        "4": ["nmap", "-sVC", direccion_ip]
    }

    comando = opciones.get(opcion)

    if comando is None:
        print("Opción no válida")
        return

    try:
        resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if resultado.returncode == 0:
            print(resultado.stdout)
        else:
            print("Ocurrió un error al ejecutar nmap:")
            print(resultado.stderr)
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar nmap:", e)
    except Exception as e:
        print("Ocurrió un error:", e)

# Solicitar la dirección IP al usuario
direccion_ip = input("Ingresa la dirección IP a escanear: ")

# Solicitar la opción al usuario
opcion = input("Seleccione una opción (1-4): ")

# Llamar a la función para escanear la IP utilizando nmap
escanear_ip_con_nmap(direccion_ip, opcion)
