import socket
from datetime import datetime

def scan_ports(target, port_range):
    print(f"Escaneando {target} para los puertos en el rango {port_range[0]}-{port_range[1]}")
    
    start_time = datetime.now()

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Error: No se pudo resolver el dominio {target}.")
        return

    print(f"Iniciando escaneo en: {target_ip}\n")

    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Puerto {port} está ABIERTO")
        else:
            print(f"Puerto {port} está CERRADO")
        
        sock.close()

    end_time = datetime.now()
    print(f"\nEscaneo completado en {end_time - start_time}")

if __name__ == "__main__":
    target = input("Introduce la IP o dominio del objetivo: ")
    port_range = (int(input("Puerto inicial: ")), int(input("Puerto final: ")))
    scan_ports(target, port_range)
