import sys

def tiempo_minimo(rivales):
    # Orden greedy por a_i descendente
    rivales_ordenados = sorted(rivales, key=lambda x: x[1], reverse=True)

    tiempo_scaloni = 0
    tiempo_total = 0 

    for s_i, a_i in rivales_ordenados:
        tiempo_scaloni += s_i
        final = tiempo_scaloni + a_i
        tiempo_total = max(tiempo_total, final)

    return tiempo_total, rivales_ordenados


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 tp1.py archivo.txt")
        return

    ruta_archivo = sys.argv[1]
    rivales = []   

    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = [linea.strip() for linea in archivo if linea.strip()]

            if not lineas:
                return

            for linea in lineas[1:]:
                partes = linea.split(",")
                if len(partes) == 2:
                    s_i = int(partes[0])
                    a_i = int(partes[1])
                    rivales.append((s_i, a_i))
  
        resultado = tiempo_minimo(rivales)
        tiempo_total, rivales_ordenados = resultado

        print("=== Resultado ===\n")  
        print(f"Tiempo mínimo total: {tiempo_total}\n")
        print("Orden de los rivales:", rivales_ordenados)
    

       
    except FileNotFoundError:
        print("Error: archivo no encontrado")
    except ValueError:
        print("Error: formato inválido")

if __name__ == "__main__":
    main()