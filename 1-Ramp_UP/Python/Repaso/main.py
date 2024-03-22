import random
from variables import LISTA_PALABRAS, VIDAS
from funciones import ahorcado

palabra_elegida = random.choice(LISTA_PALABRAS)
palabra_elegida = palabra_elegida.upper()

palabra_oculta = "_" * len(palabra_elegida)
palabra_oculta = list(palabra_oculta)

print("Bienvenido al juego del ahorcado, disfruta bastante!")

ahorcado(vidas= VIDAS, palabra_elegida=palabra_elegida, palabra_oculta=palabra_oculta)