import clases
import funciones
import os
import time

#inicializan los objetos. Personajes, items y mapas
item = [
    clases.Objeto("Perla", "Brilla mucho, vale más", 300),
    clases.Arma("Palo", "Pega poco", 1, 1),
    clases.Arma("Espada del novato", "Espada ligera para principiantes", 30, 5)
]

enemigo = clases.Entidad("Pitufo", 50, 1)
heroe = clases.Personaje("Jilbatran", 20, 3)
mercader = clases.Mercader("Juan", item)

mapas = [
    clases.Lugar("Campo", "Un campo abierto repletos de monstruos debiles", enemigo),
    clases.Lugar("Bazar", "Un sitio desordenado con 3 tiendas diferentes", mercader),
    clases.Lugar("Castillo", "Un enorme castillo custodiado por guardias"),
]

#ubicamos al jugador 
puntero = mapas[0]
accion = 0

#Cambiar el sistema de mercado a tipo de ubicacion para admitir areas de combate

#Bucle principal
while accion != 9:
    try:
        print(f"Ubicación actual: {puntero.localidad}\n{puntero.descripcion}")
        if puntero.actividad:
            print("¡Puedes comerciar!")
        print("\nSelecciona una acción \n1: Viajar \n2: Comprar \n3: Ver Inventario \n9: Salir")
        accion = int(input())
        os.system("cls||clear")
        match accion:
            case 1:
                puntero = funciones.viaje(puntero, mapas)
            case 2:
                if puntero.actividad == mercader:
                    puntero.actividad.vender(heroe)
                    time.sleep(3)
                else:
                    print("No existe accion a llevar a cabo\n")
                    time.sleep(2)
            case 3:
                heroe.ver_inventario()
                print("Presione ENTER para continuar")
                input()
            case 4:
                heroe.ataque(puntero.actividad)
            case 9:
                print("¡Adiós!")
            case _:
                print("Comando inválido")
    except ValueError:
        print("No es una entrada válida")