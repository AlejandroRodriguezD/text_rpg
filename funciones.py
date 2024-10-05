import os

def viaje(puntero, mapas):
    mov = []
    print("Te encuentras en: " + puntero.localidad + "\nPuedes ir a: ")
    for i in mapas:
        if i.localidad != puntero.localidad:
            mov.append(i)
    print("Introduce el número a donde deseas ir")
    for numerador, i in enumerate(mov, start=1):
        print(f"{numerador}: {i.localidad}")
    te_mide = len(mov)
    viajar_a = int(input()) - 1
    os.system("cls||clear")
    if 0 <= viajar_a < te_mide:
        puntero = mov[viajar_a]
    else:
        print("El número no corresponde a ninguna localidad")
    return puntero