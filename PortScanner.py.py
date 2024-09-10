import socket
from datetime import datetime

# Definir la dirección IP del objetivo
def scan_ports(target, port_range):
    print(f"Escaneando {target} para los puertos en el rango {port_range[0]}-{port_range[1]}")
    # Registrar el inicio
    start_time = datetime.now()

    # Intentar resolver el nombre de dominio a una IP
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Nombre de dominio {target} no resuelto.")
        return

    print(f"Iniciando escaneo en: {target_ip}\n")

    # Escaneo de puertos en el rango dado
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # Intentar conectar al puerto
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Puerto {port} está ABIERTO")
        else:
            print(f"Puerto {port} está CERRADO")
        sock.close()

    # Registrar el tiempo final
    end_time = datetime.now()
    print(f"\nEscaneo completado en {end_time - start_time}")

# Ejecutar la función
if __name__ == "__main__":
    target = input("Introduce la IP o dominio del objetivo: ")
    port_range = (int(input("Puerto inicial: ")), int(input("Puerto final: ")))
    scan_ports(target, port_range)
