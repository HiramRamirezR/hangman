# si la letra es incorrecta, agregar una parte al cuerpo y reduce un intento
# si la letra ya ha sido ingresada, mostrar un mensaje de error
# comenzar el juego con 6 intentos

import random

# list of words
words = [
    "gato", "perro", "casa", "flor", "sol", "luna", "mar", "agua", "pato", "río",
    "nube", "tren", "pan", "luz", "cielo", "amor", "rojo", "azul", "verde", "ratón",
    "nieve", "rey", "reina", "piedra", "tigre", "pez", "león", "oso", "mono", "arroz",
    "playa", "juguete", "silla", "mesa", "carro", "ventana", "fruta", "bici", "yogur",
    "globo", "delfín", "cebra", "goma", "manzana", "pera", "lago", "barco", "zorro",
    "pájaro", "niño", "niña", "dado", "dedo", "cama", "camión", "ratón", "lápiz",
    "tierra", "sola", "papel", "cuchara", "bomba", "abeja", "limón", "bota", "rana",
    "conejo", "caballo", "cabra", "pollo", "grillo", "pluma", "estrella", "sandía",
    "naranja", "melón", "chicle", "mango", "bailar", "cantar", "saltar", "comer",
    "leer", "escribir", "parque", "jirafa", "plato", "sopa", "agua", "foca", "sapo",
    "nido", "caracol", "abeja", "botella", "pelota", "cuadro", "reloj", "zapato",
    "playa", "helado", "bruja", "banda", "circo"
]

person = [
"""
 +---+
 |   |
 |
 |
 |
=========
""",
"""
 +---+
 |   |
 |   O
 |
 |
=========
""",
"""
 +---+
 |   |
 |   O
 |   |
 |
=======
""",
"""
 +---+
 |   |
 |   O
 |  /|
 |
=========
""",
"""
 +---+
 |   |
 |   O
 |  /|\
 |
=========
""",
"""
 +---+
 |   |
 |   O
 |  /|\
 |  /
 |
=========
""",
"""
 +---+
 |   |
 |   O
 |  /|\
 |  / \
 |
=========
"""
]

word = random.choice(words)

letters = []
attempts = 6
spaces = ["_"] * len(word)

print(f"Vamos a comenzar el juego.\nTu palabra tiene {len(word)} letras.\n")
print(person[0])
print(f"{spaces}\n")


while attempts > 0:

    letter = input(f"Ingresa una letra. Tienes {attempts} intentos.\n")

    if letter in letters:
        print(f"\n-------------------------------------\nYa has ingresado la letra '{letter}'.")
        print(f"{spaces}\n")
        continue

    # add the letter to the list
    letters.append(letter)

    # check if the letter is in the word
    if letter in word:
        # replace the "_" with the letter in the word
        for i, char in enumerate(word):
            if char == letter:
                spaces[i] = letter
        print("\n-------------------------------------\n!Bien hecho, sigue adelante! \n")

    else:
        print(f"\n-------------------------------------\nLa letra '{letter}' no está en la palabra.")
        attempts -= 1

    print(person[6 - attempts])
    print(f"{spaces}\n")

    if "_" not in spaces:
        print("¡Felicidades! Has adivinado la palabra correctamente.")
        break

if attempts == 0:
    print(f"Fin del juego. La palabra era '{word}'.")
