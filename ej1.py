# CI5651 - Diseño de Algoritmos I. Trimestre Enero - Marzo 2024
# Roberto Gamboa, 16-10394


# Para n = 3
# peticiones = [(p1,t1), (p2,t2), (p3,t3)]

def seleccionar_vallas(peticiones):
    # Ordenamos las peticiones por el punto donde termina la valla (p1 + t1)
    # Python utiliza el algoritmo Timsort, que pertenece al orden O(n log n)
    peticiones.sort(key=lambda x: x[0] + x[1])
    

    # Inicializamos el conjunto de las vallas seleccionadas con la valla que termina primero
    vallas = [peticiones[0]]

    # Se itera sobre las peticiones restantes
    # A lo sumo se realizaran n iteraciones
    while len(peticiones) > 0:

        # Si la peticion no se intersecta con la ultima valla en el conjunto de vallas aprobadas,
        # se agrega al conjunto de peticiones aprobadas
        # Si la peticion se intersecta, se descarta
        # La comparacion toma tiempo constante
        if peticiones[0][0] >= vallas[-1][0] + vallas[-1][1]:
            vallas.append(peticiones[0])
        peticiones.pop(0)
        
        
    # Devolvemos el conjunto de peticiones aprobadas
    return vallas


def main():
    peticiones = [(1, 4), (2, 1), (3, 3), (1,1),(3,1),(4,6),(5,2)]
    print("Vallas seleccionadas:")
    print(seleccionar_vallas(peticiones))

if __name__ == "__main__":
    main()