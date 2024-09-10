import socket
from datetime import datetime

def scan_ports(target, port_range):
    """
    Escanea los puertos de un objetivo (IP o dominio) en un rango específico.

    :param target: Dirección IP o dominio del objetivo.
    :param port_range: Tupla que define el rango de puertos a escanear (puerto_inicial, puerto_final).
    """
    print(f"Escaneando {target} para los puertos en el rango {port_range[0]}-{port_range[1]}")
    
    # Registrar el inicio del escaneo
    start_time = datetime.now()

    # Intentar resolver el nombre de dominio a una IP
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Error: No se pudo resolver el dominio {target}.")
        return

    print(f"Iniciando escaneo en: {target_ip}\n")

    # Escaneo de puertos en el rango dado
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Definir un timeout de 1 segundo para cada conexión

        # Intentar conectar al puerto
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Puerto {port} está ABIERTO")
        else:
            print(f"Puerto {port} está CERRADO")
        
        # Cerrar el socket
        sock.close()

    # Registrar el tiempo final y calcular la duración del escaneo
    end_time = datetime.now()
    print(f"\nEscaneo completado en {end_time - start_time}")


if __name__ == "__main__":
    # Solicitar IP o dominio objetivo y el rango de puertos a escanear
    target = input("Introduce la IP o dominio del objetivo: ")
    port_range = (int(input("Puerto inicial: ")), int(input("Puerto final: ")))

    # Ejecutar el escaneo de puertos
    scan_ports(target, port_range)

