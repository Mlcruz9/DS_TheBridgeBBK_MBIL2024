def prueba():
    print('Hola mundo')

if __name__ == "__main__":
    pizz = input("Buenas tardes, bienvenido al servicio de pedido online, ¿Cuántas pizzas desea?: ")

    direcc = input(f"Estupendo, se están preparando {pizz} pizzas!. Dígame su dirección: ")

    respuesta = f"Le mandaremos {pizz} pizzas a la dirección {direcc}"

    print(respuesta)