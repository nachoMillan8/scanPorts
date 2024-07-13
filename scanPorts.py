import socket


rojo = "\033[31m"
verde = "\033[32m"
amarillo = "\033[33m"
azul = "\033[34m"
estandar = "\033[0m"

print("""
        ESCANEO DE PUERTOS ABIERTOS
            
                    by nachoMillan8
""")

def scanPorts(objetivo):
    print(f"Escaneando puertos de: {objetivo}")

    for puerto in range(442, 444): #Establecer el rango de puertos que querramos escanear
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #establece conexion TCP/IP
        socket.setdefaulttimeout(1) # Establecemos un tiempo de espera para que en caso de que un puerto no responda no quede bloqueado el programa 
        resultado = s.connect_ex((objetivo, puerto)) # conexion al puerto
        if resultado == 0:
            print(f"El puerto {amarillo}{puerto}{estandar} está {verde}ABIERTO{estandar}")
        s.close()




try:
    objetivo = socket.gethostbyname(input("Inserte la dirección ip o el host-name que desea escanear: "))

    scanPorts(objetivo)


except socket.gaierror:
    print(f"Nombre o direccion ip {rojo}incorrecto{estandar}")
except KeyboardInterrupt:
    print(f"""
        {amarillo}TALUEGO LUCAS{estandar}
""")
