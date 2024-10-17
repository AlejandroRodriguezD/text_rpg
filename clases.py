class Personaje:
    def __init__(self, nombre, vida, dano, inventario=None):
        if inventario is None:
            inventario = []
        self.nombre = nombre
        self.gold = 100
        self.inventario = inventario
        #Stats verificar // Mejorar atributos, organizar
        self.vida = vida
        self.dano = dano

    def ver_inventario(self):
        print("Tienes: " + str(self.gold) + " monedas de oro")
        for item in self.inventario:
            print(f"{item.nombre}: {item.cantidad}")
        print("\n")

    def agregar_objeto(self, objeto, cantidad):
        for item in self.inventario:
            if item.nombre == objeto.nombre:
                item.cantidad += cantidad
                break
        else:
            self.inventario.append(objeto)
        #Evaluar formula para el ataque // Reubicar?
    def ataque(self, objetivo):
        while self.vida > 0 or objetivo.vida > 0:
            self.vida -= objetivo.dano
            objetivo.vida -= self.dano
            break
#Revisar sistema para implementar combates, esta clase es para enemigos-- heredar?
class Entidad(Personaje):
    def __init__(self, nombre, vida, dano, inventario=None):
        super().__init__(nombre, vida, dano, inventario)

    def ejecutar(self, jugador):
        pass
        
#Modificar actividad, dependiendo de su valor ejecutar distintas acciones
class Lugar:
    def __init__(self, localidad, descripcion, actividad= None):
        self.localidad = localidad
        self.descripcion = descripcion
        self.actividad = actividad
    
    def describir(self):
        print(self.descripcion)
    
    def llamar(self):
        if self.actividad:
            print(self.actividad.nombre)

        #Heredar a nueva clase NPC?
class Mercader:
    def __init__(self, nombre, lista_de_venta):
        self.nombre = nombre
        self.lista_de_venta = lista_de_venta

    def ejecutar(self, comprador):
        print("Elige lo que deseas comprar")
        for numerador, item in enumerate(self.lista_de_venta, start=1):
            print(f"{numerador}-{item.nombre}: {item.descripcion} {item.valor}G")
        
        print("¿Qué deseas comprar?")
        comprar = int(input()) - 1
        
        if 0 <= comprar < len(self.lista_de_venta):
            print("¿Cuántos deseas?")
            cantidad = int(input())
            if cantidad <= 0:
                print("Cantidad invalida")
            else:
                total_valor = self.lista_de_venta[comprar].valor * cantidad
                if total_valor <= comprador.gold:
                    comprador.gold -= total_valor
                    comprador.agregar_objeto(self.lista_de_venta[comprar], cantidad)
                    print("Inventario actualizado:")
                    comprador.ver_inventario()
                else:
                    print("No tienes suficiente G")
        else:
            print("El número no corresponde a los elementos listados")


class Objeto:
    def __init__(self, nombre, descripcion, valor, cantidad=1):
        self.nombre = nombre
        self.descripcion = descripcion
        self.valor = valor
        self.cantidad = cantidad


class Arma(Objeto):
    def __init__(self, nombre, descripcion, valor, dano, cantidad=1):
        super().__init__(nombre, descripcion, valor, cantidad)
        self.dano = dano