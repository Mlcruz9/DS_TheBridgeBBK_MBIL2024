import time
import random

def ahorcado(vidas, palabra_elegida, palabra_oculta):

    while vidas > 0:
        time.sleep(1)
        letra_usuario = input("Introduce una letra: ")
        letra_usuario = letra_usuario.upper()

        if letra_usuario in palabra_elegida:
            for i in range(len(palabra_elegida)):
                if palabra_elegida[i] == letra_usuario:
                    palabra_oculta[i] = letra_usuario
            
            if "_" not in palabra_oculta:
                print("Has ganado!")
                print(*palabra_oculta)
                break

            print("Has acertado!")
            print(*palabra_oculta)

        else:
            vidas -= 1
            print("Has fallado!")
            print(f'Vidas:{vidas}')
            print(*palabra_oculta)


            if vidas == 0:
                print("Has perdido :(")